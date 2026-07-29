from functions.db_operations import create_user
from functions.db_operations import create_profile
from functions.db_operations import create_link_btwn_user_profile

from functions.db_operations import read_data
from functions.db_operations import update_data
from functions.db_operations import delete_data

from functions.db_operations import read_all_data
from functions.db_operations import delete_all_data

import httpx


##################################################################
incoming_request = {
    'server_authorization_token':"",
    'payload':{
        "JWT":"",
        'detail_payload':{
            'tenant_id':'tenant0075',
            'role_id':'role005',
            'first_name':'Indiana',
            'second_name':'Indiana',
            'email':'Indiana@company.org'
        },
    }
}


def create_new_user(organised_data):
    useful_data = organised_data['payload']['detail_payload']
    new_instance_id = create_user(useful_data['tenant_id'],useful_data['role_id'])


    return new_instance_id



def get_user():
    pass


def get_profile(organised_data):
    pass






