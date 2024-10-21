from fastapi import APIRouter
from services.login_service import consult_user
from models.users_model import consultModel
from services.logs_service import create_log
from models.logs_models import logsModel

router = APIRouter()

## Endpoint de login

@router.post("/consult")
def consult_service(consultModel:consultModel):
    create_log(logsModel(change = "Realizo inicio de sesión", table = "users", email = "rmoras@colonos.com" ))
    consult = consult_user(consultModel)
    return(consult)