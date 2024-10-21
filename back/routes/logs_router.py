from fastapi import APIRouter
from services.logs_service import consult_bd_logs

router = APIRouter()

@router.get("/")
def read_root():
    logs = consult_bd_logs()
    return(logs)