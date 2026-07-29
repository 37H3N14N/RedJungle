from pydantic import BaseModel

class Transaction_Object(BaseModel):
    transaction_id: str
    user_id: str
    tenant_id: str
    card_number: int
    amount: float
    created_at: str


class Bank_Object(BaseModel):
    bank_id: str
    bank_name: str
    accounts: list


class Account_Object(BaseModel):
    account_id: str
    bank_id: str
    card_number: int
    account_balance: float
    updated_at: str
    customers: list
    banks: list


class Customer_Object(BaseModel):
    customer_id: str
    user_id: str
    accounts: list


class Incoming_Data(BaseModel):
    server_authorization_token: str
    payload: dict





