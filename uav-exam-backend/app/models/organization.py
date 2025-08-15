from sqlalchemy import Column, String, Text, Integer
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Organization(Base):
    """Training organization model."""
    __tablename__ = "organizations"
    
    # Basic information
    name = Column(String(200), nullable=False, unique=True)
    code = Column(String(50), unique=True, index=True)  # 机构代码
    contact_person = Column(String(100))
    contact_phone = Column(String(20))
    contact_email = Column(String(255))
    
    # Address
    province = Column(String(50))
    city = Column(String(50))
    district = Column(String(50))
    address = Column(String(500))
    
    # Business information
    business_license = Column(String(100))  # 营业执照号
    license_url = Column(String(500))  # 营业执照照片
    description = Column(Text)
    
    # Statistics
    total_candidates = Column(Integer, default=0)
    total_exams = Column(Integer, default=0)
    
    # Relationships
    users = relationship("User", back_populates="organization")
    exam_registrations = relationship("ExamRegistration", back_populates="organization")
    
    def __repr__(self):
        return f"<Organization {self.name}>"