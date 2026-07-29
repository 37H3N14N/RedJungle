from sqlalchemy import update, delete
import uuid
from datetime import datetime 

from databank.user_db_initialization import get_session
from databank.user_db_initialization import User_Object
from databank.user_db_initialization import Profile_Object


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

def create_user(tenant_id_input,role_id_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    user_item = User_Object(
        user_id= constant_uuid[0],
        tenant_id= tenant_id_input,
        role_id= role_id_input,
        updated_at= get_timestamp(),
        created_at= get_timestamp()
        )

    response_data.append({'user_id': f'{constant_uuid[0]}'})

    session.add(user_item)
    session.commit()
    session.close()

    return response_data

############################################################################

def create_profile(profile_picture_url_input,first_name_input,last_name_input,email_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    profile_item = Profile_Object(
        profile_id= constant_uuid[0],
        profile_picture_url= profile_picture_url_input,
        first_name= first_name_input,
        last_name= last_name_input,
        email= email_input
        )

    response_data.append({'profile_id': f'{constant_uuid[0]}'})

    session.add(profile_item)
    session.commit()
    session.close()

    return response_data

###################################################################

def create_link_btwn_user_profile(db_session,profile_column_name,profile_row_identifier,user_column_name,user_row_identifier):

    target_user = read_data(db_session,'user',user_column_name,user_row_identifier)
    target_profile = read_data(db_session,'profile',profile_column_name,profile_row_identifier)

    target_user.profiles.append(target_profile)

    db_session.commit()
    db_session.close()
    return

############################################################################

def read_data(db_session,target_model_class,column_name,row_identifier):

    if target_model_class == 'user':
        column = getattr(User_Object,column_name)
        target_item = db_session.query(User_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'profile':
        column = getattr(Profile_Object,column_name)
        target_item = db_session.query(Profile_Object).filter(column == f'{row_identifier}').first()
        return target_item

############################################################################

def update_data(db_session,target_model_class,identifying_column_name,identifying_row_entity,target_column_to_change,new_value_of_cell):

    if target_model_class == 'user':

        identify_column = getattr(User_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(User_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


    if target_model_class == 'profile':

        identify_column = getattr(Profile_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Profile_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


############################################################################

def delete_data(db_session,main_id,target_model_class):

    if target_model_class == 'user':
        target_item = db_session.query(User_Object).filter(User_Object.user_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 


    if target_model_class == 'profile':
        target_item = db_session.query(Profile_Object).filter(Profile_Object.profile_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 

############################################################################

def read_all_data(db_session,table_name):

    if table_name == 'user':
        res_data = db_session.query(User_Object).all()
        return res_data

    if table_name == 'profile':
        res_data = db_session.query(Profile_Object).all()
        return res_data


############################################################################

def delete_all_data(table_name):

    if table_name == 'user':
        all_rows = delete(User_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'profile':
        all_rows = delete(Profile_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

############################################################################

#create_user('tenant0014','role475','56Solar45','1200Solar74')
#create_profile('picture/url/here','John','Diggle','arrow@island.company')
#create_link_btwn_user_profile(session,'first_name','John','role_id','role475')

#data_one = read_all_data(session,'user')
#
#for entity in data_one:
#    print(entity.role_id,entity.tenant_id)
#    for prof in entity.profiles:
#        print(prof.first_name)
#session.close()




