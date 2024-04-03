from sqlalchemy.orm import Session
from sqlalchemy import and_
from . import  schemas, security

from user import models
from datetime import datetime



def authenticate_user(db: Session, password: str):
    # Query all users with non-null hashed passwords
    users_with_passwords = db.query(models.User).filter(models.User.hashed_password.isnot(None)).all()

    # Check each user for a match with the entered password
    for user in users_with_passwords:
        if security.verify_password(password, user.hashed_password):
            return user

    return None


def passwordInput(db: Session, password: str, confirm_password: str):
    password: str
    confirm_password: str


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_pass(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()



def update_last_login(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    user.last_login = datetime.utcnow()
    db.commit()
    db.refresh(user)
    return user




def create_user(db: Session, password: str, user: schemas.UserCreate, mnemonic: schemas.Item):
    # Check the strength of the password
    password_strength = security.check_password_strength(password)
    print(f"Password strength: {password_strength}")
    
    # Hash the password
    hashed_password = security.get_password_hash(password)
    

    # Create the user with the hashed password
    db_user = models.User(hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    mnemonic_dict = mnemonic.dict()
    if 'owner_id' in mnemonic_dict:
        del mnemonic_dict['owner_id']
    if 'description' in mnemonic_dict:
        del mnemonic_dict['description']
    if 'title' in mnemonic_dict:
        del mnemonic_dict['title']

    db_mnemonic = models.Item(owner_id=db_user.id, **mnemonic_dict)

    db.add(db_mnemonic)
    db.commit()
    db.refresh(db_mnemonic)

    return db_user


def update_mnemonic_owner_id(db: Session, mnemonic_id: int, owner_id: int):
    # Update the owner_id for the provided mnemonic_item
    db_mnemonic = db.query(models.Item).filter(models.Item.id == mnemonic_id).first()

    if db_mnemonic:
        db_mnemonic.owner_id = owner_id
        db.commit()
        db.refresh(db_mnemonic)

    return db_mnemonic



def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def all_mnemonic_words_exist(db, mnemonic):
    if isinstance(mnemonic, list):
        # If mnemonic is a list, join its elements into a string
        mnemonic_string = " ".join(mnemonic)
    else:
        # If mnemonic is already a string, use it directly
        mnemonic_string = mnemonic

    # Create a list of conditions for each word in the mnemonic
    conditions = [
        getattr(mnemonic, f"mnemonic_{i + 1}") == word for i, word in enumerate(mnemonic_string.split())
    ]

    # Use 'and_' to combine the conditions with AND
    condition_and = and_(*conditions)

    # Query the database to check if all mnemonic words exist
    return db.query(mnemonic).filter(condition_and).first() is not None



from mnemonic import Mnemonic

def is_valid_mnemonic(mnemonic_words):
    mnemo = Mnemonic("english")  # You can specify the language of the mnemonic

    # Check if the mnemonic is valid
    return mnemo.check(mnemonic_words)
