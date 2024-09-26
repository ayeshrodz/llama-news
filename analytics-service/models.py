# models.py

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class NewsRequest(BaseModel):
    title: str
    content: str
    published_date: Optional[datetime] = Field(None, alias='published_date')
    source: Optional[str]
    author: Optional[str]
    url: Optional[str]
    reference: Optional[str]
    llm_model: Optional[str]
    # Include any additional fields as necessary

class AnalysisResponse(BaseModel):
    Sentiment: dict
    Tone: list
    Language: list
    Emotive_Phrases: list
    Authority_Figure: dict
    Keywords: list
    Summary: str
    # Include additional fields from the analysis output as needed
    Entities: Optional[dict]
    Emotions: Optional[list]
    Subjectivity: Optional[dict]
    Recommendations: Optional[list]
    Questions: Optional[list]
    Categories: Optional[List[str]]
