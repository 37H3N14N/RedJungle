from functions.db_operations import create_guest
from functions.db_operations import create_booking
from functions.db_operations import create_invoice
from functions.db_operations import create_link_btwn_guest_booking
from functions.db_operations import read_data
from functions.db_operations import read_all_data
from functions.db_operations import update_data
from functions.db_operations import delete_data
from functions.db_operations import delete_all_data
from databank.booking_db_initialization import get_session

import httpx
import random
import json
from datetime import datetime

################## GLOBAL VARIABLES ##################################

session = get_session()

base_url = "http://redjungle-00.lab:7070"

guest_url = f"{base_url}/guest"
booking_url = f"{base_url}/booking"
invoice_url = f"{base_url}/invoice"

get_booking_url = f"{base_url}/get/booking"
get_guest_url = f"{base_url}/get/guest"
get_invoice_url = f"{base_url}/get/invoice"


def get_current_year():
    current_date = datetime.now()
    year = current_date.year
    return year

##########################################################################3

def invoice_function(payload):
    print('////////////// INVOICE //////////////////////////////////')
    invoice_action = payload.payload['action']

    if invoice_action == 'create':

        booking_id = payload.payload['details']['booking_id']
        invoice_number_unique_status = True
        
        while invoice_number_unique_status:

            current_invoice_number = []
            invoice_number_volatile = random.randint(105400,987250)
            current_invoice_number.append(invoice_number_volatile)

            duplicate_check_paylaod = input_data_structure_conversion(action='get',parameter_nested_list=[['entity_count','single'],['invoice_number',current_invoice_number[0]],['task_specification','invoice_number_unique_check']])
            check_duplicate_invoice_number = httpx.post(get_invoice_url,json=duplicate_check_paylaod)

            if check_duplicate_invoice_number.json()['payload']['details']['available_status'] == 'available_number':
                invoice_number_unique_status == False
                new_invoice = create_invoice(booking_id_input=booking_id,invoice_number_input=current_invoice_number[0])
                new_invoice_structured = input_data_structure_conversion(action='delivery',parameter_nested_list=[['invoice_id',new_invoice[0]['invoice_id']]])
                print(f'New invoice item = {new_invoice_structured}')
                return new_invoice_structured

            if check_duplicate_invoice_number.json()['payload']['details']['available_status'] == 'unavailable_number':
                print(f'Invoice Number already in use => {current_invoice_number[0]}')
            


    if invoice_action == 'get':
        invoice_payload = payload.payload['details']
    
        if invoice_payload['entity_count'] == "multiple":
            invoice_data_bank = []
            invoice_bulk = read_data(session,'invoice')
            invoice_data_bank_structured = input_data_structure_conversion(action='delivery',parameter_nested_list=[['invoice_bulk',invoice_data_bank]])

            for invoice_object in invoice_bulk:
                structured_invoice = {'invoice_id':invoice_object.invoice_id,'invoice_number': invoice_object.invoice_number, 'booking_id': invoice_object.booking_id}
                invoice_data_bank.append(structured_invoice)

            return invoice_data_bank_structured


        if invoice_payload['entity_count'] == "single":

            if invoice_payload['task_specification'] == 'invoice_number_unique_check':
                
                invoice_data_pool = read_all_data(session,'invoice')
                invoice_number_pool = [entity.invoice_number for entity in invoice_data_pool]

                if invoice_data_pool == None:
                    status_data = "available_number"
                    availability_check = input_data_structure_conversion(action='delivery',parameter_nested_list=[['available_status',status_data]])
                    return availability_check

                if invoice_data_pool != None:
                    if invoice_payload['invoice_number'] in invoice_number_pool:
                        status_data = "unavailable_number"
                        availability_check = input_data_structure_conversion(action='delivery',parameter_nested_list=[['available_status',status_data]])
                        return availability_check

                    else:
                        status_data = "available_number"
                        availability_check = input_data_structure_conversion(action='delivery',parameter_nested_list=[['available_status',status_data]])
                        return availability_check


    if invoice_action == 'delete':
        pass


def booking_function(payload):
    print('////////////// BOOKING ////////////////////')
    booking_action = payload.payload['action']

    if booking_action == 'create':

        tenant_id = payload.payload['details']['tenant_id']
        user_id = payload.payload['details']['user_id']
        email = payload.payload['details']['email']
        hotel_id = payload.payload['details']['hotel_id']
        room_id = payload.payload['details']['room_id']
        check_in_date = payload.payload['details']['check_in_date']
        check_out_date = payload.payload['details']['check_out_date']
        total_price = payload.payload['details']['total_price']
        payment_transaction_id = payload.payload['details']['payment_transaction_id']

        room_available_check = check_room_availability(room_id,f'{get_current_year()}_{check_in_date}',f'{get_current_year()}_{check_out_date}')

        if room_available_check[0] == 'available':

            guest_call_payload = input_data_structure_conversion(action='create',parameter_nested_list=[['user_id',user_id],['email',email]])
            make_guest = httpx.post(guest_url, json=guest_call_payload)

            new_booking = create_booking(tenant_id_input=tenant_id,hotel_id_input=hotel_id,room_id_input=room_id,check_in_date_input=f'{get_current_year()}_{check_in_date}',check_out_date_input=f'{get_current_year()}_{check_out_date}',total_price_input=total_price,payment_transaction_id_input=payment_transaction_id)
            print(f'New booking item = {new_booking[0]}')
            create_link_btwn_guest_booking(session,'guest_id',make_guest.json()['payload']['details']['guest_object']['guest_id'],'booking_id',new_booking[0]['booking_id'])

            invoice_data = input_data_structure_conversion(action='create',parameter_nested_list=[['booking_id',new_booking[0]['booking_id']]])
            create_invoice = httpx.post(invoice_url,json=invoice_data)

            return input_data_structure_conversion(action='succesful',parameter_nested_list=[['message',f'new guest of email = {email} has been created']])
            
        elif room_available_check[0] == 'unavailable':
            room_booking_failed = input_data_structure_conversion(action='failed',parameter_nested_list=[['message',f'room = {room_id} already booked']])
            return room_booking_failed


    if booking_action == 'get':
        room_id_booking = payload.payload['details']['room_id']
        guest_id_booking = payload.payload['details']['guest_id']

        if room_id_booking:
            booking_data_room = read_data(session,'booking','room_id',room_id_booking)
            return booking_data_room

        if guest_id_booking:
            booking_data_guest = read_data(session,'guest','guest_id',guest_id_booking)
            return booking_data_guest


    if booking_action == 'delete':
        pass



def guest_function(payload):
    print('////////////// GUEST /////////////////////')
    guest_action = payload.payload['action']

    if guest_action == 'create':
        user_id = payload.payload['details']['user_id']
        email = payload.payload['details']['email']
        guest_call_payload = input_data_structure_conversion(action='get',parameter_nested_list=[['user_id',user_id],['email',email],['entity_count','single']])

        check_guest_existance = httpx.post(get_guest_url,json=guest_call_payload)

        if check_guest_existance.json()['payload']['action'] == 'None':
            new_guest = create_guest(user_id_input=user_id,email_input=email)
            new_guest_created = input_data_structure_conversion(action='delivery',parameter_nested_list=[['guest_object',new_guest[0]]])
            print(f'New guest created = {new_guest_created}')
            return new_guest_created

        if check_guest_existance.json()['payload']['action'] ==  'delivery':
            print(f'Guest already exists = {check_guest_existance.json()}')
            return check_guest_existance.json()


    if guest_action == 'get':

        if payload.payload['details']['entity_count'] == "single":
            user_id = payload.payload['details']['user_id']
            guest_info = read_data(session,'guest','user_id',user_id)

            if guest_info == None:
                guest_call_payload = input_data_structure_conversion(action='None', parameter_nested_list=[['guest','not found']])
                return guest_call_payload

            if guest_info != None:
                guest_call_payload = input_data_structure_conversion(action='delivery', parameter_nested_list=[['guest_object',guest_info]])
                return guest_call_payload

        elif payload.payload['details']['entity_count'] == "multiple":
            guests_infos= read_data(session,'guest')
            return guests_infos


    if guest_action == 'delete':
        pass
    
    else:
        pass


########################## MODULAR FUNCTIONS ##################################


def check_room_availability(room_id_chosen,check_in_date,check_out_date):
    booking_data_collection = read_all_data(session,'booking')
    similar_room_booking = []
    room_availability_status = ['available']
    unavailable_chosen_days = []
    

    for booking in booking_data_collection:
        if booking.room_id == room_id_chosen:
            similar_room_booking.append(booking)

    my_year_date_split_start = check_in_date.split('_')
    my_year_date_split_end = check_out_date.split('_')

    my_check_in_date = check_in_out_date_transformation(my_year_date_split_start[1])
    my_check_out_date = check_in_out_date_transformation(my_year_date_split_end[1])

    chosen_occupation_days = [i for i in range(my_check_in_date[0],my_check_out_date[0])]

    if len(similar_room_booking) >= 1:

        for each_guest_booking in similar_room_booking:
            if len(each_guest_booking.guests) > 0:

                taken_year_date_start = each_guest_booking.check_in_date
                taken_check_in_day_start = check_in_out_date_transformation(taken_year_date_start.split('_')[1])

                taken_year_date_end = each_guest_booking.check_out_date
                taken_check_out_day_end = check_in_out_date_transformation(taken_year_date_end.split('_')[1])

                unavailable_occupation_days = [i for i in range(taken_check_in_day_start[0],taken_check_out_day_end[0])]
                [unavailable_chosen_days.append(i) for i in unavailable_occupation_days]

                already_booked_days = check_booked_days_between_two_entities(
                    chosen_occupation_days,
                    unavailable_occupation_days
                )

                if len(already_booked_days) > 0:
                    room_availability_status[0] = 'unavailable'

                if len(already_booked_days) == 0:
                    room_availability_status[0] = 'available'

            elif len(each_guest_booking.guests) == 0:
                room_availability_status[0] = 'available'
            
    if len(similar_room_booking) == 0:
        room_availability_status[0] = 'available'

    print(f'My chosen days = {chosen_occupation_days}')
    print(f'Unavailable chosen days = {list(set(unavailable_chosen_days))}')

    return room_availability_status


def check_booked_days_between_two_entities(chosen_day_list,found_day_list):
    taken_days = []

    for day in  chosen_day_list:
        if day in found_day_list:
            taken_days.append(day)

    return taken_days
                


def check_in_out_date_transformation(month_daycount):

    date_list = month_daycount.split('-')
    month = date_list[0]
    day = int(date_list[1])

    if month == 'jan':
        return [day + 0]
    if month == 'feb':
        return [day + 31]
    if month == 'mar':
        return [day + 59]
    if month == 'apr':
        return [day + 89]
    if month == 'may':
        return [day + 120]
    if month == 'jun':
        return [day + 150]
    if month == 'jul':
        return [day + 181]
    if month == 'aug':
        return [day + 212]
    if month == 'sep':
        return [day + 242]
    if month == 'oct':
        return [day + 273]
    if month == 'nov':
        return [day + 303]
    if month == 'dec':
        return [day + 334]


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











