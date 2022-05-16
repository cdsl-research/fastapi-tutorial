from urllib import request
from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import APIRouter
from starlette.requests import Request

app = FastAPI(
    title="let's make toDo Application for FastAPI",
    description="Fastapiチュートリアル:シンプルなtodoアプリケーションを作りましょう",
    version='0.9 beta'
)

templates = Jinja2Templates(directory="templates")
jinja_env = templates.env


def hello(request: Request):
    # return {'Hello': 'World'}
    return templates.TemplateResponse('hello.html',
                                    {'request': request})
def hello_tut():
    return templates.TemplateResponse('tut.html',
                                    {'request': request})
