import uuid
import bcrypt

from models.base import Base
from sqlalchemy import Boolean, String, event
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "users"

    user_uuid: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        default=uuid.uuid4,
        unique=True,
        nullable=False,
        index=True,
    )
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    _password: Mapped[str] = mapped_column(String, nullable=False)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    middle_name: Mapped[str | None] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    phone: Mapped[str | None] = mapped_column(String, nullable=False)
    is_staff: Mapped[bool] = mapped_column(Boolean, default=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        if value:
            salt = bcrypt.gensalt()
            self._password = bcrypt.hashpw(value.encode('utf-8'), salt).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), self._password.encode('utf-8'))

    def __repr__(self):
        return self.username


@event.listens_for(User, 'before_insert')
@event.listens_for(User, 'before_update')
def hash_password_before_save(mapper, connection, target):
    if hasattr(target, '_password') and target._password:
        if not target._password.startswith('$2b$'):
            salt = bcrypt.gensalt()
            target._password = bcrypt.hashpw(target._password.encode('utf-8'), salt).decode('utf-8')