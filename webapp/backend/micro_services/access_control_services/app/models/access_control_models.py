from pydantic import BaseModel


class Policy_Object(BaseModel):
    policy_id: str
    service_id: str
    uri: str
    allowed_methods: str
    roles: list


class Role_Object(BaseModel):
    role_id: str
    role_name: str
    policies: list


class Decision_Log_Object(BaseModel):
    decision_id: str
    user_id: str
    tenant_id: str
    service_id: str
    crud_action: str
    allowed: bool 
    policy_based_reason: str
    timestamp: str


class Incoming_Data(BaseModel):
    server_authorization_token: str
    payload: dict


class Send_Log_Data(BaseModel):
    source_service: str
    service_uri: str
    action_crud: str
    user_id: str
    tenant_id: str
    details: dict









