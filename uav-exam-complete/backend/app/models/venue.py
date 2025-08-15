from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base


class Venue(Base):
    """考场模型"""
    __tablename__ = "venues"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True, comment="考场名称")
    code = Column(String(50), unique=True, index=True, comment="考场编码")
    address = Column(String(255), comment="考场地址")
    location = Column(String(255), comment="考场位置")
    contact_person = Column(String(50), comment="联系人")
    contact_phone = Column(String(20), comment="联系电话")
    capacity = Column(Integer, default=30, comment="考场容量")
    latitude = Column(Float, comment="纬度")
    longitude = Column(Float, comment="经度")
    is_active = Column(Boolean, default=True, comment="是否启用")
    status = Column(String(20), default="active", comment="状态：active/inactive")
    description = Column(Text, comment="考场描述")
    facilities = Column(String(500), comment="设施说明")
    
    # 时间戳
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    schedules = relationship("Schedule", back_populates="venue")