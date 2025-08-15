from sqlalchemy import Column, String, Integer, Text, JSON, Float
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Site(Base):
    """Exam site model."""
    __tablename__ = "sites"
    
    # Basic information
    name = Column(String(200), nullable=False, unique=True)
    code = Column(String(50), unique=True, index=True)  # 考点代码
    site_type = Column(String(50))  # 考点类型
    
    # Location
    province = Column(String(50))
    city = Column(String(50))
    district = Column(String(50))
    address = Column(String(500))
    latitude = Column(Float)  # 纬度
    longitude = Column(Float)  # 经度
    
    # Contact
    contact_person = Column(String(100))
    contact_phone = Column(String(20))
    contact_email = Column(String(255))
    
    # Capacity
    theory_room_capacity = Column(Integer, default=30)  # 理论考场容量
    practice_stations = Column(Integer, default=5)  # 实操考位数
    
    # Facilities
    facilities = Column(JSON)  # 设施信息
    equipment = Column(JSON)  # 设备信息
    
    # Additional info
    description = Column(Text)
    images = Column(JSON)  # 考点图片列表
    business_hours = Column(JSON)  # 营业时间
    
    # Relationships
    staff = relationship("User", back_populates="site")
    exam_sessions = relationship("ExamSession", back_populates="site")
    exam_rooms = relationship("ExamRoom", back_populates="site")
    
    def __repr__(self):
        return f"<Site {self.name}>"