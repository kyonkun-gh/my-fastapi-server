from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.settings.config import get_settings
from app.models.request_model import RequestModel
import requests
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello FastAPI with Uvicorn!"}

@app.get("/env")
def get_env():
    settings = get_settings()
    return {
        "app_name": settings.app_name,
        "app_version": settings.app_version,
        "app_mode": settings.app_mode,
        "port": settings.port,
        "reload": settings.reload,
        "database_url": settings.database_url
    }

@app.post("/remoteRequest")
def remote_request(request: RequestModel):
    url = request.url
    method = request.method
    data = request.data
    print( f"url={url}, method={method}, data={data}" )
    
    try:
        json_data = json.loads(data)
    except json.JSONDecodeError:
        return {
            "status": 400,
            "error": "Invalid JSON"
        }
    
    for key, value in json_data.items():
        print(f"Key: {key}, Value: {value}")
    
    session = requests.Session()
    settings = get_settings()
    if settings.http_proxy != "" and settings.https_proxy != "":
        session.proxies = {
            "http": settings.http_proxy,
            "https": settings.https_proxy,
        }
        print( f"Proxy ON!!" )

    try:
        res = session.post(
            url,
            json = json_data,
        )
    except requests.exceptions.RequestException as e:
        return {
            "status": 500,
            "error": str(e)
        }

    return {
        "status": res.status_code, 
        "data": res.json(),
    }
