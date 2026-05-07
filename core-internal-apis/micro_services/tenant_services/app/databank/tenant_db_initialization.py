from sqlalchemy import create_engine, Integer, String, Boolean, ForeignKey, Table, Float, Column
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

Tenant_Billing_Association = Table (
    'tenant_billing_association',
    Base.metadata,
    Column('tenant_id', ForeignKey('tenant_object.tenant_id'), primary_key=True),
    Column('billing_id', ForeignKey('billing_object.billing_id'), primary_key=True)
)

########################## TABLE INITIALIZATION ###########################

class Tenant_Object(Base):
    __tablename__ = 'tenant_object'

    tenant_id: Mapped[str] = mapped_column(String, primary_key=True)
    tenant_name: Mapped[str] = mapped_column(String)
    super_admin_user_id: Mapped[str] = mapped_column(String)
    subscription_plan: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    created_at: Mapped[str] = mapped_column(String)

    billings: Mapped[List['Billing_Object']] = relationship(
        secondary= Tenant_Billing_Association,
        back_populates= 'tenants'
    )


class Billing_Object(Base):
    __tablename__ = 'billing_object'

    billing_id: Mapped[str] = mapped_column(String, primary_key=True)
    next_payment_after_days: Mapped[int] = mapped_column(Integer)
    total_amount: Mapped[float] = mapped_column(Float)
    payment_transaction_id: Mapped[str] = mapped_column(String, unique=True)
    created_at: Mapped[str] = mapped_column(String)

    tenants: Mapped[List['Tenant_Object']] = relationship(
        secondary= Tenant_Billing_Association,
        back_populates= 'billings'
    )



Base.metadata.create_all(engine)

#############################################################################









