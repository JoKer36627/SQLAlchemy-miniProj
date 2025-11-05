from models import User, Message
from database import SessionLocal
from sqlalchemy.orm import Session, selectinload
from sqlalchemy.dialects.postgresql import insert


def create_user(username: str, email: str):
    db = SessionLocal()
    new_user = User(username=username, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()
    return new_user

def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users

def get_user_by_name(username: str):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    db.close()
    return user


def get_users_with_messages(session: Session):
    return session.query(User).options(selectinload(User.messages)).all()


def create_user_and_message(session: Session, username, email, message_content):
    try:
        with session.begin():
            user = User(username=username, email=email)
            session.add(user)
            msg = Message(user=user, content=message_content)
            session.add(msg)
    except Exception as e:
        print("Transaction failed:", e)

from sqlalchemy.dialects.postgresql import insert

def upsert_user(session, username, email):
    stmt = insert(User).values(username=username, email=email)
    stmt = stmt.on_conflict_do_update(
        index_elements=[User.username],
        set_={'email': stmt.excluded.email}
    )
    session.execute(stmt)
    session.commit()



