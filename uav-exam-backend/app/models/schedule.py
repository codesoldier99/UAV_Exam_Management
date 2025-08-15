from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Enum as SQLEnum, Text
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import enum
from datetime import datetime


class ScheduleStatus(str, enum.Enum):
    """Schedule status enumeration."""
    SCHEDULED = "scheduled"  # 已排期
    CHECKED_IN = "checked_in"  # 已签到
    IN_EXAM = "in_exam"  # 考试中
    COMPLETED = "completed"  # 已完成
    ABSENT = "absent"  # 缺考
    CANCELLED = "cancelled"  # 已取消


class ExamSchedule(Base):
    """Exam schedule model."""
    __tablename__ = "exam_schedules"
    
    # Foreign keys
    candidate_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    session_id = Column(Integer, ForeignKey("exam_sessions.id"), nullable=False)
    registration_id = Column(Integer, ForeignKey("exam_registrations.id"), nullable=False)
    room_id = Column(Integer, ForeignKey("exam_rooms.id"), nullable=True)
    
    # Schedule info
    seat_number = Column(String(20))  # 座位号
    group_number = Column(String(20))  # 分组号
    scheduled_time = Column(DateTime, nullable=False)
    actual_start_time = Column(DateTime, nullable=True)
    actual_end_time = Column(DateTime, nullable=True)
    
    # Status
    status = Column(SQLEnum(ScheduleStatus), default=ScheduleStatus.SCHEDULED)
    
    # Additional info
    remarks = Column(Text)
    
    # Relationships
    candidate = relationship("User", back_populates="exam_schedules")
    session = relationship("ExamSession", back_populates="schedules")
    registration = relationship("ExamRegistration", back_populates="schedule")
    room = relationship("ExamRoom", back_populates="schedules")
    checkin_records = relationship("CheckinRecord", back_populates="schedule")