
from typing import Dict, List
from datetime import datetime
from .models import UserModel, AccountModel, TransactionModel


class InMemoryDB:
    def __init__(self):
        self.users: Dict[int, UserModel] = {}
        self.accounts: Dict[int, AccountModel] = {}
        self.transactions: Dict[int, TransactionModel] = {}
        self.user_seq = 0
        self.account_seq = 0
        self.transaction_seq = 0

    async def create_user(self, username: str, password_hash: str) -> UserModel:
        self.user_seq += 1
        user = UserModel(id=self.user_seq, username=username, password_hash=password_hash)
        self.users[user.id] = user
        return user

    async def get_user_by_username(self, username: str):
        return next((u for u in self.users.values() if u.username == username), None)

    async def get_user(self, user_id: int):
        return self.users.get(user_id)

    async def create_account(self, user_id: int, name: str) -> AccountModel:
        self.account_seq += 1
        account = AccountModel(id=self.account_seq, user_id=user_id, name=name, balance=0.0)
        self.accounts[account.id] = account
        return account

    async def get_account(self, account_id: int):
        return self.accounts.get(account_id)

    async def get_user_accounts(self, user_id: int) -> List[AccountModel]:
        return [a for a in self.accounts.values() if a.user_id == user_id]

    async def update_account_balance(self, account_id: int, balance: float):
        acc = self.accounts.get(account_id)
        if acc:
            acc.balance = balance
        return acc

    async def create_transaction(self, account_id: int, type_: str, amount: float) -> TransactionModel:
        self.transaction_seq += 1
        tx = TransactionModel(
            id=self.transaction_seq,
            account_id=account_id,
            type=type_,
            amount=amount,
            timestamp=datetime.utcnow(),
        )
        self.transactions[tx.id] = tx
        return tx

    async def get_account_transactions(self, account_id: int) -> List[TransactionModel]:
        return [t for t in self.transactions.values() if t.account_id == account_id]

db = InMemoryDB()