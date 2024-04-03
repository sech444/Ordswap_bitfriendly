from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class UserLoginResponse(BaseModel):
    access_token: str
    token_type: str
    mnemonic_item: List[List[str]] # Adjust the type accordingly
    taproot_address: str
    private_key: str

class UserLogin(BaseModel):
    password: Optional[str] = None

class UserResponse(BaseModel):
    mnemonic: List[str]
    private_key: str
    addresses: str


class PasswordInput(BaseModel):
    password: str
    confirm_password: str

    
class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(BaseModel):
    Optional[int]
    mnemonic_1: str
    mnemonic_2: str
    mnemonic_3: str
    mnemonic_4: str
    mnemonic_5: str
    mnemonic_6: str
    mnemonic_7: str
    mnemonic_8: str
    mnemonic_9: str
    mnemonic_10: str
    mnemonic_11: str
    mnemonic_12: str

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    password: str

class UserInDB(BaseModel):
    id: int
    hashed_password: str


class User(UserCreate):
    id: int
    is_active: bool
    items: List[Item] = []
    last_login: Optional[datetime]

    class Config:
        from_attributes = True