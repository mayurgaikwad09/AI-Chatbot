from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from chatbot import get_response
from database import save_chat_with_time, clear_chat

app = FastAPI(title="AI Powered Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

class ChatRequest(BaseModel):
    user_message: str

# ✅ THIS WILL SHOW YOUR HTML UI
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
def chat(req: ChatRequest):
    bot_reply = get_response(req.user_message)
    save_chat_with_time(req.user_message, bot_reply)
    return {"response": bot_reply}

@app.post("/clear")
def clear():
    clear_chat()
    return {"message": "Chat history cleared"}
