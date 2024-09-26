import requests
import json

class APIClient:
    def __init__(self, base_url='http://localhost:11434/api/generate'):
        self.base_url = base_url

    def generate_response(self, payload):
        try:
            response = requests.post(self.base_url, json=payload, stream=True)
            response.raise_for_status()
            return self._parse_stream_response(response)
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return None

    def _parse_stream_response(self, response):
        generated_text = ""
        for line in response.iter_lines():
            if line:
                try:
                    # Each line is a JSON object
                    data = json.loads(line.decode('utf-8'))
                    token = data.get('response', '')
                    generated_text += token
                except json.JSONDecodeError:
                    continue  # Skip lines that cannot be parsed
        return generated_text.strip()
