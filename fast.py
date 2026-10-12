from datetime import datetime
from fastapi import FastAPI, Request, status, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from starlette.responses import RedirectResponse
from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, select

from model import engine, Todo

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]


class TemplateCreate(BaseModel):
    title: str
    description: str | None = None
    created_at: datetime | None = None
    status: bool = False


class TemplateUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    created_at: datetime | None = None
    status: bool | None = None


@app.get("/todo/create", tags=["todo-frontend"])
async def todo_create_page(request: Request):
    return templates.TemplateResponse(request=request, name="todo_create.html")


@app.post("/todo/create", status_code=status.HTTP_201_CREATED, tags=["todo"])
async def todo_create_submit(
        request: Request,
        session: SessionDep
):
    form_data = await request.form()
    title = form_data.get("title")
    description = form_data.get("description")

    instance = Todo(
        title=title,
        description=description,
        status=False
    )
    session.add(instance)
    session.commit()

    return RedirectResponse(url="/todo/list", status_code=status.HTTP_303_SEE_OTHER)


# ---------- READ ----------
@app.get("/todo/list", tags=["todo-frontend"])
async def todo_list_template(request: Request, session:  SessionDep):
    todo = session.exec(select(Todo)).all()
    return templates.TemplateResponse(
        request=request,
        name="todo_list.html",
        context={"todo": todo})



@app.get("/todo/{todo_id}/update", tags=["todo-frontend"])
async def todo_update_page(request: Request, todo_id: int, session: SessionDep):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found!")
    return templates.TemplateResponse(
        request=request,
        name="todo_update.html",
        context={"todo": todo}
    )

# ---------- UPDATE ----------
@app.post("/todo/{todo_id}/update", tags=["todo-frontend"])
async def todo_update_submit(
        request: Request,
        todo_id: int,
        session: SessionDep
):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found!")

    form_data = await request.form()
    todo.title = form_data.get("title")
    todo.description = form_data.get("description")
    todo.status = True if form_data.get("status") == "on" else False

    session.add(todo)
    session.commit()

    return RedirectResponse(url="/todo/list", status_code=status.HTTP_303_SEE_OTHER)


# ---------- DELETE ----------
@app.post("/todo/{todo_id}/delete", tags=["todo-frontend"])
async def todo_delete(todo_id: int, session:  SessionDep):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found!")
    session.delete(todo)
    session.commit()
    return RedirectResponse(url="/todo/list", status_code=status.HTTP_303_SEE_OTHER)

