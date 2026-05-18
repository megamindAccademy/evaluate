import json
import os
import re
import time
import sys
from deep_translator import GoogleTranslator

# Set stdout to utf-8 just in case
sys.stdout.reconfigure(encoding='utf-8')

def has_arabic(text):
    return bool(re.search(r'[\u0600-\u06FF]', text))

translator = GoogleTranslator(source='ar', target='en')

def translate_text(text):
    if not has_arabic(text):
        return text
    try:
        # Avoid passing too large strings all at once, though GoogleTranslator handles up to 5k chars.
        if len(text) > 4000:
            return text # Skip or chunk it if needed
        translated = translator.translate(text)
        return translated if translated else text
    except Exception as e:
        print(f"Translation failed for a chunk. Error: {e}")
        return text

def translate_json_obj(obj):
    if isinstance(obj, dict):
        new_dict = {}
        for k, v in obj.items():
            new_dict[k] = translate_json_obj(v)
        return new_dict
    elif isinstance(obj, list):
        return [translate_json_obj(item) for item in obj]
    elif isinstance(obj, str):
        if has_arabic(obj):
            # time.sleep(0.05) # Small sleep to prevent rate limiting
            return translate_text(obj)
        return obj
    else:
        return obj

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    translated_data = translate_json_obj(data)
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(translated_data, f, ensure_ascii=False, indent=2)
                        
                    print(f"Processed: {file_path}")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    process_directory("database")
