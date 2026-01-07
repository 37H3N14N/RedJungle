from sqlalchemy import create_engine, Integer,BigInteger, String, Float, Boolean, ForeignKey, Table, Column
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

Bank_Account_Association = Table (
    'bank_account_association',
    Base.metadata,
    Column('bank_id', ForeignKey('bank_object.bank_id'), primary_key=True),
    Column('account_id', ForeignKey('account_object.account_id'), primary_key=True)
)

Customer_Account_Association = Table (
    'customer_account_association',
    Base.metadata,
    Column('customer_id', ForeignKey('customer_object.customer_id'), primary_key=True),
    Column('account_id', ForeignKey('account_object.account_id'), primary_key=True)
)

########################## TABLE INITIALIZATION ###########################

class Transaction_Object(Base):
    __tablename__ = 'transaction_object'

    transaction_id: Mapped[str]= mapped_column(String, primary_key=True)
    user_id: Mapped[str]= mapped_column(String)
    tenant_id: Mapped[str]= mapped_column(String)
    card_number: Mapped[str] = mapped_column(BigInteger)
    amount: Mapped[float]= mapped_column(Float)
    created_at: Mapped[str]= mapped_column(String)


class Bank_Object(Base):
    __tablename__ = 'bank_object'

    bank_id: Mapped[str] = mapped_column(String, primary_key=True)
    bank_name: Mapped[str] = mapped_column(String)

    accounts: Mapped[List['Account_Object']] = relationship(
        secondary= Bank_Account_Association,
        back_populates= 'banks'
    )


class Account_Object(Base):
    __tablename__ = 'account_object'

    account_id: Mapped[str] = mapped_column(String, primary_key=True)
    bank_id: Mapped[str] = mapped_column(String)
    card_number: Mapped[str] = mapped_column(BigInteger, unique=True)
    account_balance: Mapped[str] = mapped_column(Float)
    updated_at: Mapped[str] = mapped_column(String)

    banks: Mapped[List['Bank_Object']] = relationship(
        secondary= Bank_Account_Association,
        back_populates= 'accounts'
    )

    customers: Mapped[List['Customer_Object']] = relationship(
        secondary= Customer_Account_Association,
        back_populates= 'accounts'
    )


class Customer_Object(Base):
    __tablename__ = 'customer_object'

    customer_id: Mapped[str] = mapped_column(String, primary_key=True)
    user_id: Mapped[str] = mapped_column(String)

    accounts: Mapped[List['Account_Object']] = relationship(
        secondary= Customer_Account_Association,
        back_populates= 'customers'
    )


Base.metadata.create_all(engine)

#############################################################################








