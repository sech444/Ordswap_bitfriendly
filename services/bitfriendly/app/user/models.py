from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from app.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    last_login = Column(DateTime, server_default=func.now(), onupdate=func.now())

    mnemonics = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "mnemonic"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    mnemonic_1 = Column(String,  index=True)
    mnemonic_2 = Column(String,  index=True)
    mnemonic_3 = Column(String,  index=True)
    mnemonic_4 = Column(String,  index=True)
    mnemonic_5 = Column(String,  index=True)
    mnemonic_6 = Column(String,  index=True)
    mnemonic_7 = Column(String,  index=True)
    mnemonic_8 = Column(String,  index=True)
    mnemonic_9 = Column(String,  index=True)
    mnemonic_10 = Column(String,  index=True)
    mnemonic_11 = Column(String,  index=True)
    mnemonic_12 = Column(String,  index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="mnemonics")



