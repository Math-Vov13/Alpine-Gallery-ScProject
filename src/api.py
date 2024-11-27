from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from src.endpoints.account import router as routerAcc
from src.endpoints.gallery import router as routerGall
from src.endpoints.middlewares.auth import router as routerAuth
from src.model.account_db import account_db
from src.model.media_db import media_db

subapp = FastAPI(root_path="/api/v1", root_path_in_servers="/api/v1")


@subapp.get("/")
def index():
    return RedirectResponse(
        url="/"  # Redirection to the website
    )

@subapp.get("/accounts", description="see all accounts")
def get_accounts():
    return account_db.get_all_accounts()

@subapp.get("/files", description= "see all files stored in the server")
def get_files():
    return media_db.get_all_files()

subapp.include_router(router= routerAcc)
subapp.include_router(router= routerGall)
subapp.include_router(router= routerAuth)