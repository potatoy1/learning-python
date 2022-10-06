from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi import FastAPI, Form

app = FastAPI()
class Item(BaseModel):
    dan : str
    
    
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello", response_class=HTMLResponse)
async def hello():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """

@app.get("/dan", response_class=HTMLResponse)
async def dan(dan: str):
    idan = int(dan)
    txt = ""
    
    txt += f"{idan} * {1} = {idan*1}<br>"
    txt += f"{idan} * {2} = {idan*2}<br>"
    txt += f"{idan} * {3} = {idan*3}<br>"
    txt += f"{idan} * {4} = {idan*4}<br>"
    txt += f"{idan} * {5} = {idan*5}<br>"
    txt += f"{idan} * {6} = {idan*6}<br>"
    txt += f"{idan} * {7} = {idan*7}<br>"
    txt += f"{idan} * {8} = {idan*8}<br>"
    txt += f"{idan} * {9} = {idan*9}<br>"

    return f"""
    <html>
        <head>
            <title>구구단</title>
        </head>
        <body>
            {txt}
        </body>
    </html>
    """
    
    
@app.post("/dan", response_class=HTMLResponse)
async def dan_post(dan: str= Form()):
    idan = int(dan)
    txt = ""
    
    txt += f"{idan} * {1} = {idan*1}<br>"
    txt += f"{idan} * {2} = {idan*2}<br>"
    txt += f"{idan} * {3} = {idan*3}<br>"
    txt += f"{idan} * {4} = {idan*4}<br>"
    txt += f"{idan} * {5} = {idan*5}<br>"
    txt += f"{idan} * {6} = {idan*6}<br>"
    txt += f"{idan} * {7} = {idan*7}<br>"
    txt += f"{idan} * {8} = {idan*8}<br>"
    txt += f"{idan} * {9} = {idan*9}<br>"

    return f"""
    <html>
        <head>
            <title>구구단</title>
        </head>
        <body>
            {txt}
        </body>
    </html>
    """  
    

# uvicorn myfastapi01:app --reload