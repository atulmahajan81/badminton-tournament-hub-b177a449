import datetime
import random
import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Tournament, Match, Score, Notification, Registration, Base

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/badminton"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Create users
users = [
    User(id=uuid.uuid4(), email="admin@example.com", password_hash="hash1", role="admin"),
    User(id=uuid.uuid4(), email="player1@example.com", password_hash="hash2", role="player"),
    User(id=uuid.uuid4(), email="player2@example.com", password_hash="hash3", role="player")
]
session.add_all(users)
session.commit()

# Create tournaments
tournaments = [
    Tournament(id=uuid.uuid4(), name="Spring Open", location="New York", date=datetime.date.today(), rules="Standard Rules"),
    Tournament(id=uuid.uuid4(), name="Summer Open", location="Los Angeles", date=datetime.date.today() + datetime.timedelta(days=10), rules="Standard Rules")
]
session.add_all(tournaments)
session.commit()

# Create matches
matches = [
    Match(id=uuid.uuid4(), tournament_id=tournaments[0].id, player1_id=users[1].id, player2_id=users[2].id, umpire_id=users[0].id, scheduled_time=datetime.datetime.now() + datetime.timedelta(days=1)),
    Match(id=uuid.uuid4(), tournament_id=tournaments[1].id, player1_id=users[1].id, player2_id=users[2].id, umpire_id=users[0].id, scheduled_time=datetime.datetime.now() + datetime.timedelta(days=2))
]
session.add_all(matches)
session.commit()

# Create scores
scores = [
    Score(id=uuid.uuid4(), match_id=matches[0].id, player1_score=21, player2_score=15),
    Score(id=uuid.uuid4(), match_id=matches[1].id, player1_score=18, player2_score=21)
]
session.add_all(scores)
session.commit()

# Create notifications
notifications = [
    Notification(id=uuid.uuid4(), user_id=users[1].id, message="Your match is scheduled for tomorrow."),
    Notification(id=uuid.uuid4(), user_id=users[2].id, message="Your match is scheduled for tomorrow.")
]
session.add_all(notifications)
session.commit()

# Create registrations
registrations = [
    Registration(id=uuid.uuid4(), user_id=users[1].id, tournament_id=tournaments[0].id),
    Registration(id=uuid.uuid4(), user_id=users[2].id, tournament_id=tournaments[1].id)
]
session.add_all(registrations)
session.commit()

session.close()