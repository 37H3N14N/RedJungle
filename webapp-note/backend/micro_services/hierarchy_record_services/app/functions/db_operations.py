from sqlalchemy import update, delete
import uuid
from datetime import datetime 

from databank.admin_db_initialization import get_session
from databank.admin_db_initialization import Hotel_Object
from databank.admin_db_initialization import Hotel_Service_Object
from databank.admin_db_initialization import Hotel_Configuration_Object
from databank.admin_db_initialization import Booking_Service_Object


###################################################################
session = get_session()

###################################################################

def get_uuid4():
    random_uuid = uuid.uuid4()
    return random_uuid

def get_timestamp():
   now = datetime.now()
   refined_structure = now.strftime("%Y-%m-%d %H:%M:%S")
   return refined_structure

###################################################################

def create_hotel(hotel_name_input,tenant_id_input,location_input,contact_number_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    hotel_item = Hotel_Object(
        hotel_id= constant_uuid[0], 
        hotel_name= hotel_name_input,
        tenant_id= tenant_id_input,
        location= location_input,
        contact_number= contact_number_input
        )

    response_data.append({'invoice_id': f'{constant_uuid[0]}'})

    session.add(hotel_item)
    session.commit()
    session.close()

    return response_data

############################################################################

def create_service(service_name_input,service_description_input,price_input,operation_day_input,operation_day_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    service_item = Hotel_Service_Object(
        service_id= constant_uuid[0], 
        service_name= service_name_input,
        service_description= service_description_input,
        price= price_input,
        operation_day= operation_day_input,
        operation_time= operation_time_input,
        )

    response_data.append({'invoice_id': f'{constant_uuid[0]}'})

    session.add(service_item)
    session.commit()
    session.close()

    return response_data

############################################################################

def create_booking_service(guest_id_input,service_id_input, status_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    booking_service_item = Booking_Service_Object(
        booking_service_id = constant_uuid[0],
        guest_id= guest_id_input,
        service_id= service_id_input,
        status= status_input,
        )

    response_data.append({'invoice_id': f'{constant_uuid[0]}'})

    session.add(booking_service_item)
    session.commit()
    session.close()

    return response_data

###################################################################

def create_hotel_config(config_name_input,config_value,last_updated_admin_user_id):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    config_item = Hotel_Configuration_Object(
        config_id= constant_uuid[0], 
        config_name= config_name_input,
        config_value= config_value_input,
        last_updated_admin_user_id= last_updated_admin_user_id_input,
        last_updated_timestamp= get_timestamp()
        )

    response_data.append({'invoice_id': f'{constant_uuid[0]}'})

    session.add(config_item)
    session.commit()
    session.close()

    return response_data

###################################################################

def create_link_btwn_hotel_config(db_session,config_column_name,config_row_identifier,hotel_column_name,hotel_row_identifier):

    target_hotel = read_data(db_session,'hotel',hotel_column_name,hotel_row_identifier)
    target_config = read_data(db_session,'config',config_column_name,config_row_identifier)

    target_hotel.configs.append(target_config)

    db_session.commit()
    db_session.close()
    return


def create_link_btwn_hotel_service(db_session,service_column_name,service_row_identifier,hotel_column_name,hotel_row_identifier):

    target_hotel = read_data(db_session,'hotel',hotel_column_name,hotel_row_identifier)
    target_service = read_data(db_session,'service',service_column_name,service_row_identifier)

    target_hotel.services.append(target_service)

    db_session.commit()
    db_session.close()
    return

############################################################################

def read_data(db_session,target_model_class,column_name,row_identifier):

    if target_model_class == 'hotel':
        column = getattr(Hotel_Object,column_name)
        target_item = db_session.query(Hotel_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'config':
        column = getattr(Hotel_Configuration_Object,column_name)
        target_item = db_session.query(Hotel_Configuration_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'service':
        column = getattr(Hotel_Service_Object,column_name)
        target_item = db_session.query(Hotel_Service_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'booking_service':
        column = getattr(Booking_Service_Object,column_name)
        target_item = db_session.query(Booking_Service_Object).filter(column == f'{row_identifier}').first()
        return target_item

############################################################################

def update_data(db_session,target_model_class,identifying_column_name,identifying_row_entity,target_column_to_change,new_value_of_cell):

    if target_model_class == 'hotel':

        identify_column = getattr(Hotel_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Hotel_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


    if target_model_class == 'service':

        identify_column = getattr(Hotel_Service_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Hotel_Service_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


    if target_model_class == 'config':

        identify_column = getattr(Hotel_Configuration_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Hotel_Configuration_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


############################################################################

def delete_data(db_session,main_id,target_model_class):

    if target_model_class == 'hotel':
        target_item = db_session.query(Hotel_Object).filter(Hotel_Object.hotel_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 


    if target_model_class == 'service':
        target_item = db_session.query(Hotel_Service_Object).filter(Hotel_Service_Object.service_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 
        

    if target_model_class == 'booking_service':
        target_item = db_session.query(Booking_Service_Object).filter(Booking_Service_Object.booking_service_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 


    if target_model_class == 'config':
        target_item = db_session.query(Hotel_Configuration_Object).filter(Hotel_Configuration_Object.config_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 

############################################################################

def read_all_data(db_session,table_name):

    if table_name == 'hotel':
        res_data = session.query(Hotel_Object).all()
        return res_data

    if table_name == 'service':
        res_data = session.query(Hotel_Service_Object).all()
        return res_data

    if table_name == 'booking_service':
        res_data = session.query(Booking_Service_Object).all()
        return res_data

    if table_name == 'config':
        res_data = session.query(Hotel_Configuration_Object).all()
        return res_data


############################################################################

def delete_all_data(table_name):

    if table_name == 'hotel':
        all_rows = delete(Hotel_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'service':
        all_rows = delete(Hotel_Service_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'booking_service':
        all_rows = delete(Booking_Service_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'config':
        all_rows = delete(Hotel_Configuration_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

############################################################################


#create_hotel('Cerritos','tenant278','user58','west indiana',754958)
#create_service('secret service','star trek lower decks season 5',857.27,'Thursday')

#create_link_btwn_hotel_service(session,'operation_schedule','Thursday','hotel_name','Cerritos')


