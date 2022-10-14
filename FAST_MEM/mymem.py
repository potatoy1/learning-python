from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse
from member_dao import MemberDao
from pydantic.main import BaseModel


class Member(BaseModel):
    m_seq:str = None
    m_name:str = None
    tel:str = None
    army_yn:str = None

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
@app.get("/mem", response_class=HTMLResponse)
async def mem_list(request: Request):
    return templates.TemplateResponse("mem.html", {"request": request})

@app.get("/mem_selects")
async def mem_selects():
    md = MemberDao()
    mems = md.selects()
    return JSONResponse(mems)

@app.post("/mem_select")
async def mem_select(mem:Member):
    md = MemberDao()
    mem = md.select(mem.m_seq)
    return JSONResponse(mem)

@app.post("/mem_insert")
async def mem_insert(mem:Member):
    md = MemberDao()
    cnt = md.insert(mem.m_name,mem.tel,mem.army_yn)
    return JSONResponse(cnt)

@app.post("/mem_update")
async def mem_update(mem:Member):
    md = MemberDao()
    cnt = md.update(mem.m_seq,mem.m_name,mem.tel,mem.army_yn)
    return JSONResponse(cnt)

@app.post("/mem_delete")
async def mem_delete(mem:Member):
    md = MemberDao()
    cnt = md.delete(mem.m_seq)
    return JSONResponse(cnt)
    