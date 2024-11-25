# API
# Mathéo Vovard

import secrets
from typing import Optional

from schemas.account import *

fakedb : list[Account_Schema_DB] = []



async def create_account(form: RegisterModel) -> RegisterModel:
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