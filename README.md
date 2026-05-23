# expense-tracker-api

A REST API for tracking personal and team expenses. I built this partly out of frustration with spreadsheets — I wanted something I could actually query, that would tell me where money was going across categories and flag when I was close to a budget limit.

It is built with Python and FastAPI, uses PostgreSQL for storage, and includes JWT-based auth so multiple users can have separate accounts without their data mixing. The CSV export was an afterthought that ended up being one of the most used features in testing.

---

## Features

- User registration and login with JWT authentication
- Create and categorise expenses (food, transport, utilities, etc.)
- Set monthly budget limits per category with automatic alerts when you hit 80%
- Monthly and weekly summary endpoints
- Export expenses to CSV by date range or category
- Pagination on all list endpoints

---

## Stack

- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy (ORM)
- Alembic (migrations)
- JWT (python-jose)
- Docker + Docker Compose

---

## Getting started

```bash
git clone https://github.com/balusi130/expense-tracker-api.git
cd expense-tracker-api
cp .env.example .env   # fill in your DB credentials and secret key
docker-compose up --build
```

The API will be running at `http://localhost:8000`. Interactive docs at `http://localhost:8000/docs`.

---

## API overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Create a new user account |
| POST | `/auth/login` | Get a JWT token |
| POST | `/expenses` | Log a new expense |
| GET | `/expenses` | List expenses (paginated, filterable) |
| GET | `/expenses/summary` | Monthly breakdown by category |
| GET | `/expenses/export` | Download CSV |
| POST | `/budgets` | Set a category budget limit |
| GET | `/budgets` | View all budget limits and current usage |

---

## Running tests

```bash
pip install -r requirements.txt
pytest tests/ -v
```

---

## Project structure

```
expense-tracker-api/
├── main.py
├── routers/
│   ├── auth.py
│   ├── expenses.py
│   └── budgets.py
├── models/
│   ├── user.py
│   ├── expense.py
│   └── budget.py
├── schemas/
│   └── schemas.py
├── core/
│   ├── database.py
│   └── security.py
├── tests/
│   └── test_expenses.py
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

MIT License