from typing import Optional
from fastapi import APIRouter, Response, Query
# from utils import map
from utils.mapv1tov2 import map_read

# fastapi prefix /api
router = APIRouter(
)

# Hello world

@router.get("/status")
@router.get("/", )
# add filter alf
def read_all(
    response: Response,

    filter: Optional[str]   = None
):
    data = map_read()
    if filter:
        filtered_data = {}
        filter = str.split(filter, ',')
        for i in filter:
            filtered_data.update({i : data[i]})
        return filtered_data
    else:
        response.status_code = 200
        return map_read()

