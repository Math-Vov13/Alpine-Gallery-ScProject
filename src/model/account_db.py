# API
# Mathéo Vovard

import secrets
from typing import Optional

from schemas.account import *
from Core.Config import CONFIG

fakedb : list[Account_Schema_DB] = []



async def is_account_already_exists(email: str) -> bool:
    for acc in fakedb:
        if acc.email == email:
            return True
    return False

async def create_account(form: RegisterModel) -> RegisterModel:
    if len(fakedb) >= CONFIG.MAX_ACCOUNT:
        return "Max account limit reached! (5)"
    
    if await is_account_already_exists(email= form.email):
        return "This email is already used!"

    fakedb.append(Account_Schema_DB(
        id=len(fakedb),
        name= form.name,
        email= form.email,
        password= form.password))
    
    return form


async def get_account(form: LoginModel) -> Optional[Account_Schema_DB]:
    for acc in fakedb:
        
        is_correct_email = secrets.compare_digest(
            form.email, acc.email
        )
        is_correct_password = secrets.compare_digest(
            form.password, acc.password
        )

        if is_correct_email and is_correct_password:
            return acc