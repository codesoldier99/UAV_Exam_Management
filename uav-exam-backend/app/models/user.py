from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, Enum as SQLEnum, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import enum
from datetime import datetime


class UserRole(str, enum.Enum):
    """User roles enumeration."""
    SUPER_ADMIN = "super_admin"  # 超级管理员
    SITE_ADMIN = "site_admin"    # 考点管理员
    ORG_ADMIN = "org_admin"      # 培训机构管理员
    EXAMINER = "examiner"        # 考务人员
    CANDIDATE = "candidate"      # 考生


class User(Base):
    """User model."""
    __tablename__ = "users"
    
    # Basic information
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(100))
    phone = Column(String(20), unique=True, index=True)
    
    # Role and permissions
    role = Column(SQLEnum(UserRole), default=UserRole.CANDIDATE, nullable=False)
    is_superuser = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)
    
    # Organization relationship
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=True)
    organization = relationship("Organization", back_populates="users")
    
    # Site relationship (for site admins and examiners)
    site_id = Column(Integer, ForeignKey("sites.id"), nullable=True)
    site = relationship("Site", back_populates="staff")
    
    # WeChat Mini Program
    wechat_openid = Column(String(255), unique=True, nullable=True)
    wechat_unionid = Column(String(255), unique=True, nullable=True)
    wechat_session_key = Column(String(255), nullable=True)
    
    # Profile
    avatar_url = Column(String(500), nullable=True)
    id_card = Column(String(18), unique=True, nullable=True)  # 身份证号
    gender = Column(String(10), nullable=True)
    birth_date = Column(DateTime, nullable=True)
    address = Column(String(500), nullable=True)
    
    # Timestamps
    last_login = Column(DateTime, nullable=True)
    email_verified_at = Column(DateTime, nullable=True)
    phone_verified_at = Column(DateTime, nullable=True)
    
    # Relationships
    exam_registrations = relationship("ExamRegistration", back_populates="candidate")
    exam_schedules = relationship("ExamSchedule", back_populates="candidate")
    checkin_records = relationship("CheckinRecord", back_populates="candidate")
    
    def __repr__(self):
        return f"<User {self.email}>"