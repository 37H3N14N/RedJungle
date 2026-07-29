from pydantic import BaseModel

class Tenant_Object(BaseModel):
    tenant_id: str
    tenant_name: str
    super_admin_user_id: str
    subscription_plan: str
    status: str
    created_at: str
    billings: list


class Billing_Object(BaseModel):
    billing_id: str
    next_payment_after_days: int
    total_amount: float
    payment_transaction_id: str
    created_at: str
    tenants: list
    

class Send_Log_Data(BaseModel):
    source_service: str
    service_uri: str
    action_crud: str
    user_id: str
    tenant_id: str
    details: dict


class Incoming_Data(BaseModel):
    server_authorization_token: str
    payload: dict



