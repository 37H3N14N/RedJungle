from sqlalchemy import create_engine, Integer, String, Boolean, ForeignKey, Table, Column, Float
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

Hotel_Config_Association = Table (
    "hotel_config_association",
    Base.metadata,
    Column('hotel_id', ForeignKey('hotel_object.hotel_id'), primary_key=True),
    Column('config_id', ForeignKey('hotel_configuration_object.config_id'), primary_key=True)
)

Hotel_Service_Association = Table (
    'hotel_service_association',
    Base.metadata,
    Column('hotel_id', ForeignKey('hotel_object.hotel_id'), primary_key=True),
    Column('service_id', ForeignKey('hotel_service_object.service_id'), primary_key=True),
)

################################ TABLES INITIALIZATION ###################################


class Hotel_Object(Base):
    __tablename__ = 'hotel_object'

    hotel_id: Mapped[str] = mapped_column(String, primary_key=True)
    hotel_name: Mapped[str] = mapped_column(String)
    tenant_id: Mapped[str] = mapped_column(String)
    admin_user_id: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    contact_number: Mapped[int] = mapped_column(Integer)

    configs: Mapped[List['Hotel_Configuration_Object']] = relationship(
        secondary=Hotel_Config_Association,
        back_populates='hotels'
        )

    services: Mapped[List['Hotel_Service_Object']] = relationship(
        secondary=Hotel_Service_Association,
        back_populates='hotels'
        )


class Hotel_Service_Object(Base):
    __tablename__ = 'hotel_service_object'

    service_id: Mapped[str] = mapped_column(String, primary_key=True)
    service_name: Mapped[str] = mapped_column(String)
    service_description: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Float)
    operation_days: Mapped[str] = mapped_column(String)
    operation_timelines: Mapped[str] = mapped_column(String)
    max_people: Mapped[str] = mapped_column(String)
    
    booking_service_wormhole: Mapped['Booking_Service_Object'] = relationship(back_populates='booking_service_wormhole')

    hotels: Mapped[List['Hotel_Object']] = relationship(
        secondary=Hotel_Service_Association,
        back_populates='services'
        )

class Booking_Service_Object(Base):
    __tablename__ = 'booking_service_object'

    booking_service_id: Mapped[str] = mapped_column(String, primary_key=True)
    service_id: Mapped[str] = mapped_column(ForeignKey('hotel_service_object.service_id'))
    guest_id: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)

    booking_service_wormhole: Mapped['Hotel_Service_Object'] = relationship(back_populates='booking_service_wormhole')


class Hotel_Configuration_Object(Base):
    __tablename__ = 'hotel_configuration_object'

    config_id: Mapped[str] = mapped_column(String, primary_key=True)
    config_name: Mapped[str] = mapped_column(String)
    config_value: Mapped[str] = mapped_column(String)
    last_updated_timestamp: Mapped[str] = mapped_column(String)
    last_updated_admin_user_id: Mapped[str] = mapped_column(String)


    hotels: Mapped[List['Hotel_Object']] = relationship(
        secondary=Hotel_Config_Association,
        back_populates='configs'
        )


Base.metadata.create_all(engine)

###########################################################################










