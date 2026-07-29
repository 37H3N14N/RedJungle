from sqlalchemy import update, delete
import uuid
from datetime import datetime 

from databank.hotel_management_db_initialization import get_session
from databank.hotel_management_db_initialization import Amenity_Object
from databank.hotel_management_db_initialization import Picture_Object
from databank.hotel_management_db_initialization import Room_Object


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

def create_amenity(amenity_name_input,amenity_description_input,max_occupancy_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    amenity_item = Amenity_Object(
        amenity_id= constant_uuid[0],
        amenity_name= amenity_name_input,
        amenity_description= amenity_description_input,
        max_occupancy= max_occupancy_input
        )

    response_data.append({'amenity_id': f'{constant_uuid[0]}'})

    session.add(amenity_item)
    session.commit()
    session.close()

    return response_data

############################################################################

def create_picture(picture_url_input,date_created_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    picture_item = Picture_Object(
        picture_id= constant_uuid[0],
        picture_url= picture_url_input,
        date_created= get_timestamp()
        )

    response_data.append({'picture_id': f'{constant_uuid[0]}'})

    session.add(picture_item)
    session.commit()
    session.close()

    return response_data

###################################################################

def create_room(room_no_input,room_name_input,hotel_id_input,status_input,price_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    room_item = Room_Object(
        room_id= constant_uuid[0],
        room_no= room_no_input,
        room_name= room_name_input,
        hotel_id= hotel_id_input,
        status= status_input,
        price= price_input
        )

    response_data.append({'room_id': f'{constant_uuid[0]}'})

    session.add(room_item)
    session.commit()
    session.close()

    return response_data

###################################################################

def create_link_btwn_room_amenity(db_session,amenity_column_name,amenity_row_identifier,room_column_name,room_row_identifier):

    target_room = read_data(db_session,'room',room_column_name,room_row_identifier)
    target_amenity = read_data(db_session,'amenity',amenity_column_name, amenity_row_identifier)

    target_room.amenities.append(target_amenity)

    db_session.commit()
    db_session.close()
    return

def create_link_btwn_amenity_picture(db_session,picture_column_name,picture_row_identifier,amenity_column_name,amenity_row_identifier):

    target_amenity = read_data(db_session,'amenity',amenity_column_name,amenity_row_identifier)
    target_picture = read_data(db_session,'picture',picture_column_name,picture_row_identifier)

    target_amenity.pictures.append(target_picture)

    db_session.commit()
    db_session.close()
    return



############################################################################

def read_data(db_session,target_model_class,column_name,row_identifier):

    if target_model_class == 'amenity':
        column = getattr(Amenity_Object,column_name)
        target_item = db_session.query(Amenity_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'room':
        column = getattr(Room_Object,column_name)
        target_item = db_session.query(Room_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'picture':
        column = getattr(Picture_Object,column_name)
        target_item = db_session.query(Picture_Object).filter(column == f'{row_identifier}').first()
        return target_item

############################################################################

def update_data(db_session,target_model_class,identifying_column_name,identifying_row_entity,target_column_to_change,new_value_of_cell):

    if target_model_class == 'amenity':

        identify_column = getattr(Amenity_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Amenity_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


    if target_model_class == 'picture':

        identify_column = getattr(Picture_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Picture_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


    if target_model_class == 'room':

        identify_column = getattr(Room_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Room_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


############################################################################

def delete_data(db_session,main_id,target_model_class):

    if target_model_class == 'amenity':
        target_item = db_session.query(Amenity_Object).filter(Amenity_Object.amenity_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 

    if target_model_class == 'picture':
        target_item = db_session.query(Picture_Object).filter(Picture_Object.picture_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 

    if target_model_class == 'room':
        target_item = db_session.query(Room_Object).filter(Room_Object.room_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 

############################################################################

def read_all_data(db_session,table_name):

    if table_name == 'amenity':
        res_data = db_session.query(Amenity_Object).all()
        return res_data

    if table_name == 'picture':
        res_data = db_session.query(Picture_Object).all()
        return res_data

    if table_name == 'room':
        res_data = db_session.query(Room_Object).all()
        return res_data


############################################################################

def delete_all_data(table_name):

    if table_name == 'amenity':
        all_rows = delete(Amenity_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'picture':
        all_rows = delete(Picture_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'room':
        all_rows = delete(Room_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

############################################################################


#create_amenity('pool','liquid glass and salty', 15)
#create_picture('http://picture/here','50Jan3096')
#create_room('4c','hotel_585','under maintenance',245.55)

#create_link_btwn_room_amenity(session,'amenity_name','pool','hotel_id','hotel_585')
#create_link_btwn_amenity_picture(session,'date_created','50Jan3096','max_occupancy',15)

#data_one = read_all_data(session,'room')
#
#for data_entity in data_one:
#    print(data_entity.room_no,data_entity.status,data_entity.price)
#    for min_entity in data_entity.amenities:
#        print(min_entity.amenity_name)
#        for items in min_entity.pictures:
#            print(items.picture_url)
#








