from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from endpoints.account import router as routerAcc
from endpoints.gallery import router as routerGall


app = FastAPI(root_path="/api/v1", root_path_in_servers="/api/v1")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)


@app.get("/")
def index():
    return RedirectResponse(
        url="/index.html"  # Redirection to the website
    )



app.mount("/static", StaticFiles(directory= "model\storage"), name="static")
app.include_router(router= routerAcc)
app.include_router(router= routerGall)