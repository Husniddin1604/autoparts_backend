from pydantic import BaseModel


class LoginWithUsernameRequest(BaseModel):
    username: str
    password: str


class LoginWithEmailRequest(BaseModel):
    email: str
    password: str

