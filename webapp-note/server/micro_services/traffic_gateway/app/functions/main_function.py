from databank.orchestration_schema_data.workflow_data import workflow_object
from databank.orchestration_schema_data.service_data import service_object
from databank.orchestration_schema_data.step_data import step_object
from databank.orchestration_schema_data.sub_workflow_data import sub_workflow_object
from databank.orchestration_db_initialization import get_session

from functions.db_operations import create_workflow
from functions.db_operations import create_step
from functions.db_operations import create_sub_workflow
from functions.db_operations import create_service
from functions.db_operations import get_uuid4
from functions.db_operations import read_data
from functions.db_operations import read_all_data
from functions.db_operations import delete_all_data

from functions.db_operations import create_link_btwn_sub_workflow_workflow
from functions.db_operations import create_link_btwn_workflow_steps

import yaml
import httpx 


################ POPULATE ORCHESTRATION DB PERSISTENT INFO ###################
def enumerate_steps_data_then_send_to_db():
    current_session = get_session()

    print('[START WRITTING STEPS TO DB]')
    for step_item in step_object:

        get_workflow_name = get_local_workflow_name_by_id(step_item['workflow_id'])
        workflow_db_instance = read_data(current_session,'workflow','workflow_name',get_workflow_name)
        workflow_db_instance_id = workflow_db_instance.workflow_id

        service_item_name = get_local_service_name_by_id(step_item['service_id'])
        service_db_find = read_data(current_session,'service','service_name',service_item_name)
        service_id_db = service_db_find.service_id

        new_step_id = create_step(service_id_db,step_item['relative_url'],step_item['request_type'],step_item['execution_order'])
        create_link_btwn_workflow_steps(current_session,'step_id',new_step_id,'workflow_id',workflow_db_instance_id)
        current_session.close()

    print('[DONE WRITTING STEPS TO DB]')

#####################
def enumerate_sub_workflows_data_then_send_to_db():

    current_session = get_session()

    print('[START WRITTING SUB WORKFLOWS TO DB]')
    for sub_work in sub_workflow_object:
        get_workflow_name = get_local_workflow_name_by_id(sub_work['master_workflow_id'])
        workflow_db_instance = read_data(current_session,'workflow','workflow_name',get_workflow_name)
        workflow_db_instance_id = workflow_db_instance.workflow_id

        assistant_workflow_name = get_local_workflow_name_by_id(sub_work['assistance_workflow_id'])
        assistance_workflow_db_find = read_data(current_session,'workflow','workflow_name',assistant_workflow_name)
        assistance_workflow_id_db = assistance_workflow_db_find.workflow_id

        new_sub_workflow_id = create_sub_workflow(assistance_workflow_id_db,sub_work['execution_order'])
        create_link_btwn_sub_workflow_workflow(current_session,'sub_workflow_id',new_sub_workflow_id,'workflow_id',workflow_db_instance_id) 
        current_session.close()
        
    print('[DONE WRITTING SUB WORKFLOWS TO DB]')

#####################
def enumerate_workflow_data_then_send_to_db():
    print('[START WRITTING WORKFLOW TO DB]')
    for workflow_item in workflow_object:
        create_workflow(workflow_item['workflow_name'])
    print('[DONE WRITTING WORKFLOW TO DB]')

#####################
def enumerate_services_data_then_send_to_db():
    print('[START WRITTING SERVICES TO DB]')
    for service_item in service_object:
        create_service(service_item['service_name'],service_item['endpoint'])
    print('[DONE WRITTING SERVICES TO DB]')

######################
def get_local_workflow_name_by_id(workflow_id):
    for workflow_item in workflow_object:
        if workflow_item['workflow_id'] == workflow_id:
            return workflow_item['workflow_name']

#####################
def get_local_service_name_by_id(service_id):
    for service_item in service_object:
        if service_item['service_id'] == service_id:
            return service_item['service_name']

#####################
def complete_migration_of_orchestration_data_to_db():
   enumerate_services_data_then_send_to_db()
   enumerate_workflow_data_then_send_to_db()
   enumerate_steps_data_then_send_to_db()
   enumerate_sub_workflows_data_then_send_to_db()


#complete_migration_of_orchestration_data_to_db()
#delete_all_data('service')


##################### GENERAL FUNCTIONS ##########################
def load_yaml_config(filepath):
    with open(filepath, 'r') as f:
        config = yaml.safe_load(f)
    return config


########################################################################
def steps_detail_info(list_step):
    enumeration_list = []

    for step in list_step:
            step_execution_order = step.execution_order
            step_relative_uri = step.relative_uri
            step_request_type = step.request_type
            service_port = service.endpoint

            enumeration_list.append({
                'execution_order': step_execution_order,
                'uri': f'{service_port}{step_relative}',
                'request_type': step_request_type
                })

    return enumeration_list


############## TRANSFORM DB STEPS & SUB WORKFLOWS TO ORDERED STEPS ONLY ##################
global_ordered_steps = []

def raw_db_workflow_steps_sub_workflows_to_arranged_steps(main_steps,main_sub_work):
    current_session = get_session()
    ordered_step_list = []

    original_length_steps = len(main_steps) + len(main_sub_work)
    current_original_length_iteration = 0

    while current_original_length_iteration < original_length_steps:

        for step_item in main_steps:
            if step_item.execution_order == current_original_length_iteration + 1:
                ordered_step_list.append(step_item)

        for sub_work_item in main_sub_work:

            if sub_work_item.execution_order == current_original_length_iteration + 1:
                if sub_work_item.assistance_workflow_id:
                    get_workflow_db_instance = read_data(current_session,'workflow','workflow_id',sub_work_item.assistance_workflow_id) 
                    raw_db_workflow_steps_sub_workflows_to_arranged_steps(get_workflow_db_instance.steps,get_workflow_db_instance.sub_workflows)

        current_original_length_iteration += 1

    global_ordered_steps.append(ordered_step_list[0])
    current_session.close()
    return ordered_step_list


################### WORKFLOW NAME TO COMPLETE ORDERED STEPS #######################
def workflow_name_to_ordered_steps_linkage(given_name):
    current_session = get_session()
    workflow_instance= read_data(current_session,'workflow','workflow_name',given_name) 
    
    if workflow_instance:
        main_steps = workflow_instance.steps
        main_sub_workflow = workflow_instance.sub_workflows
        raw_db_workflow_steps_sub_workflows_to_arranged_steps(main_steps,main_sub_workflow)

    current_session.close()
    return global_ordered_steps
    

#workflow_name_to_ordered_steps_linkage('create_room')


######################## FULL INTER API COMMUNICATION ###############################
def full_transactional_api_communication(structured_step_list,initial_payload):

    current_session = get_session()
    response_data_bank = []
    current_step_index = 0

    while current_step_index < len(structured_step_list):

        current_target_relative_uri = structured_step_list[current_step_index].relative_uri
        current_target_service= read_data(current_session,'service','service_id',structured_step_list[current_step_index].service_id)
        current_service_endpoint = current_target_service.endpoint
        http_request_type = structured_step_list[current_step_index].request_type

        complete_url = f'http://localhost:{current_service_endpoint}{current_target_relative_uri}'

        if current_step_index == 0:
            response_data_from_api = singular_api_data_communication(http_request_type,complete_url,initial_payload)
            response_data_bank.append(response_data_from_api)
            print(response_data_from_api)

        if current_step_index > 0:

            next_api_for_communication = response_data_bank[current_step_index - 1]
            previous_api_for_info = next_api_for_communication['payload']['endpoint_touched']

            response_data_from_api = singular_api_data_communication(http_request_type,complete_url, next_api_for_communication)
            response_data_from_api['payload']['previous_endpoint'] = previous_api_for_info

            print(response_data_from_api)
            response_data_bank.append(response_data_from_api)

        current_step_index += 1

    current_session.close()
    return response_data_bank


################ INDIVIDUAL API COMMUNICATION BASED ON REQUEST TYPE ###################
def singular_api_data_communication(http_request_type,complete_url,payload):

    if http_request_type == 'post':
        data = httpx.post(complete_url, json=payload)

        data_one = data.json()
        endpoint_name = data_one['endpoint']
        response_data = data_restructurization_for_target_endpoint_model('server_to_server')

        response_data['payload']['endpoint_touched'] = data_one['endpoint']
        response_data['server_authorization_token'] = complete_url

        return response_data


    if http_request_type == 'put':
        data = httpx.put(complete_url, json=payload)

        data_one = data.json()
        endpoint_name = data_one['endpoint']
        response_data = data_restructurization_for_target_endpoint_model('server_to_server')

        response_data['payload']['endpoint_touched'] = data_one['endpoint']
        response_data['server_authorization_token'] = complete_url

        return response_data


    if http_request_type == 'delete':

        payload_data = {
            "server_authorization_token":"authorized token",
            "target_object_id":'target object id to delete',
            "JWT":'user JWT'
            }

        data = httpx.delete(complete_url, data=payload)

        data_one = data.json()
        endpoint_name = data_one['endpoint']
        response_data = data_restructurization_for_target_endpoint_model('server_to_server')

        response_data['payload']['endpoint_touched'] = data_one['endpoint']
        response_data['server_authorization_token'] = complete_url
        print(response_data)

        return response_data


def data_restructurization_for_target_endpoint_model(type_of_parties):

    if type_of_parties == 'client_to_general_server':
        pass

    if type_of_parties == 'orch_to_acs':
        pass

    if type_of_parties == 'server_to_server':
        response_data = {
            'server_authorization_token': '',
            'payload': {
                "endpoint_touched" : ''
                }
            }
        return response_data



#########################################################################
data_input_initial = {
        "server_authorization_token": "transient_token_for_this_transaction",
        "payload": {
            "JWT":"YTJJFMDGMSDFGMSGFSKLGFFGSLJFGKSJF",
            "data":{
                "data_one":"something",
                "data_two":"someone"
            }
        }
    }


structured_steps_data = workflow_name_to_ordered_steps_linkage('create_booking')
full_transactional_api_communication(structured_steps_data,data_input_initial)











