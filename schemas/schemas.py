from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True


class ExpenseCreate(BaseModel):
    amount: float
    category: str
    description: Optional[str] = None


class ExpenseOut(ExpenseCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class BudgetCreate(BaseModel):
    category: str
    limit_amount: float
    alert_threshold: float = 0.8


class BudgetOut(BudgetCreate):
    id: int

    class Config:
        from_attributes = True
