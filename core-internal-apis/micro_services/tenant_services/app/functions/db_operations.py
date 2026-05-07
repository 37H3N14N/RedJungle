from sqlalchemy import update, delete
import uuid
from datetime import datetime 

from databank.tenant_db_initialization import get_session
from databank.tenant_db_initialization import Tenant_Object
from databank.tenant_db_initialization import Billing_Object


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

def create_tenant(tenant_name_input,super_admin_user_id_input,subscription_plan_input,status_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    tenant_item = Tenant_Object(
        tenant_id= constant_uuid[0],
        tenant_name= tenant_name_input,
        super_admin_user_id= super_admin_user_id_input,
        subscription_plan= subscription_plan_input,
        status= status_input,
        created_at= get_timestamp()
        )

    response_data.append({'tenant_id': f'{constant_uuid[0]}'})

    session.add(tenant_item)
    session.commit()
    session.close()

    return response_data

############################################################################

def create_billing(next_payment_after_days_input,total_amount_input,payment_transaction_id_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    billing_item = Billing_Object(
        billing_id= constant_uuid[0],
        next_payment_after_days= next_payment_after_days_input,
        total_amount= total_amount_input,
        payment_transaction_id= payment_transaction_id_input,
        created_at= get_timestamp()
        )

    response_data.append({'billing_id': f'{constant_uuid[0]}'})

    session.add(billing_item)
    session.commit()
    session.close()

    return response_data

###################################################################

def create_link_btwn_tenant_billing(db_session,billing_column_name,billing_row_identifier,tenant_column_name,tenant_row_identifier):

    target_tenant = read_data(db_session,'tenant',tenant_column_name,tenant_row_identifier)
    target_billing = read_data(db_session,'billing',billing_column_name,billing_row_identifier)

    target_tenant.billings.append(target_billing)

    db_session.commit()
    db_session.close()
    return

############################################################################

def read_data(db_session,target_model_class,column_name,row_identifier):

    if target_model_class == 'tenant':
        column = getattr(Tenant_Object,column_name)
        target_item = db_session.query(Tenant_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'billing':
        column = getattr(Billing_Object,column_name)
        target_item = db_session.query(Billing_Object).filter(column == f'{row_identifier}').first()
        return target_item

############################################################################

def update_data(db_session,target_model_class,identifying_column_name,identifying_row_entity,target_column_to_change,new_value_of_cell):

    if target_model_class == 'tenant':

        identify_column = getattr(Tenant_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Tenant_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


    if target_model_class == 'billing':

        identify_column = getattr(Billing_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Billing_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


############################################################################

def delete_data(db_session,main_id,target_model_class):

    if target_model_class == 'tenant':
        target_item = db_session.query(Tenant_Object).filter(Tenant_Object.tenant_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 


    if target_model_class == 'billing':
        target_item = db_session.query(Billing_Object).filter(Billing_Object.billing_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 


############################################################################

def read_all_data(db_session,table_name):

    if table_name == 'tenant':
        res_data = db_session.query(Tenant_Object).all()
        return res_data

    if table_name == 'billing':
        res_data = db_session.query(Billing_Object).all()
        return res_data


############################################################################

def delete_all_data(table_name):

    if table_name == 'tenant':
        all_rows = delete(Tenant_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'billing':
        all_rows = delete(Billing_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 


############################################################################

#create_tenant('big_belly_zone','user001','basic','active','Today15Month')
#create_billing(62, 587.00,'transaction_oo2','2SolarMonths')
#create_link_btwn_tenant_billing(session,'billing_id','$F45','tenant_name','big_belly_zone')


#data_one = read_all_data(session,'tenant')

#for entity in data_one:
#    print(entity.tenant_name)
#    for bill in entity.billings:
#        print(bill.next_payment_after_days,bill.total_amount,bill.created_at)
#session.close()




