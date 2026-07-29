from sqlalchemy import create_engine, Integer, Boolean, ForeignKey, Table, String, Float, Column
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

Room_Amenity_Association = Table (
    'room_amenity_association',
    Base.metadata,
    Column('room_id', ForeignKey('room_object.room_id'), primary_key=True),
    Column('amenity_id', ForeignKey('amenity_object.amenity_id'), primary_key=True)
)

Amenity_Picture_Association = Table (
    'amenity_picture_association',
    Base.metadata,
    Column('amenity_id', ForeignKey('amenity_object.amenity_id'), primary_key=True),
    Column('picture_id', ForeignKey('picture_object.picture_id'), primary_key=True),
)

########################## TABLE INITIALIZATION ###########################

class Room_Object(Base):
    __tablename__ = 'room_object'

    room_id: Mapped[str] = mapped_column(String, primary_key=True)
    room_no: Mapped[int] = mapped_column(Integer)
    room_name: Mapped[int] = mapped_column(String)
    hotel_id: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Float)

    amenities: Mapped[List['Amenity_Object']] = relationship(
        secondary= Room_Amenity_Association,
        back_populates= 'rooms'
    )


class Amenity_Object(Base):
    __tablename__ = 'amenity_object'

    amenity_id: Mapped[str] = mapped_column(String, primary_key=True)
    amenity_name: Mapped[str] = mapped_column(String)
    amenity_description: Mapped[str] = mapped_column(String)
    max_occupancy: Mapped[int] = mapped_column(Integer)
    
    pictures: Mapped[List['Picture_Object']] = relationship(
        secondary= Amenity_Picture_Association,
        back_populates= 'amenities'
    )

    rooms: Mapped[List['Room_Object']] = relationship(
        secondary= Room_Amenity_Association,
        back_populates= 'amenities'
    )


class Picture_Object(Base):
    __tablename__ = 'picture_object'

    picture_id: Mapped[str] = mapped_column(String, primary_key=True)
    picture_url: Mapped[str] = mapped_column(String)
    date_created: Mapped[str] = mapped_column(String)

    amenities: Mapped[List['Amenity_Object']] = relationship(
        secondary= Amenity_Picture_Association,
        back_populates= 'pictures'
    )



Base.metadata.create_all(engine)

#############################################################################









