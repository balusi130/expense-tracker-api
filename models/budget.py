from sqlalchemy import Column, Integer, String, Float, ForeignKey
from core.database import Base


class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category = Column(String, nullable=False)
    limit_amount = Column(Float, nullable=False)
    alert_threshold = Column(Float, default=0.8)  # alert at 80% by default
