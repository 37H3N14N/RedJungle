from pydantic import BaseModel


class Credential_Object(BaseModel):
    credential_id: str
    user_id: str
    email: str
    hashed_password: str
    salt: str
    mfa_secret: str
    last_login_at: str
    failed_login_attempts: int

    reset_tokens: list


class Session_Object(BaseModel):
    session_id: str
    token_hash: str
    expires_at: str
    ip_address: str


class Password_Reset_Token_Object(BaseModel):
    token_id: str
    token: str
    expires_at: str
    is_used: bool
    credentials: list


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



