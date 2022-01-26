# To run this fastapi app:
# $ python3 main.py
#
# To run this fastapi app with uvicorn:
# $ uvicorn main:app --reload

from mimetypes import suffix_map
from fastapi import FastAPI
import api.read
import utils


# default fastapi app
app = FastAPI(
    title="go-echarger v3 API",
    description="API for go-echarger v3",
    version="0.1.0",
)

app.include_router(api.read.router, prefix="/api")
# hello world
@app.get("/")
def read_root():
    return {"Hello": "World"}

