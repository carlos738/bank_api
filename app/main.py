
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from .schemas import (
    Token, UserCreate, User, AccountCreate, Account,
    TransactionCreate, Transaction, Statement
)
from .storage import db
from .utils import hash_password, verify_password
from .auth import create_access_token, get_current_user

app = FastAPI(
    title="API Bancária Assíncrona",
    description="API para depósitos, saques e extrato de contas correntes com JWT e FastAPI.",
    version="1.0.0",
)


@app.post("/auth/signup", response_model=User, tags=["Auth"])
async def signup(payload: UserCreate):
    existing = await db.get_user_by_username(payload.username)
    if existing:
        raise HTTPException(status_code=400, detail="Usuário já existe")
    user = await db.create_user(payload.username, hash_password(payload.password))
    return User(id=user.id, username=user.username)


@app.post("/auth/token", response_model=Token, tags=["Auth"])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await db.get_user_by_username(form_data.username)
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
    access_token = create_access_token(data={"sub": user.username})
    return Token(access_token=access_token)


@app.post("/accounts", response_model=Account, tags=["Contas"])
async def create_account(payload: AccountCreate, current_user=Depends(get_current_user)):
    account = await db.create_account(user_id=current_user.id, name=payload.name)
    return Account(id=account.id, user_id=account.user_id, name=account.name, balance=account.balance)


@app.get("/accounts", response_model=List[Account], tags=["Contas"])
async def list_accounts(current_user=Depends(get_current_user)):
    accounts = await db.get_user_accounts(current_user.id)
    return [Account(id=a.id, user_id=a.user_id, name=a.name, balance=a.balance)for a in accounts]

