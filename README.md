"""markdown
# ALX Travel App - Phase 0: Database Modeling and Data Seeding

A small Django application demonstrating database modeling, API serialization, and data seeding for travel listings, bookings, and reviews.

## Quick Start (Windows / PowerShell)

1. Clone the repository:
   ```powershell
   git clone <repo-url> alx_travel_app_0x01
   cd alx_travel_app_0x01
   ```

2. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```powershell
   cd alx_travel_app
   python manage.py migrate
   ```

5. (Optional) Seed the database (project includes `listings/management/commands/seed.py`):
   ```powershell
   python manage.py seed
   ```

6. Run the development server:
   ```powershell
   python manage.py runserver
   ```

## Project structure

- `alx_travel_app/` — Django project settings and config
- `listings/` — App with models, serializers, views, tests, and management commands
- `requirements.txt` — Python dependencies

## Contributing

1. Create a branch:
   ```powershell
   git checkout -b feat/update-readme
   ```
2. Make changes, commit, push, then open a pull request.

## License

See `LICENSE` in the repository root.

"""
# ALX Travel App - Phase 0: Database Modeling and Data Seeding

This project is a Django application for managing travel listings, bookings, and reviews.  
It demonstrates **database modeling**, **API serialization**, and **data seeding**.

---

## Table of Contents

- [Project Setup](#project-setup)
- [Models](#models)
- [Serializers](#serializers)
- [Database Seeding](#database-seeding)
- [Usage](#usage)

---

## Project Setup

1. Clone or duplicate the project:

```bash
cp -r alx_travel_app alx_travel_app_0x00
cd alx_travel_app_0x00

Lets do this