# prompt_manager.py

class PromptManager:
    def __init__(self, prompt_file='prompt.txt'):
        self.prompt_template = self._read_prompt(prompt_file)

    def _read_prompt(self, prompt_file):
        try:
            with open(prompt_file, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Prompt file '{prompt_file}' not found.")
            return ""

    def format_prompt(self, text):
        return f"""News Text: {text}\n{self.prompt_template}"""
