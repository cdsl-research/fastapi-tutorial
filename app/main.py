# from urllib import request
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.requests import Request

app = FastAPI(
    title="FastAPI tutorial",
    description="FastAPIを学ぼう！！！",
    version='0.9 beta'
)

templates = Jinja2Templates(directory="templates")
jinja_env = templates.env


@app.get("/")
def hello(request: Request):
    # return {'Hello': 'World'}
    return templates.TemplateResponse('hello.html',
                                    {'request': request})
@app.get("/hello_tut")
def hello_tut(request: Request):
    return templates.TemplateResponse('tut.html',
                                    {'request': request})
