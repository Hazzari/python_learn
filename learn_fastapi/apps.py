import typing
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from schemas import Book

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get('/', tags=['Index'])
def home():
    return {'key': 'Hello'}


@app.get('/{pk}')
def get_item(pk: int, query: typing.Union[int, float] = None):
    return {'key': pk, 'query': query}


@app.get('/user/{pk}/items/{item}/')
def get_user_item(pk: int, item: str):
    return {'user': pk, 'item': item}


@app.post('/book')
def create_book(item: Book):
    return item


@app.get("/items/{pk}", response_class=HTMLResponse)
async def read_item(request: Request, pk: str):
    return templates.TemplateResponse("index.html", {"request": request, "pk": pk})
