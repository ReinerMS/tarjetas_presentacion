from fastapi import APIRouter
from services.company_service import get_company,create_company, Company
from models.logs_models import logsModel
from services.logs_service import create_log

router = APIRouter()

@router.get("/")
def read_root():
    company = get_company()
    return(company)

@router.post("/")
def create_root(company:Company):
    create_log(logsModel(change = "Creo una compañia", table = "company", email = "rmoras@colonos.com" ))
    message = create_company(company)
    return(message)