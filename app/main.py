from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.settings.config import get_settings
from app.models.remote_request_model import RemoteRequestModel
from app.session import get_session_manager
import requests

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
    return get_settings().to_dict()

@app.post("/remoteRequest")
def remote_request(request: RemoteRequestModel):
    url = request.remote_url
    method = request.remote_method
    data = request.remote_data
    print( f"url={url}, method={method}, data={data}" )

    session = get_session_manager().get_session()
    try:
        res = session.post(
            url,
            json = data,
        )
    except requests.exceptions.RequestException as e:
        return {
            "status": 500,
            "data": str(e),
        }

    return {
        "status": 200,
        "data": {
            "remote_status": res.status_code,
            "remote_data": res.json(),
        },
    }
