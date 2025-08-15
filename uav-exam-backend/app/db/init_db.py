from sqlalchemy.orm import Session
from app.core.config import settings
from app.core.security import get_password_hash
from app.models.user import User, UserRole
from app.models.organization import Organization
from app.models.site import Site
from app.models.exam import ExamProduct, ExamType
from app.db.base import engine, Base
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_db(db: Session) -> None:
    """Initialize database with default data."""
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    # Check if superuser exists
    superuser = db.query(User).filter(
        User.email == settings.FIRST_SUPERUSER_EMAIL
    ).first()
    
    if not superuser:
        # Create superuser
        superuser = User(
            email=settings.FIRST_SUPERUSER_EMAIL,
            username="admin",
            hashed_password=get_password_hash(settings.FIRST_SUPERUSER_PASSWORD),
            full_name=settings.FIRST_SUPERUSER_NAME,
            role=UserRole.SUPER_ADMIN,
            is_superuser=True,
            is_active=True,
            is_verified=True
        )
        db.add(superuser)
        logger.info("Created superuser")
    
    # Create default site
    default_site = db.query(Site).filter(Site.code == "SITE001").first()
    if not default_site:
        default_site = Site(
            name="福州无人机考试中心",
            code="SITE001",
            site_type="comprehensive",
            province="福建省",
            city="福州市",
            district="仓山区",
            address="福州市仓山区科技园路1号",
            contact_person="张管理",
            contact_phone="13800138000",
            contact_email="admin@uavexam.com",
            theory_room_capacity=50,
            practice_stations=10,
            latitude=26.0745,
            longitude=119.2965
        )
        db.add(default_site)
        logger.info("Created default site")
    
    # Create default organization
    default_org = db.query(Organization).filter(
        Organization.code == "ORG001"
    ).first()
    if not default_org:
        default_org = Organization(
            name="福州飞翔无人机培训学校",
            code="ORG001",
            contact_person="李校长",
            contact_phone="13900139000",
            contact_email="contact@fxuav.com",
            province="福建省",
            city="福州市",
            district="鼓楼区",
            address="福州市鼓楼区五四路1号",
            business_license="91350100MA000000XX"
        )
        db.add(default_org)
        logger.info("Created default organization")
    
    # Create exam products
    exam_products = [
        {
            "name": "无人机理论考试",
            "code": "EXAM_THEORY",
            "exam_type": ExamType.THEORY,
            "duration_minutes": 120,
            "pass_score": 70,
            "total_score": 100,
            "price": 200.0
        },
        {
            "name": "无人机实操基础考试",
            "code": "EXAM_PRACTICE_BASIC",
            "exam_type": ExamType.PRACTICE_BASIC,
            "duration_minutes": 30,
            "pass_score": 80,
            "total_score": 100,
            "price": 500.0
        },
        {
            "name": "无人机实操进阶考试",
            "code": "EXAM_PRACTICE_ADV",
            "exam_type": ExamType.PRACTICE_ADVANCED,
            "duration_minutes": 45,
            "pass_score": 80,
            "total_score": 100,
            "price": 800.0
        }
    ]
    
    for product_data in exam_products:
        product = db.query(ExamProduct).filter(
            ExamProduct.code == product_data["code"]
        ).first()
        if not product:
            product = ExamProduct(**product_data)
            db.add(product)
            logger.info(f"Created exam product: {product_data['name']}")
    
    db.commit()
    logger.info("Database initialized successfully")


if __name__ == "__main__":
    from app.db.base import SessionLocal
    db = SessionLocal()
    try:
        init_db(db)
    finally:
        db.close()