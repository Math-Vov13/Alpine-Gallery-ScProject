from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from src.endpoints.account import router as routerAcc
from src.endpoints.gallery import router as routerGall
from src.endpoints.middlewares.auth import router as routerAuth

subapp = FastAPI(root_path="/api/v1", root_path_in_servers="/api/v1")


@subapp.get("/")
def index():
    return RedirectResponse(
        url="/"  # Redirection to the website
    )


subapp.include_router(router= routerAcc)
subapp.include_router(router= routerGall)
subapp.include_router(router= routerAuth)