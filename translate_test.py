import json
import os
import re
import time
from deep_translator import GoogleTranslator

def has_arabic(text):
    return bool(re.search(r'[\u0600-\u06FF]', text))

translator = GoogleTranslator(source='ar', target='en')

def translate_text(text):
    if not has_arabic(text):
        return text
    try:
        translated = translator.translate(text)
        return translated if translated else text
    except Exception as e:
        print(f"Translation failed for: {text[:50]}... Error: {e}")
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
            print(f"Translating: {obj[:50]}")
            time.sleep(0.1) # to prevent rate limiting
            return translate_text(obj)
        return obj
    else:
        return obj

file_path = "database/junior_python/games.json"
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

translated_data = translate_json_obj(data)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(translated_data, f, ensure_ascii=False, indent=2)

print("Done translating", file_path)
