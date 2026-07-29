from sqlalchemy import create_engine, Integer, String, ForeignKey, Column, Table
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped
from sqlalchemy.orm import mapped_column, sessionmaker
from configs.config_general import DATABASE_CONFIG
from typing import List


###############################################################################

db_username = DATABASE_CONFIG['db_username']
db_passcode = DATABASE_CONFIG['db_passcode']
db_url = DATABASE_CONFIG['db_url']
db_port = DATABASE_CONFIG['db_port']
db_name = DATABASE_CONFIG['db_name']

###############################################################################

DATABASE_URL = f"postgresql+psycopg2://{db_username}:{db_passcode}@{db_url}:{db_port}/{db_name}"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def get_session():
    session = Session()
    return session

###############################################################################
class Base(DeclarativeBase):
    pass

########################  INTERMEDIATE TABLES  #################################

User_Profile_Association = Table (
    'user_profile_association',
    Base.metadata,
    Column('user_id', ForeignKey('user_object.user_id'), primary_key=True),
    Column('profile_id', ForeignKey('profile_object.profile_id'), primary_key=True)
)

########################## TABLE INITIALIZATION ###########################

class User_Object(Base):
    __tablename__ = 'user_object'

    user_id: Mapped[str] = mapped_column(String, primary_key=True)
    tenant_id: Mapped[str] = mapped_column(String)
    role_id: Mapped[str]= mapped_column(String)
    updated_at: Mapped[str] = mapped_column(String)
    created_at: Mapped[str] = mapped_column(String)

    profiles: Mapped[List['Profile_Object']] = relationship(
        secondary= User_Profile_Association,
        back_populates= 'users'
    )

class Profile_Object(Base):
    __tablename__ = 'profile_object'

    profile_id: Mapped[str] = mapped_column(String, primary_key=True)
    profile_picture_url: Mapped[str] = mapped_column(String)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)

    users: Mapped[List['User_Object']] = relationship(
        secondary= User_Profile_Association,
        back_populates= 'profiles'
    )



Base.metadata.create_all(engine)

#############################################################################









