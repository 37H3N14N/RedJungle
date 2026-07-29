from sqlalchemy import update, delete
import uuid
from datetime import datetime 

from databank.access_control_db_initialization import get_session
from databank.access_control_db_initialization import Policy_Object
from databank.access_control_db_initialization import Role_Object
from databank.access_control_db_initialization import Decision_Log_Object


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

def create_policy(service_id_input,uri_input,allowed_methods_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    policy_item = Policy_Object(
        policy_id= constant_uuid[0], 
        service_id=service_id_input,
        uri=uri_input,
        allowed_methods=allowed_methods_input
        )
        
    response_data.append({'policy_id': f'{constant_uuid[0]}'})

    session.add(policy_item)
    session.commit()
    session.close()

    return response_data

############################################################################

def create_role(role_name_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    role_item = Role_Object(
        role_id= constant_uuid[0],
        role_name= role_name_input
        )
        
    response_data.append({'role_id': f'{constant_uuid[0]}'})

    session.add(role_item)
    session.commit()
    session.close()

    return response_data

###################################################################

def create_decision_log(user_id_input,tenant_id_input,service_id_input,crud_action_input,allowed_input,policy_based_reason_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    decision_log_item = Decision_Log_Object(
        decision_id= constant_uuid[0],
        user_id= user_id_input,
        tenant_id= tenant_id_input,
        service_id= service_id_input,
        crud_action= crud_action_input,
        allowed=allowed_input,
        policy_based_reason= policy_based_reason_input,
        timestamp= get_timestamp()
        )
        
    response_data.append({'decision_id': f'{constant_uuid[0]}'})

    session.add(decision_log_item)
    session.commit()
    session.close()

    return response_data

###################################################################

def create_link_btwn_policy_role(db_session,policy_column_name,policy_row_identifier,role_column_name,role_row_identifier):

    target_policy = read_data(db_session,'policy',policy_column_name,policy_row_identifier)
    target_role = read_data(db_session,'role',role_column_name,role_row_identifier)

    target_policy.roles.append(target_role)

    db_session.commit()
    db_session.close()
    return

############################################################################

def read_data(db_session,target_model_class,column_name,row_identifier):

    if target_model_class == 'policy':
        column = getattr(Policy_Object,column_name)
        target_item = db_session.query(Policy_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'decision_log':
        column = getattr(Decision_Log_Object,column_name)
        target_item = db_session.query(Decision_Log_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'role':
        column = getattr(Role_Object,column_name)
        target_item = db_session.query(Role_Object).filter(column == f'{row_identifier}').first()
        return target_item

############################################################################

def update_data(db_session,target_model_class,identifying_column_name,identifying_row_entity,target_column_to_change,new_value_of_cell):

    if target_model_class == 'policy':

        identify_column = getattr(Policy_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Policy_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


    if target_model_class == 'role':

        identify_column = getattr(Role_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Role_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


############################################################################

def delete_data(db_session,main_id,target_model_class):

    if target_model_class == 'policy':
        target_item = db_session.query(Policy_Object).filter(Hotel_Object.hotel_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 


    if target_model_class == 'role':
        target_item = db_session.query(Role_Object).filter(Hotel_Service_Object.service_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 

    if target_model_class == 'decision_log':
        target_item = db_session.query(Decision_Log_Object).filter(Hotel_Configuration_Object.config_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 

############################################################################

def read_all_data(db_session,table_name):

    if table_name == 'policy':
        res_data = session.query(Policy_Object).all()
        return res_data

    if table_name == 'role':
        res_data = session.query(Role_Object).all()
        return res_data

    if table_name == 'decision_log':
        res_data = session.query(Decision_Log_Object).all()
        return res_data


############################################################################

def delete_all_data(table_name):

    if table_name == 'policy':
        all_rows = delete(Policy_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'role':
        all_rows = delete(Role_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'decision_log':
        all_rows = delete(Decision_Log_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

############################################################################


#create_link_btwn_policy_role(session,'service_id','#58','role_name','omiman')








