from os import urandom
from fastapi import APIRouter, Response, Query, Request
import utils

router = APIRouter(
)

@router.get("/status")
def get_status(
    response: Response
):
    
    r = utils.getdata()
    response.status_code = r.status_code
    return r.json()

@router.post("/mqtt")
@router.get("/mqtt")
def set(
    request: Request,
    response: Response,
    payload: str
    ):
    print(payload)
    r = utils.setdatafromv1(payload)
    response.status_code = r.status_code
    return r.json()
    
