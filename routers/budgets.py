from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from core.security import get_current_user
from models.expense import Expense
from schemas.schemas import BudgetCreate
from datetime import datetime

router = APIRouter()

# In-memory budget store (would be DB in production)
budgets = {}


@router.post("/")
def set_budget(budget: BudgetCreate, user=Depends(get_current_user)):
    budgets[f"{user}:{budget.category}"] = budget.limit
    return {"message": f"Budget set for {budget.category}", "limit": budget.limit}


@router.get("/")
def get_budgets(db: Session = Depends(get_db), user=Depends(get_current_user)):
    now = datetime.utcnow()
    result = []
    for key, limit in budgets.items():
        uid, category = key.split(":", 1)
        if uid != str(user):
            continue
        spent = db.query(Expense).filter(
            Expense.user_id == user,
            Expense.category == category,
            Expense.created_at >= now.replace(day=1, hour=0, minute=0, second=0)
        ).all()
        total_spent = sum(e.amount for e in spent)
        pct = (total_spent / limit) * 100 if limit else 0
        result.append({
            "category": category,
            "limit": limit,
            "spent": total_spent,
            "usage_pct": round(pct, 1),
            "alert": pct >= 80
        })
    return result
