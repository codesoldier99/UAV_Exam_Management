from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Enum as SQLEnum, Text, Boolean
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import enum
from datetime import datetime


class RegistrationStatus(str, enum.Enum):
    """Registration status enumeration."""
    PENDING = "pending"  # 待审核
    APPROVED = "approved"  # 已通过
    REJECTED = "rejected"  # 已拒绝
    CANCELLED = "cancelled"  # 已取消
    COMPLETED = "completed"  # 已完成


class ExamRegistration(Base):
    """Exam registration model."""
    __tablename__ = "exam_registrations"
    
    # Registration number
    registration_number = Column(String(50), unique=True, index=True)
    
    # Foreign keys
    candidate_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    session_id = Column(Integer, ForeignKey("exam_sessions.id"), nullable=False)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=True)
    
    # Status
    status = Column(SQLEnum(RegistrationStatus), default=RegistrationStatus.PENDING)
    
    # Registration info
    registered_at = Column(DateTime, default=datetime.utcnow)
    approved_at = Column(DateTime, nullable=True)
    approved_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    # Additional info
    remarks = Column(Text)
    is_paid = Column(Boolean, default=False)
    payment_amount = Column(Integer, default=0)
    payment_at = Column(DateTime, nullable=True)
    
    # Emergency contact
    emergency_contact = Column(String(100))
    emergency_phone = Column(String(20))
    
    # Relationships
    candidate = relationship("User", foreign_keys=[candidate_id], back_populates="exam_registrations")
    session = relationship("ExamSession", back_populates="registrations")
    organization = relationship("Organization", back_populates="exam_registrations")
    approver = relationship("User", foreign_keys=[approved_by])
    schedule = relationship("ExamSchedule", back_populates="registration", uselist=False)