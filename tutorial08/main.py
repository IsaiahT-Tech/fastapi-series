from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

@app.get("/{book}/{id}", response_class=HTMLResponse)
async def read(request: Request, book: str, id: int):
    return templates.TemplateResponse("index.html", {"request": request, "book": book, "id": id})
