from fastapi import FastAPI, Request, HTTPException, Depends, BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from fastapi.templating import Jinja2Templates

#setup templates
templates = Jinja2Templates(directory="./templates")

app = FastAPI()

@app.get('/index',response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        context={"request": request}
        )