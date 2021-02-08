from typing import Optional, Dict

from fastapi import FastAPI, exceptions, Query, Header, Depends

from demo_pydantic import User, UserBase, UserOut

app = FastAPI()

ids = iter(range(1, 100000))

USERS = {}

USERS_BY_TOKEN: Dict[str, User] = {}


@app.get('/')
# def hello_world(name: str = Query(...)):
def hello_world(name: str = Query("world")):
    """
    Документация сразу отображается в /docs или /redoc

    ### Return greeting

    *Формат документации в Markdown*

    1. is json
    2. is documented
    3. is world
    """
    return {'message': name}


@app.get("/{item_id}/")
def item(item_id: int):
    """
    Returns item id

    """
    return {"item_id": item_id}


@app.post("/user/", response_model=UserOut, tags=["User"])
def create_user(user_in: UserBase):
    user = User(id=next(ids), **user_in.dict())
    USERS[user.id] = user
    USERS_BY_TOKEN[user.token] = user
    return {"user": user.dict()}


def get_current_user(token: str = Header(..., description="user auth token (user token)")) -> User:
    print("check for token", token)
    if token not in USERS_BY_TOKEN:
        raise exceptions.HTTPException(404, f"user token {token!r} not found")
    user = USERS_BY_TOKEN[token]
    return user
