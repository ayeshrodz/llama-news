# main.py

import json
from text_analyzer import TextAnalyzer

def read_news_text(file_path='news.txt'):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"News file '{file_path}' not found.")
        return ""

def main():
    text = read_news_text()
    if text:
        analyzer = TextAnalyzer()
        response = analyzer.analyze_text(text)
        # Print the JSON output
        print(json.dumps(response, indent=2))
    else:
        print("No text to analyze.")

if __name__ == "__main__":
    main()
