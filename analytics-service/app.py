from fastapi import FastAPI, HTTPException
from models import NewsRequest, AnalysisResponse
from text_analyzer import TextAnalyzer
import logging

app = FastAPI(title="News Analysis API")

# Initialize the TextAnalyzer
analyzer = TextAnalyzer()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_news(news: NewsRequest):
    # Validate mandatory fields
    if not news.title or not news.content:
        raise HTTPException(status_code=400, detail="Title and content fields are required.")
    
    # Combine title and content for analysis
    text_to_analyze = f"Title: {news.title}\n\nContent: {news.content}"

    # Get the model name from the request, if provided
    llm_model = news.llm_model

    # Perform the analysis
    result = analyzer.analyze_text(text_to_analyze, llm_model=llm_model)

    if not result:
        raise HTTPException(status_code=500, detail="Analysis failed.")

    # Return the analysis result
    return result
