from fastapi import FastAPI
from routes import user_router, cards_router, company_router, login_router, logs_router


app = FastAPI()

app.include_router(login_router.router, tags=["Login"], prefix="/login")
app.include_router(user_router.router, tags=["Users"], prefix="/users")
app.include_router(cards_router.router, tags=["Card"], prefix="/cards")
app.include_router(company_router.router, tags=["Company"], prefix="/company")
app.include_router(logs_router.router, tags=["Logs"], prefix="/logs")