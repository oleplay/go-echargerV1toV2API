from fastapi import APIRouter, Response, Query, Request
from utils import map_set
from utils import setdata

router = APIRouter(
    # name="Set Data",
)


@router.get("/set")
def set_data(
    response: Response,
    request: Request,
    # set_data: str = "",
    # data: str = {}
):
    query_params = request.query_params._dict
    x = map_set(query_params)
    setdata(x)
