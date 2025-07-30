from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
async def generate_bio(request: Request, vibe: str = Form(...), emoji: str = Form(...), reason: str = Form(...)):
    bio = f"{emoji} {vibe.title()} | {reason.capitalize()} | Click the link 😘"
    return templates.TemplateResponse("index.html", {"request": request, "bio": bio})
