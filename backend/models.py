from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, default="AI大神")
    type = Column(String)
    summary = Column(Text)
    raw_worldview = Column(Text)

class Chapter(Base):
    __tablename__ = "chapters"
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    order = Column(Integer)
    title = Column(String)
    summary = Column(Text)
    content = Column(Text, default="")
    words = Column(Integer, default=0)
