from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Enum as SQLEnum, Text, JSON, Float
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import enum
from datetime import datetime


class ExamType(str, enum.Enum):
    """Exam type enumeration."""
    THEORY = "theory"  # 理论考试
    PRACTICE_BASIC = "practice_basic"  # 实操基础
    PRACTICE_ADVANCED = "practice_advanced"  # 实操进阶
    COMPREHENSIVE = "comprehensive"  # 综合考试


class ExamStatus(str, enum.Enum):
    """Exam status enumeration."""
    PENDING = "pending"  # 待开始
    IN_PROGRESS = "in_progress"  # 进行中
    COMPLETED = "completed"  # 已完成
    CANCELLED = "cancelled"  # 已取消


class ExamProduct(Base):
    """Exam product model."""
    __tablename__ = "exam_products"
    
    name = Column(String(200), nullable=False)
    code = Column(String(50), unique=True, index=True)
    exam_type = Column(SQLEnum(ExamType), nullable=False)
    description = Column(Text)
    duration_minutes = Column(Integer, default=60)  # 考试时长（分钟）
    pass_score = Column(Integer, default=70)  # 及格分数
    total_score = Column(Integer, default=100)  # 总分
    price = Column(Float, default=0.0)  # 考试费用
    requirements = Column(JSON)  # 考试要求
    
    # Relationships
    exam_sessions = relationship("ExamSession", back_populates="product")
    

class ExamSession(Base):
    """Exam session model."""
    __tablename__ = "exam_sessions"
    
    # Basic information
    session_code = Column(String(50), unique=True, index=True)
    name = Column(String(200), nullable=False)
    
    # Foreign keys
    product_id = Column(Integer, ForeignKey("exam_products.id"), nullable=False)
    site_id = Column(Integer, ForeignKey("sites.id"), nullable=False)
    
    # Schedule
    exam_date = Column(DateTime, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    
    # Capacity
    max_candidates = Column(Integer, default=30)
    registered_count = Column(Integer, default=0)
    
    # Status
    status = Column(SQLEnum(ExamStatus), default=ExamStatus.PENDING)
    
    # Relationships
    product = relationship("ExamProduct", back_populates="exam_sessions")
    site = relationship("Site", back_populates="exam_sessions")
    registrations = relationship("ExamRegistration", back_populates="session")
    schedules = relationship("ExamSchedule", back_populates="session")
    

class ExamRoom(Base):
    """Exam room model."""
    __tablename__ = "exam_rooms"
    
    # Basic information
    room_number = Column(String(50), nullable=False)
    room_name = Column(String(100))
    room_type = Column(String(50))  # theory/practice
    
    # Foreign key
    site_id = Column(Integer, ForeignKey("sites.id"), nullable=False)
    
    # Capacity
    capacity = Column(Integer, default=30)
    
    # Equipment
    equipment = Column(JSON)
    
    # Relationships
    site = relationship("Site", back_populates="exam_rooms")
    schedules = relationship("ExamSchedule", back_populates="room")