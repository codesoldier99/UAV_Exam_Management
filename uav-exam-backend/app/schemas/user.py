from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, validator
from app.models.user import UserRole


class UserBase(BaseModel):
    """Base user schema."""
    email: EmailStr
    username: Optional[str] = None
    full_name: Optional[str] = None
    phone: Optional[str] = None
    role: UserRole = UserRole.CANDIDATE
    is_active: bool = True
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    

class UserCreate(UserBase):
    """User creation schema."""
    password: str = Field(..., min_length=6, max_length=50)
    
    @validator('password')
    def validate_password(cls, v):
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters long')
        return v


class UserUpdate(BaseModel):
    """User update schema."""
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    full_name: Optional[str] = None
    phone: Optional[str] = None
    password: Optional[str] = Field(None, min_length=6, max_length=50)
    role: Optional[UserRole] = None
    is_active: Optional[bool] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    avatar_url: Optional[str] = None
    id_card: Optional[str] = None
    gender: Optional[str] = None
    birth_date: Optional[datetime] = None
    address: Optional[str] = None


class UserInDB(UserBase):
    """User in database schema."""
    id: int
    created_at: datetime
    updated_at: datetime
    is_verified: bool = False
    is_superuser: bool = False
    last_login: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class User(UserInDB):
    """User response schema."""
    pass


class UserLogin(BaseModel):
    """User login schema."""
    username: str  # Can be email or username
    password: str


class Token(BaseModel):
    """Token schema."""
    access_token: str
    refresh_token: Optional[str] = None
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    """Token payload schema."""
    sub: Optional[int] = None
    exp: Optional[int] = None
    type: Optional[str] = None


class PasswordReset(BaseModel):
    """Password reset schema."""
    old_password: str
    new_password: str = Field(..., min_length=6, max_length=50)


class WeChatLogin(BaseModel):
    """WeChat login schema."""
    code: str
    user_info: Optional[dict] = None