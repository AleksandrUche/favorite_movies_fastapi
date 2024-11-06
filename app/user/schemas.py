from typing import Optional

from pydantic import BaseModel, ConfigDict


class UserBaseDTO(BaseModel):
    name: Optional[str] = None


class UserBaseInDbDTO(UserBaseDTO):
    model_config = ConfigDict(from_attributes=True)
    id: int = None


class UserCreateDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    password: str


class UserDTO(UserBaseInDbDTO):
    pass


# Токен

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    user_id: int = None
