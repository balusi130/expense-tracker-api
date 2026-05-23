# Changelog

## [1.2.0]
- Add budget alert at 80% threshold — returns warning in summary response
- Add pagination support to GET /expenses (skip + limit params)
- Fix: CSV export was not including expenses from the current day

## [1.1.0]
- Add JWT authentication with bcrypt password hashing
- Add Docker Compose with PostgreSQL service
- Add .env.example for easier local setup

## [1.0.0]
- Initial release
- Expense CRUD, category filtering, monthly summary
- CSV export endpoint