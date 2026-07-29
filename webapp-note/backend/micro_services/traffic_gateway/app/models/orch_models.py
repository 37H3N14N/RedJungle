from pydantic import BaseModel


class Workflow_Object(BaseModel):
    workflow_id: str
    workflow_name:str
    sub_workflows:list
    steps: list


class Step_Object(BaseModel):
    step_id: str
    service_id: str
    relative_uri: str
    request_type: str
    execution_order: int
    workflows: list


class Sub_Workflow_Object(BaseModel):
    sub_workflow_id: str
    assistance_workflow_id: str
    execution_order: int
    workflows:list


class Service_Object(BaseModel):
    service_id: str
    service_name: str
    endpoint: str


class Progress_Object(BaseModel):
    progress_id: str
    workflow_id: str
    current_step_no: str
    progress_status: str
    complete_status: str


class Send_Log_Data(BaseModel):
    source_service: str
    service_uri: str
    action_crud: str
    user_id: str
    tenant_id: str
    details: dict


class Incoming_Data_External(BaseModel):
    workflow_name: str
    authorization_data: dict
    payload: dict


class Incoming_Data_Internal(BaseModel):
    server_authorization_token: str
    status: str
    payload: dict








