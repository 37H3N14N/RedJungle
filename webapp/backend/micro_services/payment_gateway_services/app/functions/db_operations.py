from sqlalchemy import update, delete
import uuid
from datetime import datetime 

from databank.payment_gateway_db_initialization import get_session
from databank.payment_gateway_db_initialization import Transaction_Object
from databank.payment_gateway_db_initialization import Customer_Object
from databank.payment_gateway_db_initialization import Bank_Object
from databank.payment_gateway_db_initialization import Account_Object


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

def create_transaction(user_id_input,tenant_id_input,card_number_input,amount_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    transaction_item = Transaction_Object(
        transaction_id= constant_uuid[0],
        user_id= user_id_input,
        tenant_id= tenant_id_input,
        card_number = card_number_input,
        amount= amount_input,
        created_at= get_timestamp()
        )

    response_data.append({'transaction_id': f'{constant_uuid[0]}'})

    session.add(transaction_item)
    session.commit()
    session.close()

    return response_data

############################################################################

def create_customer(user_id_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    customer_item = Customer_Object(
        customer_id= constant_uuid[0],
        user_id= user_id_input
        )

    response_data.append({'customer_id': f'{constant_uuid[0]}'})

    session.add(customer_item)
    session.commit()
    session.close()

    return response_data

############################################################################

def create_bank(bank_name_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    bank_item = Bank_Object(
        bank_id = constant_uuid[0],
        bank_name = bank_name_input
    )

    response_data.append({'bank_id': f'{constant_uuid[0]}'})

    session.add(bank_item)
    session.commit()
    session.close()

    return response_data

############################################################################

def create_account(bank_id_input,card_number_input,account_balance_input,updated_at_input):
    constant_uuid = []
    response_data = []
    constant_uuid.append(get_uuid4())

    account_item = Account_Object(
        account_id = constant_uuid[0],
        bank_id = bank_id_input,
        card_number = card_number_input,
        account_balance = account_balance_input,
        updated_at = updated_at_input

    )

    response_data.append({'account_id': f'{constant_uuid[0]}'})
    response_data.append({'card_number': f'{account_item.card_number}'})

    session.add(account_item)
    session.commit()
    session.close()

    return response_data

###################################################################

def create_link_btwn_bank_account(db_session,account_column_name,account_row_identifier,bank_column_name,bank_row_identifier):

    target_bank = read_data(db_session,'bank',bank_column_name,bank_row_identifier)
    target_account = read_data(db_session,'account',account_column_name,account_row_identifier)

    target_bank.accounts.append(target_account)

    db_session.commit()
    db_session.close()
    return

############################################################################

def create_link_btwn_customer_account(db_session,customer_column_name,customer_row_identifier,account_column_name,account_row_identifier):

    target_customer = read_data(db_session,'customer',customer_column_name,customer_row_identifier)
    target_account = read_data(db_session,'account',account_column_name,account_row_identifier)

    target_customer.accounts.append(target_account)

    db_session.commit()
    db_session.close()
    return

############################################################################

def read_data(db_session,target_model_class,column_name,row_identifier):

    if target_model_class == 'transaction':
        column = getattr(Transaction_Object,column_name)
        target_item = db_session.query(Transaction_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'bank':
        column = getattr(Bank_Object,column_name)
        target_item = db_session.query(Bank_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'customer':
        column = getattr(Customer_Object,column_name)
        target_item = db_session.query(Customer_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'account':
        column = getattr(Account_Object,column_name)
        target_item = db_session.query(Account_Object).filter(column == f'{row_identifier}').first()
        return target_item

############################################################################

def update_data(db_session,target_model_class,identifying_column_name,identifying_row_entity,target_column_to_change,new_value_of_cell):

    if target_model_class == 'bank':

        identify_column = getattr(Bank_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Bank_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


    if target_model_class == 'customer':

        identify_column = getattr(Customer_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Customer_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


    if target_model_class == 'account':

        identify_column = getattr(Account_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Account_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


############################################################################

def delete_data(db_session,main_id,target_model_class):

    if target_model_class == 'transaction':
        target_item = db_session.query(Transaction_Object).filter(Transaction_Object.transaction_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 

    if target_model_class == 'bank':
        target_item = db_session.query(Bank_Object).filter(Bank_Object.bank_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 

    if target_model_class == 'customer':
        target_item = db_session.query(Customer_Object).filter(Customer_Object.customer_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 

    if target_model_class == 'account':
        target_item = db_session.query(Account_Object).filter(Account_Object.account_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 

############################################################################

def read_all_data(db_session,table_name):

    if table_name == 'transaction':
        res_data = db_session.query(Transaction_Object).all()
        return res_data

    if table_name == 'bank':
        res_data = db_session.query(Bank_Object).all()
        return res_data

    if table_name == 'customer':
        res_data = db_session.query(Customer_Object).all()
        return res_data

    if table_name == 'account':
        res_data = db_session.query(Account_Object).all()
        return res_data

############################################################################

def delete_all_data(table_name):

    if table_name == 'transaction':
        all_rows = delete(Transaction_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'bank':
        all_rows = delete(Bank_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'customer':
        all_rows = delete(Customer_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'account':
        all_rows = delete(Account_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

############################################################################


#create_bank('user2','mastercard',451745174517,'Tuesday5thNever',58500.25,'4THnow')
#create_transaction('user45','tenanat001',457.05,'successful','bank#5','visa',5782,'2ndYear')






