from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, condecimal


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    username: Optional[str] = None


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)

    password: str = Field(..., min_length=6, max_length=128)


class User(BaseModel):
    id: int

    username: str


class AccountCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)


class Account(BaseModel):
    id: int
    user_id: int
    name: str
    balance: float


class TransactionCreate(BaseModel):
    type: str = Field(..., pattern="^(deposit|withdraw)$")  # Alterado regex para pattern
    amount: condecimal(gt=0)


class Transaction(BaseModel):
    id: int
    account_id: int
    type: str
    amount: float
    timestamp: datetime


class Statement(BaseModel):
    account: Account
    transactions: List[Transaction]
