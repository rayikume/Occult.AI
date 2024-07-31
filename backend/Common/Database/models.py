from sqlalchemy import Column, Float, Integer, String, DateTime, ForeignKey, Text, Numeric
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True, index=True)
    password_hash = Column(String)
    role = Column(String)

    preferences = relationship("UserPreference", back_populates="user")
    activities = relationship("UserActivity", back_populates="user")

class UserPreference(Base):
    __tablename__ = "userpreferences"

    preference_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, ForeignKey("users.username"))
    preference_type = Column(String)
    preference_value = Column(String)

    user = relationship("User", back_populates="preferences")

class UserActivity(Base):
    __tablename__ = "user_activities"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, ForeignKey("users.username"))
    activity = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="activities")

class Author(Base):
    __tablename__ = "authors"

    author_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(500))
    biography = Column(Text)

class Book(Base):
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500))
    subtitle = Column(String(500))
    author = Column(String(500))
    author_id = Column(Integer, index=True)
    genre = Column(String(500))
    thumbnail = Column(Text)
    description = Column(Text)
    published_year = Column(String(30))
    average_rating = Column(String(30))