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

Review_Picture_Association = Table (
    'review_picture_association',
    Base.metadata,
    Column('review_id', ForeignKey('review_object.review_id'), primary_key=True),
    Column('picture_id', ForeignKey('picture_object.picture_id'), primary_key=True)
)

Review_Message_Association = Table (
    'review_message_association',
    Base.metadata,
    Column('review_id', ForeignKey('review_object.review_id'), primary_key=True),
    Column('message_id', ForeignKey('message_object.message_id'), primary_key=True)
)

########################## TABLE INITIALIZATION ###########################

class Review_Object(Base):
    __tablename__ = 'review_object'

    review_id: Mapped[str] = mapped_column(String, primary_key=True)
    user_id: Mapped[str] = mapped_column(String)
    tenant_id: Mapped[str] = mapped_column(String)
    date_created: Mapped[str] = mapped_column(String)
    date_updated: Mapped[str] = mapped_column(String)

    pictures: Mapped[List['Picture_Object']] = relationship(
        secondary= Review_Picture_Association,
        back_populates= 'reviews'
    )

    messages: Mapped[List['Message_Object']] = relationship(
        secondary= Review_Message_Association,
        back_populates= 'reviews'
    )


class Picture_Object(Base):
    __tablename__ = 'picture_object'

    picture_id: Mapped[str] = mapped_column(String, primary_key=True)
    picture_url: Mapped[str] = mapped_column(String)
    date_created: Mapped[str] = mapped_column(String)

    reviews: Mapped[List['Review_Object']] = relationship(
        secondary= Review_Picture_Association,
        back_populates= 'pictures'
    )


class Message_Object(Base):
    __tablename__ = 'message_object'

    message_id: Mapped[str] = mapped_column(String, primary_key=True)
    message_text: Mapped[str] = mapped_column(String)
    date_created: Mapped[str] = mapped_column(String)
    date_updated: Mapped[str] = mapped_column(String)

    reviews: Mapped[List['Review_Object']] = relationship(
        secondary= Review_Message_Association,
        back_populates= 'messages'
    )



Base.metadata.create_all(engine)

#############################################################################







