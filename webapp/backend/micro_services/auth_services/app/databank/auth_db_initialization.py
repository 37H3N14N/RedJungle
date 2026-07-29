from sqlalchemy import create_engine, Integer, String, Boolean, ForeignKey, Table, Column
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped
from sqlalchemy.orm import mapped_column, sessionmaker
from app.configs.config_general import DATABASE_CONFIG
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

Credential_Reset_Token_Association = Table (
    'credential_reset_token_association',
    Base.metadata,
    Column('credential_id', ForeignKey('credential_object.credential_id'), primary_key=True),
    Column('password_reset_token_id', ForeignKey('password_reset_token_object.token_id'), primary_key=True)
)

########################## TABLE INITIALIZATION ###########################

class Credential_Object(Base):
    __tablename__ = 'credential_object'

    credential_id: Mapped[str] = mapped_column(String, primary_key=True)
    user_id: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    hashed_password: Mapped[str] = mapped_column(String)
    salt: Mapped[str] = mapped_column(String)
    mfa_secret: Mapped[str] = mapped_column(String)
    last_login_at: Mapped[str] = mapped_column(String)
    failed_login_attempts: Mapped[int] = mapped_column(Integer)

    credential_session_wormhole: Mapped['Session_Object'] = relationship(back_populates='session_credential_wormhole')

    reset_tokens: Mapped[List['Password_Reset_Token_Object']] = relationship(
        secondary= Credential_Reset_Token_Association,
        back_populates= 'credentials'
    )


class Session_Object(Base):
    __tablename__ = 'session_object'

    session_id: Mapped[str] = mapped_column(String, primary_key=True)
    token_hash: Mapped[str] = mapped_column(String)
    expires_at: Mapped[str] = mapped_column(String)
    ip_address: Mapped[str] = mapped_column(String)

    credential_id: Mapped[str] = mapped_column(ForeignKey('credential_object.credential_id'))

    session_credential_wormhole: Mapped['Credential_Object'] = relationship(back_populates='credential_session_wormhole')



class Password_Reset_Token_Object(Base):
    __tablename__ = 'password_reset_token_object' 

    token_id: Mapped[str] = mapped_column(String, primary_key=True)
    token: Mapped[str] = mapped_column(String, unique=True)
    expires_at: Mapped[str] = mapped_column(String)
    is_used: Mapped[bool] = mapped_column(Boolean)

    credentials: Mapped[List['Credential_Object']] = relationship(
        secondary= Credential_Reset_Token_Association,
        back_populates= 'reset_tokens'
    )



Base.metadata.create_all(engine)

#############################################################################





