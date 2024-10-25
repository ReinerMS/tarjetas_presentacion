from fastapi import APIRouter
from services.login_service import consult_user
from models.users_model import consultModel
from services.logs_service import create_log
from models.logs_models import logsModel

router = APIRouter()

## Endpoint de login

@router.post("/consult")
def consult_service(consultModel:consultModel):
    """
    Realiza una consulta sobre el usuario proporcionado en el modelo de consulta.

    Esta función recibe un modelo de consulta, realiza un log sobre el inicio de sesión y devuelve
    la información consultada.

    - **consultModel**: El modelo de consulta con los datos necesarios.
    """
    create_log(logsModel(change = "Realizo inicio de sesión", table = "users", email = "rmoras@colonos.com" ))
    consult = consult_user(consultModel)
    return(consult)