# main.py

from fastapi import FastAPI
from models import LLMRequest  # Import the model from models.py
from utils import read_file, analyze_text_with_ollama  # Import the utility functions

# Initialize FastAPI app
app = FastAPI()

# The FastAPI POST endpoint
@app.post("/analyze")
def analyze_news(request: LLMRequest):
    # Read the predefined prompt (assuming it's stored in a text file)
    prompt_file = "sentiment_prompt.txt"  # File path to the prompt
    prompt = read_file(prompt_file)

    # Make a call to the Ollama API with the parameters
    result = analyze_text_with_ollama(
        model=request.model, 
        prompt=prompt,
        news_text=f"{request.news_title}\n{request.news_content}",
        temperature=request.temperature_value
    )
    
    # Return the full analysis result along with optional parameters
    return {
        "news_title": request.news_title,
        "news_content": request.news_content,
        "news_url": request.news_url,
        "published_date": request.published_date,
        "llm_analysis": result
    }
