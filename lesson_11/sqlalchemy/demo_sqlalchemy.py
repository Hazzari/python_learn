from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///example.db")
Base = declarative_base(bind=engine)


class User:
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    fullname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.username, self.fullname, self.nickname)


Base.metadata.create_all(engine)
