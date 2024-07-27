from pydantic import BaseModel
from typing import List, Dict

class PlayerDetails(BaseModel):
    name: str
    age: int
    position: str

class BufferMessage(BaseModel):
    role: str
    content: str

class ChatbotRequest(BaseModel):
    prompt: str
    player_details: PlayerDetails
