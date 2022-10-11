from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse
from emp_dao import EmpDao

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
@app.get("/emp", response_class=HTMLResponse)
async def emp_list(request: Request):
    return templates.TemplateResponse("emp.html", {"request": request})

@app.get("/emp_selects")
async def emp_selects():
    ed = EmpDao()
    emps = ed.selects()
    return JSONResponse(emps)
    