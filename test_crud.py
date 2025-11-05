import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User
from crud import get_users

@pytest.fixture()
def test_db():
    engine = create_engine("sqlite:///:memory:", echo=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session  # віддаємо сесію у тест
    finally:
        session.close()

def test_create_user(test_db):
    user = User(username="testuser", email="test@example.com")
    test_db.add(user)
    test_db.commit()

    users = get_users(test_db)
    assert len(users) == 1
    assert users[0].username == "testuser"