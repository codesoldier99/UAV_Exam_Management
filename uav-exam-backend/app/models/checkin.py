from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Enum as SQLEnum, Text
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import enum
from datetime import datetime


class CheckinType(str, enum.Enum):
    """Check-in type enumeration."""
    ARRIVAL = "arrival"  # 到达考点
    THEORY_ENTER = "theory_enter"  # 进入理论考场
    THEORY_EXIT = "theory_exit"  # 离开理论考场
    PRACTICE_ENTER = "practice_enter"  # 进入实操考场
    PRACTICE_EXIT = "practice_exit"  # 离开实操考场
    DEPARTURE = "departure"  # 离开考点


class CheckinRecord(Base):
    """Check-in record model."""
    __tablename__ = "checkin_records"
    
    # Foreign keys
    candidate_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    schedule_id = Column(Integer, ForeignKey("exam_schedules.id"), nullable=False)
    examiner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Check-in info
    checkin_type = Column(SQLEnum(CheckinType), nullable=False)
    checkin_time = Column(DateTime, default=datetime.utcnow)
    
    # Location info
    location = Column(String(200))  # 签到地点
    device_info = Column(String(200))  # 设备信息
    
    # QR code info
    qr_code = Column(String(500))  # 二维码内容
    qr_valid = Column(Integer, default=1)  # 二维码是否有效
    
    # Additional info
    remarks = Column(Text)
    photo_url = Column(String(500))  # 现场照片
    
    # Relationships
    candidate = relationship("User", foreign_keys=[candidate_id], back_populates="checkin_records")
    schedule = relationship("ExamSchedule", back_populates="checkin_records")
    examiner = relationship("User", foreign_keys=[examiner_id])