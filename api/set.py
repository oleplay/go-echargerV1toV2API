from fastapi import APIRouter, Response, Query, Request
from utils import map_set
from utils import setdata

router = APIRouter(
    # name="Set Data",
)

@router.post("/set")
@router.get("/set")
def set_data(
    response: Response,
    request: Request,
    # set_data: str = "",
    # data: str = {}
):
    query_params = request.query_params._dict
    # print(query_params)
    
    x = map_set(query_params)
    r = setdata(x)
    response.status_code = r.status_code
    return r.json()
