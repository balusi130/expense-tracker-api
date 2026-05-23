from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from core.database import get_db
from core.security import get_current_user
from models.expense import Expense
from schemas.schemas import ExpenseCreate, ExpenseOut
from datetime import datetime
import csv, io

router = APIRouter()


@router.post("/", response_model=ExpenseOut)
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_expense = Expense(**expense.dict(), user_id=user.id, created_at=datetime.utcnow())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense


@router.get("/", response_model=list[ExpenseOut])
def list_expenses(
    category: str = None,
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    query = db.query(Expense).filter(Expense.user_id == user.id)
    if category:
        query = query.filter(Expense.category == category)
    return query.offset(skip).limit(limit).all()


@router.get("/summary")
def monthly_summary(db: Session = Depends(get_db), user=Depends(get_current_user)):
    expenses = db.query(Expense).filter(Expense.user_id == user.id).all()
    summary = {}
    for e in expenses:
        month = e.created_at.strftime("%Y-%m")
        summary.setdefault(month, {}).setdefault(e.category, 0)
        summary[month][e.category] += e.amount
    return summary


@router.get("/export")
def export_csv(db: Session = Depends(get_db), user=Depends(get_current_user)):
    expenses = db.query(Expense).filter(Expense.user_id == user.id).all()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Date", "Category", "Amount", "Description"])
    for e in expenses:
        writer.writerow([e.created_at.date(), e.category, e.amount, e.description])
    output.seek(0)
    return StreamingResponse(output, media_type="text/csv",
                             headers={"Content-Disposition": "attachment; filename=expenses.csv"})
