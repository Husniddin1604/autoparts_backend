from datetime import datetime, timezone
import jwt
from fastapi import HTTPException, status

from core.security import decode_token, create_access_token, create_refresh_token
from core.redis import redis_client
from services.ports import AuthServiceABC
from uow.ports import UnitOfWorkABC


class AuthService(AuthServiceABC):
    """
    AuthService is a concrete implementation of AuthServiceABC.
    """

    def __init__(
        self,
        uow: UnitOfWorkABC,
    ):
        self.uow = uow

    async def verify_access_token(self, token: str) -> dict:
        try:
            payload = decode_token(token)

            if payload.get("type") != "access":
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid token type.",
                )

            jti = payload.get("jti")
            if jti:
                is_blacklisted = await redis_client.get(f"blacklist:{jti}")
                if is_blacklisted:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Token has been invalidated (logged out).",
                    )

            return payload

        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
            )

        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
            )

    async def verify_refresh_token(self, token: str) -> dict:
        try:
            payload = decode_token(token)

            if payload.get("type") != "refresh":
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid token type.",
                )

            jti = payload.get("jti")
            if jti:
                is_blacklisted = await redis_client.get(f"blacklist:{jti}")
                if is_blacklisted:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Refresh token has been invalidated.",
                    )

            return payload

        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Refresh token has expired.",
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token.",
            )

    async def logout(self, token: str, verify_exp=False) -> dict:
        try:
            payload = decode_token(token)

            jti = payload.get("jti")
            exp = payload.get("exp")

            await self.blacklist_jti(jti, exp)

            return {"message": "Logged out successfully"}

        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )


    async def login_with_email(self, email: str, password: str) -> dict:
        user = await self.uow.user.get_by_email(email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
            )

        is_correct = user.check_password(password)

        if not is_correct:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
            )


        access_token = create_access_token(str(user.user_uuid), user.email)
        refresh_token = create_refresh_token(str(user.user_uuid), user.email)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    async def login_with_username(self, username: str, password: str) -> dict:
        user = await self.uow.user.get_by_username(username)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
            )

        is_correct = user.check_password(password)

        if not is_correct:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
            )

        access_token = create_access_token(str(user.user_uuid), user.email)
        refresh_token = create_refresh_token(str(user.user_uuid), user.email)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    async def refresh_token(self, token: str) -> dict:
        refresh_token = await self.verify_refresh_token(token)
        user_uuid = refresh_token.get("user_uuid")
        user_email = refresh_token.get("user_email")

        access_token = create_access_token(str(user_uuid), str(user_email))
        refresh_token = create_refresh_token(str(user_uuid), str(user_email))

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }


    async def blacklist_jti(self, jti: str, exp: int) -> None:
        now_ts = int(datetime.now(timezone.utc).timestamp())
        ttl = exp - now_ts
        if ttl > 0:
            await redis_client.setex(f"blacklist:{jti}", ttl, "true")
