from pydantic import BaseModel, HttpUrl


class LoginResponse(BaseModel):
    token: str