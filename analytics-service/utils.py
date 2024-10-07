# utils.py

import requests
import json

# Function to read the prompt from the file
def read_file(filepath):
    """Read content from a file."""
    with open(filepath, 'r') as file:
        content = file.read()
    return content

# Function to send the request to the LLM (Ollama API)
def analyze_text_with_ollama(model, prompt, news_text, temperature):
    api_url = "http://localhost:11434/api/generate"  # Example of Ollama's API
    headers = {
        "Content-Type": "application/json",
    }

    # Prepare the data payload including the configurable temperature
    data = {
        "model": model,
        "prompt": f"{prompt}\n\nNews Text: {news_text}",
        "stream": False,
        "options": {
            "temperature": temperature  # Configurable temperature value
        }
    }
    
    try:
        # Send request to the Ollama API
        response = requests.post(api_url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return response.json()  # Return the full response including metadata
        else:
            return {"error": f"Failed to analyze text, status code: {response.status_code}", "details": response.text}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
