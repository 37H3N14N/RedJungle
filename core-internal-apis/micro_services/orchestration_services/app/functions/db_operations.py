from sqlalchemy import update, delete
import uuid

from databank.orchestration_db_initialization import get_session
from databank.orchestration_db_initialization import Workflow_Object
from databank.orchestration_db_initialization import Step_Object
from databank.orchestration_db_initialization import Sub_Workflow_Object
from databank.orchestration_db_initialization import Service_Object
from databank.orchestration_db_initialization import Progress_Object


###################################################################
session = get_session()

###################################################################

def get_uuid4():
    random_uuid = uuid.uuid4()
    return random_uuid

###################################################################

def create_workflow(workflow_name_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    workflow_item = Workflow_Object(
        workflow_id= constant_uuid[0],
        workflow_name= workflow_name_input
        )

    response_data.append({'workflow_id': f'{constant_uuid[0]}'})

    session.add(workflow_item)
    session.commit()
    session.close()

    return response_data

############################################################################

def create_step(service_id_input,relative_uri_input,request_type_input,execution_order_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    step_item = Step_Object(
        step_id= constant_uuid[0],
        service_id= service_id_input,
        relative_uri= relative_uri_input,
        request_type= request_type_input,
        execution_order= execution_order_input
        )

    response_data.append({'step_id': f'{constant_uuid[0]}'})

    session.add(step_item)
    session.commit()
    session.close()

    return response_data

###################################################################

def create_sub_workflow(assistance_workflow_id_input,execution_order_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    sub_workflow_item = Sub_Workflow_Object(
        sub_workflow_id= constant_uuid[0],
        assistance_workflow_id= assistance_workflow_id_input,
        execution_order= execution_order_input
        )

    response_data.append({'sub_workflow_id': f'{constant_uuid[0]}'})

    session.add(sub_workflow_item)
    session.commit()
    session.close()

    return response_data

###################################################################

def create_service(service_name_input,endpoint_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    service_item = Service_Object(
        service_id= constant_uuid[0],
        service_name= service_name_input,
        endpoint= endpoint_input
        )

    response_data.append({'service_id': f'{constant_uuid[0]}'})

    session.add(service_item)
    session.commit()
    session.close()

    return response_data

###################################################################

def create_progress(workflow_id_input,current_step_no_input,progress_status_input,complete_status_input):
    constant_uuid = []
    constant_uuid.append(get_uuid4())
    response_data = []

    progress_item = Progress_Object(
        progress_id= constant_uuid[0],
        workflow_id= workflow_id_input,
        current_step_no= current_step_no_input,
        progress_status= progress_status_input,
        complete_status= complete_status_input
        )

    response_data.append({'progress_id': f'{constant_uuid[0]}'})

    session.add(progress_item)
    session.commit()
    session.close()

    return response_data

###################################################################

def create_link_btwn_sub_workflow_workflow(db_session,sub_workflow_column_name,sub_workflow_row_identifier,workflow_column_name,workflow_row_identifier):

    target_workflow = read_data(db_session,'workflow',workflow_column_name,workflow_row_identifier)
    target_sub_workflow = read_data(db_session,'sub_workflow',sub_workflow_column_name,sub_workflow_row_identifier)

    target_workflow.sub_workflows.append(target_sub_workflow)

    db_session.commit()
    db_session.close()
    return


def create_link_btwn_workflow_steps(db_session,step_column_name,step_row_identifier,workflow_column_name,workflow_row_identifier):

    target_workflow = read_data(db_session,'workflow',workflow_column_name,workflow_row_identifier)
    target_step = read_data(db_session,'step',step_column_name,step_row_identifier)

    target_step.workflows.append(target_workflow)

    db_session.commit()
    db_session.close()
    return

############################################################################

def read_data(db_session,target_model_class,column_name,row_identifier):

    if target_model_class == 'workflow':
        column = getattr(Workflow_Object,column_name)
        target_item = db_session.query(Workflow_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'sub_workflow':
        column = getattr(Sub_Workflow_Object,column_name)
        target_item = db_session.query(Sub_Workflow_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'step':
        column = getattr(Step_Object,column_name)
        target_item = db_session.query(Step_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'service':
        column = getattr(Service_Object,column_name)
        target_item = db_session.query(Service_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'progress':
        column = getattr(Progress_Object,column_name)
        target_item = db_session.query(Progress_Object).filter(column == f'{row_identifier}').first()
        return target_item

############################################################################

def update_data(db_session,target_model_class,identifying_column_name,identifying_row_entity,target_column_to_change,new_value_of_cell):

    if target_model_class == 'workflow':

        identify_column = getattr(Workflow_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Workflow_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


    if target_model_class == 'step':

        identify_column = getattr(Step_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Step_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


    if target_model_class == 'sub_workflow':

        identify_column = getattr(Sub_Workflow_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Sub_Workflow_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


    if target_model_class == 'service':

        identify_column = getattr(Service_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Service_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


    if target_model_class == 'progress':

        identify_column = getattr(Progress_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Progress_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 



############################################################################

def delete_data(db_session,main_id,target_model_class):

    if target_model_class == 'workflow':
        target_item = db_session.query(Workflow_Object).filter(Workflow_Object.workflow_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 


    if target_model_class == 'step':
        target_item = db_session.query(Step_Object).filter(Step_Object.step_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 

    if target_model_class == 'sub_workflow':
        target_item = db_session.query(Sub_Workflow_Object).filter(Sub_Workflow_Object.sub_workflow_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 

    if target_model_class == 'service':
        target_item = db_session.query(Service_Object).filter(Service_Object.service_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 

    if target_model_class == 'progress':
        target_item = db_session.query(Progress_Object).filter(Progress_Object.progress_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 

############################################################################

def read_all_data(db_session,table_name):

    if table_name == 'workflow':
        res_data = db_session.query(Workflow_Object).all()
        return res_data

    if table_name == 'step':
        res_data = db_session.query(Step_Object).all()
        return res_data

    if table_name == 'sub_workflow':
        res_data = db_session.query(Sub_Workflow_Object).all()
        return res_data

    if table_name == 'service':
        res_data = db_session.query(Service_Object).all()
        return res_data

    if table_name == 'progress':
        res_data = db_session.query(Progress_Object).all()
        return res_data


############################################################################

def delete_all_data(table_name):

    if table_name == 'workflow':
        all_rows = delete(Workflow_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'step':
        all_rows = delete(Step_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'sub_workflow':
        all_rows = delete(Sub_Workflow_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'service':
        all_rows = delete(Service_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'progress':
        all_rows = delete(Progress_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

############################################################################


#create_workflow('work1','workflow_one')
#create_workflow('work2','workflow_two')
#create_workflow('work3','workflow_three')
#create_workflow('work4','workflow_four')
#create_workflow('work5','workflow_five')
#
#create_service('service1','service_name_one','endpoint/1')
#create_service('service2','service_name_two','endpoint/2')
#create_service('service3','service_name_three','endpoint/3')
#create_service('service4','service_name_four','endpoint/4')
#create_service('service5','service_name_five','endpoint/5')
#
#create_sub_workflow('sub1','work1',5)
#create_sub_workflow('sub2','work2',4)
#create_sub_workflow('sub3','work3',3)
#create_sub_workflow('sub4','work4',2)
#create_sub_workflow('sub5','work5',1)
#
#create_step('step1','service3','/something/three','post',3)
#create_step('step2','service1','/something/one','delete',1)
#create_step('step3','service4','/something/four','put',4)
#create_step('step4','service2','/something/two','get',2)
#create_step('step5','service5','/something/five','post',5)


#create_link_btwn_sub_workflow_workflow(session,'sub_workflow_id','sub1','workflow_id','work3')
#create_link_btwn_sub_workflow_workflow(session,'sub_workflow_id','sub2','workflow_id','work3')
#create_link_btwn_sub_workflow_workflow(session,'sub_workflow_id','sub3','workflow_id','work5')
#
#create_link_btwn_workflow_steps(session,'step_id','step1','workflow_id','work3')
#create_link_btwn_workflow_steps(session,'step_id','step2','workflow_id','work5')
#create_link_btwn_workflow_steps(session,'step_id','step3','workflow_id','work5')
#create_link_btwn_workflow_steps(session,'step_id','step4','workflow_id','work5')
#create_link_btwn_workflow_steps(session,'step_id','step5','workflow_id','work3')




#data_one = read_all_data(session,'workflow')
#
#for workflow_item in  data_one:
#    print('//////////////// START ///////////////////')
#    print(workflow_item.workflow_name)
#    for step_item in workflow_item.steps:
#        print(step_item.step_id,step_item.service_id,step_item.relative_uri,step_item.request_type,step_item.execution_order)
#    for sub_work in workflow_item.sub_workflows:
#        print(sub_work.sub_workflow_id,sub_work.assistance_workflow_id,sub_work.execution_order)
#        print('///////////////////////////')
#        for work in sub_work.workflows:
#            print(work.workflow_name)
#








