from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from main import app

import modal

##web_app = FastAPI()
web_app = app
app = modal.App()

image = modal.Image.debian_slim().pip_install("boto3").pip_install("sqlalchemy")

@app.function(image=image)
@modal.asgi_app()
def fastapi_app():
    return web_app