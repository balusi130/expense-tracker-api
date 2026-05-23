from fastapi import FastAPI
from routers import auth, expenses, budgets
from core.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Expense Tracker API",
    description="Track personal and team expenses with budget alerts and CSV export.",
    version="1.0.0"
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(expenses.router, prefix="/expenses", tags=["Expenses"])
app.include_router(budgets.router, prefix="/budgets", tags=["Budgets"])


@app.get("/")
def root():
    return {"message": "Expense Tracker API is running"}
