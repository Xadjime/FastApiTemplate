# FastAPI Todo App

A simple FastAPI application to manage todos with SQLModel and PostgreSQL.

## Prerequisites

- Python 3.10+
- PostgreSQL

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Xadjime/FastApiTemplate.git
   cd FastApiTemplate
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment:**
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   Update the `DATABASE_URL` in `.env` with your PostgreSQL credentials.

5. **Run the application:**
   ```bash
   uvicorn main:app --reload
   ```
