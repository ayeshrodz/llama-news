# text_analyzer.py

import json
import re
from api_client import APIClient
from prompt_manager import PromptManager

class TextAnalyzer:
    def __init__(self, model='llama3.2:3b', num_ctx=2048, temperature=0.3):
        self.api_client = APIClient()
        self.prompt_manager = PromptManager()
        self.model = model
        self.num_ctx = num_ctx
        self.temperature = temperature

    def analyze_text(self, text, llm_model=None):
        prompt = self.prompt_manager.format_prompt(text)
        payload = {
            "model": llm_model if llm_model else self.model,
            "prompt": prompt,
            "num_ctx": self.num_ctx,
            "temperature": self.temperature,
            "stop": ["<JSON_END>"]
        }
        generated_text = self.api_client.generate_response(payload)
        if generated_text:
            return self._parse_generated_text(generated_text)
        else:
            return {}

    def _parse_generated_text(self, generated_text):
        # Extract the JSON content between <JSON_START> and <JSON_END>
        match = re.search(r'<JSON_START>(.*?)<JSON_END>', generated_text, re.DOTALL)
        if match:
            json_content = match.group(1).strip()
            # Attempt to parse the extracted JSON content
            try:
                result = json.loads(json_content)
                return result
            except json.JSONDecodeError as e:
                print("Failed to parse the JSON content.")
                print("Extracted JSON content:")
                print(json_content)
                return {}
        else:
            print("JSON markers not found in the response.")
            print("Generated text:")
            print(generated_text)
            return {}
