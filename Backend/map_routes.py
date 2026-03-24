from fastapi import APIRouter
from app.utils.load_json import ng_json_data

router = APIRouter(
    prefix="/map",
    tags=["map"]
)

@router.get("/nigeria")
async def get_nigeria_map():
    return {"ng_map": ng_json_data}