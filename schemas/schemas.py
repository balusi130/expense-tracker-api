from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class ExpenseCreate(BaseModel):
    amount: float = Field(..., gt=0, description="Amount must be greater than 0")
    category: str
    description: Optional[str] = ""


class ExpenseOut(BaseModel):
    id: int
    amount: float
    category: str
    description: str
    created_at: datetime

    class Config:
        from_attributes = True


class BudgetCreate(BaseModel):
    category: str
    limit: float = Field(..., gt=0)


class UserCreate(BaseModel):
    email: str
    password: str
