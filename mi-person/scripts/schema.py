from typing import Any, Dict, Optional
from pydantic import BaseModel

class Sentiment(BaseModel):
    sentence: str
    
