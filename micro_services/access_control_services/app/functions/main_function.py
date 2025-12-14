from functions.db_operations import create_role
from functions.db_operations import create_policy
from functions.db_operations import create_decision_log
from functions.db_operations import create_link_btwn_policy_role
from functions.db_operations import read_data
from functions.db_operations import read_all_data
from functions.db_operations import update_data
from functions.db_operations import delete_data
from functions.db_operations import delete_all_data
from databank.access_control_db_initialization import get_session

import httpx
import json
from datetime import datetime

################## GLOBAL VARIABLES ##################################

session = get_session()

base_url = "http://redjungle-00.lab:7020"

role_url = f"{base_url}/role"
get_role_url = f"{base_url}/role"
policy_url = f"{base_url}/policy"
decision_log_url = f"{base_url}/decision-log"

##########################################################################3

def role_function(payload):
    
    if payload.payload['action'] == 'create':
        role_name_gotten = payload.payload['details']['role_name']

        get_role_payload = input_data_structure_conversion(action='get',parameter_nested_list=[['description','existance'],['role_name',role_name_gotten]])
        check_role_existance = httpx.post(get_role_url,json=get_role_payload)

        if check_role_existance.json() == 'not_found':
            created_role = create_role(role_name_gotten)
            response_data = input_data_structure_conversion(action='delivery',parameter_nested_list=[['role_id',created_role[0]['role_id']]]) 
            return response_data

        if check_role_existance.json() == 'found':
            response_data = input_data_structure_conversion(action='duplicate',parameter_nested_list=[['message' ,f'role [{role_name_gotten}] already existed']])
            return response_data


    if payload.payload['action'] == 'get':

        if payload.payload['details']['description'] == 'existance':
            search_db_role_name = read_data(session,'role','role_name',payload.payload['details']['role_name'])

            if search_db_role_name == None:
                return 'not_found'

            if search_db_role_name != None:
                return 'found'

        if payload.payload['details']['description'] == 'retrieval':
            all_roles = read_all_data(session,'role')
            
            if all_roles == None:
                response_data = input_data_structure_conversion(action='delivery',parameter_nested_list=[['message','There are no roles in db']])
                return response_data

            if all_roles != None:
                role_item_list = [f'{role.role_name}:[policies = {role.policies}]' for role in all_roles]
                #role_object_list = [[f'{role.role_name}:[service_id = {role.policies.service_id},uri = {role.policies.uri}, allowed_methods = {role.policies.allowed_methods}'] for role in all_roles]
                response_data = input_data_structure_conversion(action='delivery',parameter_nested_list=[['role_objects',role_item_list]])
                return response_data

        else:
            return 'task given in description does not exist'


    if payload.payload['action'] == 'update':
        pass



def authorization_function(payload):

    target_role_name  = payload.payload['details']['role_name']
    target_service_id  = payload.payload['details']['service_id']
    target_crud_action  = payload.payload['details']['crud_action']
    target_uri  = payload.payload['details']['uri']
    target_user_id  = payload.payload['details']['user_id']
    target_tenant_id  = payload.payload['details']['tenant_id']

    policy_id_request_payload = input_data_structure_conversion(action='get',parameter_nested_list=[['description','retrieve_policy_id'],['service_id',target_service_id],['crud_action',target_crud_action],['uri',target_uri]])
    policy_id_object = httpx.post(policy_url,json=policy_id_request_payload)


    if policy_id_object.json()['payload']['action'] == 'delivery':

        policy_object_roles_payload = input_data_structure_conversion(action='get',parameter_nested_list=[['description','roles'],['policy_id',policy_id_object.json()['payload']['details']['policy_id']]])
        policy_object_roles = httpx.post(policy_url,json=policy_object_roles_payload)

        policy_id_derived = policy_id_object.json()['payload']['details']['policy_id'] 
        policy_roles_derived = policy_object_roles.json()['payload']['details']['roles']

        if target_role_name in policy_roles_derived:
            target_allowed = True
            policy_based_reason = 'authorized'

            make_decision_log_payload = input_data_structure_conversion(action='create',parameter_nested_list=[['service_id',target_service_id],['user_id',target_user_id],['tenant_id',target_tenant_id],['crud_action',target_crud_action[0]],['allowed',target_allowed],['policy_based_reason',policy_based_reason]])
            make_decision_log = httpx.post(decision_log_url,json=make_decision_log_payload)

            return 'authorized'

        if target_role_name not in policy_roles_derived:
            target_allowed = False
            policy_based_reason = 'unauthorized'

            make_decision_log_payload = input_data_structure_conversion(action='create',parameter_nested_list=[['service_id',target_service_id],['user_id',target_user_id],['tenant_id',target_tenant_id],['crud_action',target_crud_action[0]],['allowed',target_allowed],['policy_based_reason',policy_based_reason]])
            make_decision_log = httpx.post(decision_log_url,json=make_decision_log_payload)

            return 'unauthorized'

        if len(policy_roles_derived) == 0:

            target_allowed = False
            policy_based_reason = 'suspicious'

            make_decision_log_payload = input_data_structure_conversion(action='create',parameter_nested_list=[['service_id',target_service_id],['user_id',target_user_id],['tenant_id',target_tenant_id],['crud_action',target_crud_action[0]],['allowed',target_allowed],['policy_based_reason',policy_based_reason]])
            make_decision_log = httpx.post(decision_log_url,json=make_decision_log_payload)

            return f'policy of id {policy_id_derived} has no roles'

    if policy_id_object.json()['payload']['action'] == 'not_found':
        return f'Service of id = {target_service_id} with crud action of = {target_crud_action} and uri of = {target_uri} is not assosiated with any policies'



def policy_function(payload):

    if payload.payload['action'] == 'create':
        inner_data_capsule = payload.payload['details']
        check_policy_existance_payload = input_data_structure_conversion(action='get',parameter_nested_list=[['description','existance'],['uri',inner_data_capsule['uri']],['service_id',inner_data_capsule['service_id']]])

        check_policy_existance = httpx.post(get_policy_url,json=check_policy_existance_payload)

        if check_policy_existance.json() == 'not_found':

            allowed_methods_transformed = transform_list_string_bidirectional(change_direction='turn_to_string',input_data_list=inner_data_capsule['allowed_methods'],mediator_char="_")
            make_policy = create_policy(inner_data_capsule['service_id'],inner_data_capsule['uri'],allowed_methods_transformed)
            create_policy_structured = input_data_structure_conversion(action='delivery',parameter_nested_list=[['policy_id',make_policy[0]['policy_id']]])

            return create_policy_structured

        if check_policy_existance.json() == 'found':
            uri_instance = inner_data_capsule['uri']
            service_instance = inner_data_capsule['service_id']
            duplicate_message = input_data_structure_conversion(action='duplicate',parameter_nested_list=[['message',f'policy with service= [{service_instance}] uri= [{uri_instance}] is duplicate']]) 
            return duplicate_message


    if payload.payload['action'] == 'get':
        esoteric_action = payload.payload['details']['description']
        
        if esoteric_action == 'existance':
            get_policy_data_by_service_id = read_data(session,'policy','service_id',payload.payload['details']['service_id'])

            if get_policy_data_by_service_id == None :
                return 'not_found'

            if get_policy_data_by_service_id != None:
                get_policy_bulk = read_all_data(session,'policy')
                uri_with_same_service_id = [] 

                for policy_row in get_policy_bulk:

                    if policy_row.service_id == payload.payload['details']['service_id']:
                        uri_with_same_service_id.append({'uri':policy_row.uri})

                for db_found_uri in uri_with_same_service_id:
                    print(f'db found uri = {db_found_uri}')
                    existing_uri_restructured = transform_list_string_bidirectional(change_direction='turn_to_list',input_data_list=[db_found_uri['uri']],mediator_char="/")
                    payload_uri_restructured = transform_list_string_bidirectional(change_direction='turn_to_list',input_data_list=[payload.payload['details']['uri']],mediator_char="/")

                    print(f'Existing uri restructured = {existing_uri_restructured}')
                    print(f'Payload uri restructured = {payload_uri_restructured}')


                    if len(existing_uri_restructured) == len(payload_uri_restructured):

                        path_count = 0 
                        similarity_count = []

                        while  path_count < len(existing_uri_restructured):
                            print(f'This is the path count = {path_count}')
                            if payload_uri_restructured[path_count] == existing_uri_restructured[path_count]:
                                similarity_count.append(f'similar_index : {path_count}')
                            
                            path_count += 1

                        if len(similarity_count) == len(payload_uri_restructured):
                            print(f'This is the found are with similarity = {similarity_count} and payload = {payload_uri_restructured}')
                            return 'found'

                return 'not_found'


        if esoteric_action == 'retrieve_policy_id':
            target_service_id = payload.payload['details']['service_id']
            target_uri = payload.payload['details']['uri']
            target_crud_action = payload.payload['details']['crud_action']

            policy_bulk_data = read_all_data(session,'policy')
            policy_id_capsule = []

            for policy_item in policy_bulk_data:
                allowed_methods_list_converted = transform_list_string_bidirectional(change_direction='turn_to_list',input_data_list=[policy_item.allowed_methods],mediator_char="_")
                if policy_item.service_id == target_service_id:
                    if target_crud_action[0] in allowed_methods_list_converted and policy_item.uri == target_uri:
                        policy_id_capsule.append(policy_item.policy_id)

            if len(policy_id_capsule) >= 1:
                policy_id_delivery = input_data_structure_conversion(action='delivery',parameter_nested_list=[['policy_id',policy_id_capsule[0]]])
                return policy_id_delivery

            if len(policy_id_capsule) == 0:
                policy_id_delivery = input_data_structure_conversion(action='not_found',parameter_nested_list=[])
                print(f'service of id = {target_service_id} with uri = {target_uri} with action = {target_crud_action} does not exist')
                return policy_id_delivery


        if esoteric_action == 'roles':
            policy_id_target = payload.payload['details']['policy_id']
            policy_object = read_data(session,'policy','policy_id',policy_id_target)

            response_roles_list_payload = input_data_structure_conversion(action='delivery',parameter_nested_list=[['roles',[role.role_name for role in policy_object.roles]]])
            return response_roles_list_payload


        if esoteric_action == 'retrieval':
            policies_bulk = read_all_data(session,'policy') 
            policy_dict_list = [{f'policy_id : {policy.policy_id}',f'service_id : {policy.service_id}',f'uri : {policy.uri}',f'allowed_methods : {policy.allowed_methods}',f'roles : {[role.role_name for role in policy.roles]}'} for policy in policies_bulk]
            response_data = input_data_structure_conversion(action='delivery',parameter_nested_list=[['policy_objects',policy_dict_list]])
            return response_data


    if payload.payload['action'] == 'update':

        if payload.payload['details']['description'] == 'roles':

            policy_id_target = payload.payload['details']['policy_id']
            role_name_target = payload.payload['details']['role_name']

            if payload.payload['details']['specification'] == 'add':
                print('one')
                check_role_existance_payload = input_data_structure_conversion(action='get',parameter_nested_list=[['description','existance'],['role_name',role_name_target]])
                role_existance_statement = httpx.post(role_url,json=check_role_existance_payload)

                policy_roles_retrival_payload = input_data_structure_conversion(action='get',parameter_nested_list=[['description','roles'],['policy_id',policy_id_target]])
                policy_roles_retrival = httpx.post(policy_url,json=policy_roles_retrival_payload)
                
                if role_existance_statement.json() == 'found':
                    print('two')
                    if role_name_target in policy_roles_retrival.json()['payload']['details']['roles']:
                        return f'role name = {role_name_target} already exists in policy of id = {policy_id_target}'

                    if len(policy_roles_retrival.json()['payload']['details']['roles']) == 0 or role_name_target not in policy_roles_retrival.json()['payload']['details']['roles']:
                        print('three')
                        connect_policy_role = create_link_btwn_policy_role(session,'policy_id',payload.payload['details']['policy_id'],'role_name',payload.payload['details']['role_name'])
                        return f'Finished linking policy_id [{policy_id_target}] to role_name [{role_name_target}]'

                if role_existance_statement.json() == 'not_found':
                    return f'The role name {role_name_target} does not exist in db'

            if payload.payload['details']['specification'] == 'remove':

                get_policy_object = read_data(session,'policy','policy_id',policy_id_target)
                get_role_object = read_data(session,'role','role_name',role_name_target)
                print(f'This is the old roles allowed = [{[role.role_name for role in get_policy_object.roles]}]')

                if [role.role_name for role in get_policy_object.roles] == None:
                    return f'policy of id {policy_id_target} does not have any roles'

                if [role.role_name for role in get_policy_object.roles] != None:

                    if get_role_object not in get_policy_object.roles:
                        return f'Policy of policy id = {policy_id_target} and Role name {role_name_target} are not associated'

                    if get_role_object in get_policy_object.roles:
                        get_policy_object.roles.remove(get_role_object)
                        session.commit()
                        return f'This is the new roles allowed = [{[role.role_name for role in get_policy_object.roles]}]'


        if payload.payload['details']['description'] == 'allowed_methods':

            method_change_payload = payload.payload['details']['method_change']
            policy_id_target = payload.payload['details']['policy_id']

            policy_object = read_data(session,'policy','policy_id',policy_id_target)
            policy_db_methods_list = transform_list_string_bidirectional(change_direction='turn_to_list',input_data_list=[policy_object.allowed_methods],mediator_char="_")

            if payload.payload['details']['specification'] == 'add':
                new_methods_to_add_list = []

                for method_item in method_change_payload:
                    if method_item not in policy_db_methods_list:
                        new_methods_to_add_list.append(method_item)

                print(f'This is the db allowed actions = {policy_db_methods_list}') 
                print(f'This is the new methods to add list = {new_methods_to_add_list}') 

                if len(new_methods_to_add_list) == 0:
                    return f'all the input methods to add are already existant = {policy_db_methods_list}' 

                if len(new_methods_to_add_list) >= 1:

                    combined_old_new_list = new_methods_to_add_list + policy_db_methods_list
                    new_policy_allowed_methods_string = transform_list_string_bidirectional(change_direction='turn_to_string',input_data_list=combined_old_new_list,mediator_char="_")

                    policy_object.allowed_methods = new_policy_allowed_methods_string
                    session.commit()

                    print(f'This is the new policy allowed string = {new_policy_allowed_methods_string}') 
                    return f'new allowed methods for policy of id = {policy_id_target} has allowed methods = {policy_object.allowed_methods}'

            if payload.payload['details']['specification'] == 'remove':
                new_methods_allowed = []
                method_existance_in_db_list = []

                for method_item in policy_db_methods_list:

                    if method_item not in method_change_payload:
                        new_methods_allowed.append(method_item)

                    if method_item in method_change_payload:
                        method_existance_in_db_list.append(method_item)
                    

                if len(method_existance_in_db_list) == 0:
                    return f'all the input methods to are non existant for policy of id = {policy_id_target}' 

                if len(method_existance_in_db_list) >= 1:
                    new_policy_allowed_methods_string = transform_list_string_bidirectional(change_direction='turn_to_string',input_data_list=new_methods_allowed,mediator_char="_")
                    policy_object.allowed_methods = new_policy_allowed_methods_string
                    session.commit()
                    return f'new allowed methods for policy of id = {policy_id_target} has allowed methods = {policy_object.allowed_methods}'




def decision_log_function(payload):

    if payload.payload['action'] == 'create':

        target_service_id = payload.payload['details']['service_id']
        target_user_id = payload.payload['details']['user_id']
        target_tenant_id = payload.payload['details']['tenant_id']
        target_crud_action = payload.payload['details']['crud_action']
        target_allowed = payload.payload['details']['allowed']
        policy_based_reason = payload.payload['details']['policy_based_reason']

        print(f'new_decision_payload = {payload}')
        new_decision_log = create_decision_log(user_id_input=target_user_id,tenant_id_input=target_tenant_id,service_id_input=target_service_id,crud_action_input=target_crud_action,allowed_input=target_allowed,policy_based_reason_input=policy_based_reason)
        new_decision_log_id = new_decision_log['decision_id']
        print(f'Decision logged of id = {new_decision_log_id}')
        

    if payload.payload['action'] == 'get':

        decision_log_bulk = read_all_data(session,'decision_log')
        decision_log_output_transformation = input_data_structure_conversion(action='delivery',parameter_nested_list=['decision_logs',decision_log_bulk])
        
        return decision_log_output_transformation
        



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
