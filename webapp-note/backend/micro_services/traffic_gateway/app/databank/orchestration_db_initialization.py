from sqlalchemy import create_engine, Integer, String, Boolean, ForeignKey, Table, Column
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

Workflow_Step_Association = Table (
    "workflow_step_association",
    Base.metadata,
    Column('workflow_id', ForeignKey('workflow_object.workflow_id'), primary_key=True),
    Column('step_id', ForeignKey('step_object.step_id'), primary_key=True)
)

Workflow_Sub_Workflow_Association = Table (
    "workflow_sub_workflow_association",
    Base.metadata,
    Column('workflow_id', ForeignKey('workflow_object.workflow_id'), primary_key=True),
    Column('sub_workflow_id', ForeignKey('sub_workflow_object.sub_workflow_id'), primary_key=True)
)

########################## TABLE INITIALIZATION ###########################

class Workflow_Object(Base):
    __tablename__ = 'workflow_object'

    workflow_id: Mapped[str] = mapped_column(String, primary_key=True)
    workflow_name: Mapped[str] = mapped_column(String)

    workflow_progress_wormhole: Mapped['Progress_Object'] = relationship(back_populates='progress_workflow_wormhole')
    workflow_sub_workflow_wormhole: Mapped['Sub_Workflow_Object'] = relationship(back_populates='sub_workflow_workflow_wormhole')

    steps: Mapped[List['Step_Object']] = relationship(
        secondary=Workflow_Step_Association,
        back_populates='workflows'
        )

    sub_workflows: Mapped[List['Sub_Workflow_Object']] = relationship(
        secondary=Workflow_Sub_Workflow_Association,
        back_populates='workflows'
        )


class Step_Object(Base):
    __tablename__ = 'step_object'

    step_id: Mapped[str] = mapped_column(String, primary_key=True)
    relative_uri: Mapped[str] = mapped_column(String)
    request_type: Mapped[str] = mapped_column(String)
    execution_order: Mapped[int] = mapped_column(Integer)

    service_id: Mapped[str] = mapped_column(ForeignKey('service_object.service_id'))
    step_service_wormhole: Mapped['Service_Object'] = relationship(back_populates='service_step_wormhole')

    workflows: Mapped[List['Workflow_Object']] = relationship(
        secondary=Workflow_Step_Association,
        back_populates='steps'
        )


class Service_Object(Base):
    __tablename__ = 'service_object'

    service_id: Mapped[str] = mapped_column(String, primary_key=True)
    service_name: Mapped[str] = mapped_column(String)
    endpoint: Mapped[str] = mapped_column(String)

    service_step_wormhole: Mapped['Step_Object'] = relationship(back_populates='step_service_wormhole')


class Sub_Workflow_Object(Base):
    __tablename__ = 'sub_workflow_object'

    sub_workflow_id: Mapped[str] = mapped_column(String, primary_key=True)
    execution_order: Mapped[int] = mapped_column(Integer)
    
    assistance_workflow_id: Mapped[str] = mapped_column(ForeignKey('workflow_object.workflow_id'))
    sub_workflow_workflow_wormhole: Mapped['Workflow_Object'] = relationship(back_populates='workflow_sub_workflow_wormhole')

    workflows: Mapped[List['Workflow_Object']] = relationship(
        secondary=Workflow_Sub_Workflow_Association,
        back_populates='sub_workflows'
        )


class Progress_Object(Base):
    __tablename__ = 'progress_object'

    progress_id: Mapped[str] = mapped_column(String, primary_key=True)
    workflow_id: Mapped[str] = mapped_column(ForeignKey('workflow_object.workflow_id'))
    current_service_id: Mapped[str] = mapped_column(String)
    progress_status: Mapped[str] = mapped_column(String)
    complete_status: Mapped[str] = mapped_column(String)

    progress_workflow_wormhole: Mapped['Workflow_Object'] = relationship(back_populates='workflow_progress_wormhole')



Base.metadata.create_all(engine)

##################################################################################################







