from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api import subapp


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)

templates = Jinja2Templates("..\client")


@app.get("/")
def index(request : Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


app.mount("/css", StaticFiles(directory= "..\client\css"), name="static")
app.mount("/api/v1", subapp)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app:app",
        host    = "0.0.0.0",
        port    = 8036, 
        reload  = True
    )