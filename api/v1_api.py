from os import urandom
from fastapi import APIRouter, Response, Query, Request
import utils

router = APIRouter(
)

@router.get("/status")
def get_status(
    respone: Response
):
    
    r = utils.getdata()
    respone.status_code= r.status_code
    return r.json()

@router.get("/mqtt")
def set(
    request: Request,
    respone: Response,
    payload: str
    ):
    print(payload)
    r = utils.setdatafromv1(payload)
    respone.status_code = r.status_code
    return r.json()
    
