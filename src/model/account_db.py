# API
# Mathéo Vovard

from pydantic import BaseModel

fakedb = []

class account(BaseModel):
    name: str
    email: str
    password: str

async def create_account(form: account) -> account:
    fakedb.append(form)
    return form

async def get_account(form):
    for acc in fakedb:
        if form.email == acc.email and form.password == acc.password:
            return True
    return False