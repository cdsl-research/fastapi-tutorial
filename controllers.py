from re import template
from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI(
    title="I make a toDo Application with FastAPI",
    description="FastAPI tutorial: Let's make a simple toDo Application with FastAPI(and starlette)",
    version='1.0 beta test'
)

# new template related settings(jinja2)
templates = Jinja2Templates(directory="templates_test")
# Jinja2.Environment : settings for filter and global
jinja_env = templates.env    

def index_test(request: Request):
    return templates.TemplateResponse('index.html',
                                        {'request': request}) # new change!
def admin(request: Request):
    return templates.TemplateResponse('admin.html',
                                        {'request': request,
                                        'username': 'admin'})
    