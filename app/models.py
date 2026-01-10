from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserModel:
    id: int
    username: str
    password_hash: str


@dataclass
class AccountModel:
    id: int
    user_id: int
    name: str
    balance: float


@dataclass    
class TransactionModel:
    id: int
    account_id: int
    amount: float
    timestamp: datetime
