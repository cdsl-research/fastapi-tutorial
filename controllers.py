from fastapi import FastAPI
from starlette.templating import Jinja2Templates
# from jinja2 import Template
from starlette.requests import Request

app = FastAPI(
    title="let's make toDo Application for FastAPI",
    description="Fastapiチュートリアル:シンプルなtodoアプリケーションを作りましょう",
    version='0.9 beta'
)

templates = Jinja2Templates(directory="templates")
jinja_env = templates.env

def index(request: Request):
    # return {'Hello': 'World'}
    return templates.TemplateResponse('index.html',
                                    {'request': request})