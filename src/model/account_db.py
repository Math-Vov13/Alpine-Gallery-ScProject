# API
# Mathéo Vovard

import secrets
from typing import Optional

from src.schemas.account import *
from src.Core.Config import CONFIG

fakedb : list[Account_Schema_DB] = []



class account_db:

    @staticmethod
    async def is_account_already_exists(email: str) -> bool:
        for acc in fakedb:
            if acc.email == email:
                return True
        return False


    @staticmethod
    async def create_account(form: RegisterModel) -> RegisterModel:
        if len(fakedb) >= CONFIG.MAX_ACCOUNT:
            return f"Max account limit reached! ({CONFIG.MAX_ACCOUNT})"
        
        if await account_db.is_account_already_exists(email= form.email):
            return "This email is already used!"
        
        if len(form.name) > CONFIG.MAX_ACCOUNT_NAME_CHARS:
            return f"Max characters reached for the name! ({CONFIG.MAX_ACCOUNT_NAME_CHARS})"

        fakedb.append(Account_Schema_DB(
            id=len(fakedb),
            name= form.name,
            email= form.email,
            password= form.password))
        
        return form

    @staticmethod
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