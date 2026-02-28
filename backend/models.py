from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)



class Questionnaire(Base):
    __tablename__ = "questionnaires"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    content = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User")

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    questionnaire_id = Column(Integer, ForeignKey("questionnaires.id"))

class ReferenceDocument(Base):
    __tablename__ = "reference_documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    content = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))

class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    citation = Column(String)
    question_id = Column(Integer, ForeignKey("questions.id"))