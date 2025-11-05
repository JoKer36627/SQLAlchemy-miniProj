# SQLAlchemy Mini Project

This mini-project demonstrates basic usage of **SQLAlchemy**, **Alembic**, and **SQLite**.  
The goal is to learn how to create models, perform CRUD operations, work with table relationships, and manage database migrations.

---

## 📦 Technologies & Libraries
- **Python 3.14**
- **SQLAlchemy** – ORM for database operations.
- **Alembic** – for database migrations.
- **SQLite** – lightweight database for local development.
- **pytest** – for testing CRUD operations and functionality.

---

## 🗂 Project Structure

SQLAlchemy-miniProj/
├─ alembic/               # Alembic configurations and migration scripts
├─ backend/               # (optional backend folder)
├─ models.py              # database models
├─ database.py            # database connection and SQLAlchemy session
├─ crud.py                # CRUD functions for User and Message
├─ test_crud.py           # tests for CRUD operations
├─ users.db               # SQLite database
├─ alembic.ini            # Alembic configuration
└─ README.md              # this file

---

## 🔧 Environment Setup

1. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate      # Windows

	2.	Install required packages:

pip install -r requirements.txt
# or individually
pip install sqlalchemy alembic pytest


⸻

⚡ Database Models

User
	•	id – unique user ID
	•	username – user name
	•	email – user email
	•	messages – one-to-many relationship with Message

Message
	•	id – unique message ID
	•	user_id – foreign key to User.id
	•	content – message text
	•	user – relationship to User

Relationship:
User.messages <-> Message.user via relationship and back_populates.

⸻

🛠 CRUD Functions
	•	create_user(username, email) – create a new user
	•	get_users() – fetch all users
	•	get_user_by_name(username) – find a user by username
	•	create_user_and_message(session, username, email, message_content) – transaction: create user and message
	•	upsert_user(session, username, email) – insert or update a user

⸻

🏗 Alembic Migrations
	1.	Initialize Alembic (if not already done):

alembic init alembic

	2.	Create a new migration:

alembic revision --autogenerate -m "create users and messages"

	3.	Apply migrations:

alembic upgrade head


⸻

✅ Testing
	•	Uses pytest.
	•	Run tests with:

pytest -v

	•	Tests verify CRUD functionality and database relationships.

⸻

🚀 Usage
	1.	Activate your virtual environment.
	2.	Apply migrations with Alembic.
	3.	Use functions from crud.py to interact with the database.

⸻

📝 Notes
	•	SQLAlchemy ORM allows using Python code instead of raw SQL to create, read, update, and delete records.
	•	Alembic tracks table structure changes and applies them to the database.
	•	pytest automates verification of CRUD logic and database integrity.

⸻

🔗 Resources
	•	SQLAlchemy Documentation￼
	•	Alembic Documentation￼
	•	pytest Documentation￼
