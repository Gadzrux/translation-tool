from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates("./templates")

@app.get("/", response_class=HTMLResponse)
def send_template(request: Request):
    return templates.TemplateResponse(
        request,
        name="index.html"
        )