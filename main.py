from database import Base, engine, SessionLocal
from crud import create_user, get_users, get_user_by_name, get_users_with_messages
from models import User, Message

Base.metadata.create_all(bind=engine)

db = SessionLocal()
user1 = User(username="aandrii", email="andrii2@example.com")
user2 = User(username="aaria", email="maria2@example.com")
db.add_all([user1, user2])
db.commit()

msg1 = Message(user=user1, content="Hello!")
msg2 = Message(user=user1, content="How are you?")
msg3 = Message(user=user2, content="SQLAlchemy")
db.add_all([msg1, msg2, msg3])
db.commit()


users = get_users_with_messages(db)
for user in users:
    print(user.username, [m.content for m in user.messages])
db.close()