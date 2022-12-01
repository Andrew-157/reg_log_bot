from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Date, String

Base = declarative_base()


class Account(Base):

    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(26), nullable=False)
    email = Column(String(35), nullable=False)
    phone = Column(String(14), nullable=False)
