"""
认证相关 Pydantic 模型
"""

from pydantic import BaseModel, EmailStr, Field


class UserRegister(BaseModel):
    email: EmailStr
    username: str = Field(min_length=2, max_length=50)
    password: str = Field(min_length=6, max_length=100)
    code: str = Field(min_length=6, max_length=6, description="邮箱验证码")


class SendCodeRequest(BaseModel):
    email: EmailStr


class SendCodeResponse(BaseModel):
    message: str
    resend_after: int = 60


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: "UserOut"


class UserOut(BaseModel):
    id: str
    email: str
    username: str
    avatar_url: str | None = None
    is_active: bool

    model_config = {"from_attributes": True}
