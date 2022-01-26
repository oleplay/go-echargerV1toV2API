# To run this fastapi app:
# $ python3 main.py
#
# To run this fastapi app with uvicorn:
# $ uvicorn main:app --reload

from mimetypes import suffix_map
from fastapi import FastAPI, Response
import api
import utils


# default fastapi app
app = FastAPI(
    title="go-echarger v3 API",
    description="API for go-echarger v3",
    version="0.1.0",
)


app.include_router(api.read.router, prefix="/api", tags=["Read Data"])
app.include_router(api.set_router, prefix="/api", tags=["Set Data"])
app.include_router(api.v1_router, prefix="/api/v1", tags=["v1 API"])

# hello world
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/status")
def read_status(
    response: Response
):
    # Redirect to /api/v1/status
    response.status_code = 307
    response.headers["Location"] = "/api/v1/status"
    return response

@app.get("/mqtt")
def set(
    response: Response,
    payload: str
    ):
    # Redirect to /api/v1/mqtt
    response.status_code = 307
    response.headers["Location"] = f"/api/v1/mqtt/?payload={payload}"
    return response

@app.get("/test")
def test(
    response: Response
):
    r = utils.start_switching()
    return r 
