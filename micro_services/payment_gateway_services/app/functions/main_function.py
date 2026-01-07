from functions.db_operations import create_transaction
from functions.db_operations import create_bank
from functions.db_operations import create_customer
from functions.db_operations import create_account
from functions.db_operations import create_link_btwn_bank_account
from functions.db_operations import create_link_btwn_customer_account

from functions.db_operations import read_data
from functions.db_operations import read_all_data
from functions.db_operations import update_data
from functions.db_operations import delete_data
from functions.db_operations import delete_all_data
from databank.payment_gateway_db_initialization import get_session

import httpx
import json
import random
from datetime import datetime

################## GLOBAL VARIABLES ##################################

session = get_session()

base_url = "http://redjungle-00.lab:7060"

bank_url = f"{base_url}/bank"
transaction_url = f"{base_url}/transaction"
customer_url = f"{base_url}/customer"
account_url = f"{base_url}/account"

def get_current_year():
    current_date = datetime.now()
    year = current_date.year
    return year

##########################################################################3

def transaction_function(payload):

    if  payload.payload['action'] == 'create':

        user_id = payload.payload['details']['user_id']
        tenant_id = payload.payload['details']['tenant_id']
        card_number = payload.payload['details']['card_number']
        amount = payload.payload['details']['amount']


        check_customer_existance_payload = input_data_structure_conversion(action='get',parameter_nested_list=[['description','existance'],['user_id',user_id]])
        check_customer_existance = httpx.post(customer_url, json=check_customer_existance_payload)
        customer_id = check_customer_existance.json()['payload']['details']['customer_id']

        if check_customer_existance.json()['payload']['details']['description'] == 'found':
            print(f'User of id = {user_id} is a Customer of id = {customer_id}') 

        if check_customer_existance.json()['payload']['details']['description'] == 'not_found':
           return f'Customer of User of id = {user_id} does not exist' 

        check_customer_account_existance_payload = input_data_structure_conversion(action='get',parameter_nested_list=[['description','account_existance'],['customer_id',customer_id],['card_number', card_number]])
        check_customer_account_existance= httpx.post(customer_url, json=check_customer_account_existance_payload)
        print(f'////////////////////////// = {check_customer_account_existance.json()}')
        account_id = check_customer_account_existance.json()['payload']['details']['account_id']

        if check_customer_account_existance.json()['payload']['details']['description'] == 'found':
            print(f'User of id = {user_id} has Account of id = {account_id}') 

        if check_customer_account_existance.json()['payload']['details']['description'] == 'not_found':
            return f'User of id = {user_id} and customer id of = {customer_id} has no such account'

        check_account_payment_viability_payload= input_data_structure_conversion(action='get',parameter_nested_list=[['description','account_payment_viability'],['account_id',account_id],['amount',amount]])
        check_account_payment_viability= httpx.post(account_url, json=check_account_payment_viability_payload)

        if check_account_payment_viability.json()['payload']['details']['description'] == 'viable':

            account_balance_update_payload = input_data_structure_conversion(action='update',parameter_nested_list=[['account_id',account_id],['amount',amount]])
            account_balance_update = httpx.post(account_url, json=account_balance_update_payload)
            print(account_balance_update.json())

            new_transaction = create_transaction(user_id_input=user_id,tenant_id_input=tenant_id,card_number_input=card_number,amount_input=amount)
            transaction_id = new_transaction[0]['transaction_id']
            transaction_completion_message = input_data_structure_conversion(action='delivery',parameter_nested_list=[['description','Transaction Fully Completed'],['transaction_id',transaction_id]])

            return transaction_completion_message

        if check_account_payment_viability.json()['payload']['details']['description'] == 'not_viable':
            print(f'You have insufficient funds')
            return f'You have insufficient funds'


    if  payload.payload['action'] == 'get':

        if payload.payload['details']['description'] == 'retrieve':
            all_transaction_data = read_all_data(session,'transaction')
            transaction_list_dict = []

            if all_transaction_data == None:
                pass

            if all_transaction_data != None:
                for transaction in all_transaction_data:
                    transaction_list_dict.append({
                            "transaction_id": transaction.transaction_id,
                            "user_id" : transaction.user_id,
                            "tenant_id" : transaction.tenant_id,
                            "card_number" : transaction.card_number,
                            "amount" : transaction.amount,
                            "created_at" : transaction.created_at
                        }
                    )

            print(f'list of transactions = {transaction_list_dict}')
            bulk_transaction_data = input_data_structure_conversion(action='delivery',parameter_nested_list=[['transactions',transaction_list_dict]])
            return bulk_transaction_data


    if  payload.payload['action'] == 'delete':
        pass


def bank_function(payload):

    if  payload.payload['action'] == 'create':
        bank_name = payload.payload['details']['bank_name']

        check_bank_existance_payload = input_data_structure_conversion(action='get',parameter_nested_list=[['description','existance'],['bank_name',bank_name]])
        check_bank_existance = httpx.post(bank_url,json=check_bank_existance_payload)

        if check_bank_existance.json()['payload']['details']['description'] == 'found':
            bank_data = check_bank_existance.json()['payload']['details']
            existing_bank_id = bank_data['bank_id']
            return f'bank already exists of id = {existing_bank_id}'

        if check_bank_existance.json()['payload']['details']['description'] == 'not_found':
            new_bank = create_bank(bank_name_input=bank_name)
            print(f'new bank id = {new_bank}')
            new_bank_id = new_bank[0]['bank_id']
            return f'new bank has been made and has id = {new_bank_id}'


    if  payload.payload['action'] == 'get':

        if payload.payload['details']['description'] == 'existance':
            bank_name = payload.payload['details']['bank_name']
            bank_data = read_data(session,'bank','bank_name',bank_name)

            if bank_data == None:
                bank_data_result = input_data_structure_conversion(action='delivery',parameter_nested_list=[['description','not_found']])
                return bank_data_result

            if bank_data != None:
                bank_data_result = input_data_structure_conversion(action='delivery',parameter_nested_list=[['description','found'],['bank_id',bank_data.bank_id]])
                return bank_data_result

        if payload.payload['details']['description'] == 'retrieve':
            all_banks_data = read_all_data(session,'bank')
            bank_list_dict = []

            if all_banks_data == None:
                pass

            if all_banks_data != None:
                for bank in all_banks_data:
                    bank_list_dict.append({
                            "bank_name": bank.bank_name,
                            "bank_id" : bank.bank_id,
                            "bank_accounts" : bank.accounts
                        }
                    )

            print(f'list of banks = {bank_list_dict}')
            bulk_bank_data = input_data_structure_conversion(action='delivery',parameter_nested_list=[['banks',bank_list_dict]])
            return bulk_bank_data


    if  payload.payload['action'] == 'delete':
        pass


def customer_function(payload):

    customer_data = payload.payload['details']
    if  payload.payload['action'] == 'create':

        check_user_data = input_data_structure_conversion(action='get',parameter_nested_list=[['description', 'existance'],['user_id',customer_data['user_id']]])
        check_user_api_call = httpx.post(customer_url,json=check_user_data)
        
        if check_user_api_call.json()['payload']['details']['description'] == 'found':
            customer_id = check_user_api_call.json()['payload']['details']['customer_id'] 
            user_id = customer_data['user_id']
            response_data_call_payload = input_data_structure_conversion(action='delivery',parameter_nested_list=[['description',f'customer of id = {customer_id} and has that user id'],['user_id', user_id]])
            return response_data_call_payload

        if check_user_api_call.json()['payload']['details']['description'] == 'not_found':
            new_customer = create_customer(customer_data['user_id'])
            new_customer_id = new_customer[0]['customer_id']
            response_data_call_payload = input_data_structure_conversion(action='delivery',parameter_nested_list=[['description', 'New customer created'],['customer_id', new_customer_id]])
            return response_data_call_payload


    if  payload.payload['action'] == 'get':

        if  payload.payload['details']['description'] == 'existance':
            user_id = customer_data['user_id']
            customer_list = read_all_data(session,'customer')

            for person in customer_list:
                if person.user_id == user_id:

                    search_response = input_data_structure_conversion(action='delivery',parameter_nested_list=[['description','found'],['customer_id',person.customer_id]])
                    return search_response
            search_response = input_data_structure_conversion(action='delivery',parameter_nested_list=[['description','not_found']])
            return search_response


        if  payload.payload['details']['description'] == 'account_existance':
            customer_id = customer_data['customer_id']
            card_number = customer_data['card_number']
            customer_instance = read_data(session,'customer','customer_id',customer_id)
            print(f'accounts => {customer_instance.accounts}')

            for account in customer_instance.accounts:
                if account.card_number == card_number:
                    account_existance_payload = input_data_structure_conversion(action='deliver',parameter_nested_list=[['description','found'],['account_id',account.account_id]])
                    return account_existance_payload
            
            account_existance_payload = input_data_structure_conversion(action='deliver',parameter_nested_list=[['description','not_found']])
            return account_existance_payload


        if  payload.payload['details']['description'] == 'retrieve':
            all_customer_data = read_all_data(session,'customer')
            customer_list_dict = []

            if all_customer_data == None:
                pass
            if all_customer_data != None:
                for customer in all_customer_data:
                    customer_list_dict.append({
                            "customer_id": customer.customer_id,
                            "user_id" : customer.user_id,
                            "accounts" : customer.accounts
                        }
                    )

            print(f'list of customers = {customer_list_dict}')
            bulk_customer_data = input_data_structure_conversion(action='delivery',parameter_nested_list=[['customers',customer_list_dict]])
            return bulk_customer_data
    

    if  payload.payload['action'] == 'update':
        pass

    if  payload.payload['action'] == 'delete':
        pass


def account_function(payload):
    account_data = payload.payload['details']
    if  payload.payload['action'] == 'create':

        user_id = account_data['user_id']
        bank_name = account_data['bank_name']

        bank_id_found = []
        customer_id_found = []
        card_number = []
        card_number.append(card_number_generator())

        bank_existance_payload = input_data_structure_conversion(action='get',parameter_nested_list=[['description', 'existance'],['bank_name',bank_name]])
        bank_existance = httpx.post(bank_url,json=bank_existance_payload)

        if bank_existance.json()['payload']['details']['description'] == 'found':
            bank_id_found.append(bank_existance.json()['payload']['details']['bank_id'])

        if bank_existance.json()['payload']['details']['description'] == 'not_found':
            return f'There is no bank of name = {bank_name} in existance'


        customer_existance_payload = input_data_structure_conversion(action='get',parameter_nested_list=[['description', 'existance'],['user_id',user_id]])
        customer_existance = httpx.post(customer_url,json=customer_existance_payload)

        if customer_existance.json()['payload']['details']['description'] == 'found':
            customer_id_found.append(customer_existance.json()['payload']['details']['customer_id'])

        if customer_existance.json()['payload']['details']['description'] == 'not_found':
            print(f'There is no customer of user id = {user_id} thus creating one')
            create_customer_api_call_payload = input_data_structure_conversion(action='create',parameter_nested_list=[['user_id',user_id]])
            create_customer_api_call = httpx.post(customer_url, json=create_customer_api_call_payload)
            customer_id_found.append(create_customer_api_call.json()['payload']['details']['customer_id'])


        check_account_api_call_payload = input_data_structure_conversion(action='get',parameter_nested_list=[['description', 'account_existance'],['card_number',card_number],['bank_id',bank_id_found[0]]])
        check_account_api_call = httpx.post(account_url,json=check_account_api_call_payload)
        
        if check_account_api_call.json()['payload']['details']['description'] == 'found':
            account_id = check_account_api_call.json()['payload']['details']['account_id'] 
            card_number = check_account_api_call.json()['payload']['details']['card_number'] 
            return f'Account of id = {account_id} and has  card number of = {card_number} already exists'

        if check_account_api_call.json()['payload']['details']['description'] == 'not_found':
            account_balance = account_data['account_balance']
            updated_at = get_timestamp()

            new_account = create_account(bank_id_input=bank_id_found[0],card_number_input=card_number[0],account_balance_input=account_balance,updated_at_input=updated_at)
            new_account_id = new_account[0]['account_id']
            create_link_btwn_customer_account(db_session=session,customer_column_name='customer_id',customer_row_identifier=customer_id_found[0],account_column_name='account_id',account_row_identifier=new_account_id)
            create_link_btwn_bank_account(db_session=session,bank_column_name='bank_id',bank_row_identifier=bank_id_found[0],account_column_name='account_id',account_row_identifier=new_account_id)

            return f'New account created with id = {new_account_id} with card number = {card_number[0]} '


    if  payload.payload['action'] == 'get':

        if  account_data['description'] == 'account_existance':
            card_number= account_data['card_number']
            bank_id = account_data['bank_id']

            account_list = read_all_data(session,'account')

            for account in account_list:
                stored_customer_instance = account.customers
                if account.card_number == card_number and account.bank_id == bank_id:
                    search_response = input_data_structure_conversion(action='delivery',parameter_nested_list=[['description','found'],['account_id',account.account_id],['card_number',account.card_number],['account_balance',account.account_balance]])
                    return search_response

            search_response = input_data_structure_conversion(action='delivery',parameter_nested_list=[['description','not_found']])
            return search_response


        if  account_data['description'] == 'retrieve':
            all_account_data = read_all_data(session,'account')
            account_list_dict = []

            if all_account_data == None:
                pass
            if all_account_data != None:
                for account in all_account_data:
                    account_list_dict.append({
                            "account_id": account.account_id,
                            "bank_id": account.bank_id,
                            "card_number": account.card_number,
                            "account_balance": account.account_balance,
                            "updated_at": account.updated_at
                        }
                    )

            print(f'list of accounts = {account_list_dict}')
            bulk_account_data = input_data_structure_conversion(action='delivery',parameter_nested_list=[['accounts',account_list_dict]])
            return bulk_account_data
    

        if  account_data['description'] == 'account_payment_viability':
            account_id = account_data['account_id']
            amount = account_data['amount']

            account_instance = read_data(session,'account','account_id',account_id)

            if account_instance.account_balance >= amount:
                payment_viability_response = input_data_structure_conversion(action='delivery',parameter_nested_list=[['description','viable']])
                return payment_viability_response

            if account_instance.account_balance < amount:
                payment_viability_response = input_data_structure_conversion(action='delivery',parameter_nested_list=[['description','not_viable']])
                return payment_viability_response


    if  payload.payload['action'] == 'update':

        account_id_current = account_data['account_id']
        amount_used = account_data['amount']

        account_instance = read_data(session,'account','account_id',account_id_current)
        updated_account_balance = int(account_instance.account_balance) - int(amount_used)

        account_instance.account_balance = updated_account_balance
        session.commit()

        return f'Account balance has been updated to = ${updated_account_balance}'
        



########################## MODULAR FUNCTIONS ##################################

def input_data_structure_conversion(action,parameter_nested_list):
    actual_dynamic_data = {}

    for item in parameter_nested_list:
        actual_dynamic_data[item[0]] = item[1]

    canonical_structure = {
        "server_authorization_token":"adasdfsd",
        "payload":{
            "action":action,
            "details":actual_dynamic_data
        }
    }
    return canonical_structure


def transform_list_string_bidirectional(change_direction,input_data_list,mediator_char):
    
    if change_direction == 'turn_to_list':
        list_converted = input_data_list[0].split(mediator_char)
        return list_converted

    if change_direction == 'turn_to_string':
        list_converted = mediator_char.join(input_data_list)
        return list_converted

    else:
        return 'change direction is invalid'


def card_number_generator():
        number_list = []
        for i in range(9):
            number_list.append(f"{random.randint(1,9)}")
        amalgamated_number = "".join(number_list)
        print(f'amalgamated number = {amalgamated_number}')
        return int(amalgamated_number)


def get_timestamp():
   now = datetime.now()
   refined_structure = now.strftime("%Y-%m-%d %H:%M:%S")
   return refined_structure











