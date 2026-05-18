import re
import sys
from deep_translator import GoogleTranslator
import time

sys.stdout.reconfigure(encoding='utf-8')
translator = GoogleTranslator(source='ar', target='en')

def translate_js_file(filepath):
    print(f"Starting translation for {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    def replacer(match):
        full_string = match.group(0)
        quote_char = full_string[0]
        inner_text = full_string[1:-1]
        
        if re.search(r'[\u0600-\u06FF]', inner_text):
            try:
                # Replace ${var} with a placeholder
                vars = re.findall(r'\$\{[^\}]+\}', inner_text)
                temp_text = inner_text
                for i, v in enumerate(vars):
                    temp_text = temp_text.replace(v, f"__VAR{i}__")
                
                # Sleep briefly
                time.sleep(0.5)
                translated = translator.translate(temp_text)
                
                # Put ${var} back
                for i, v in enumerate(vars):
                    translated = translated.replace(f"__VAR{i}__", v)
                
                return f"{quote_char}{translated}{quote_char}"
            except Exception as e:
                return full_string
        return full_string

    pattern = r'(["\'`])(?:(?=(\\?))\2.)*?\1'
    new_content = re.sub(pattern, replacer, content)

    # Handle single line comments
    def comment_replacer(match):
        comment = match.group(0)
        if re.search(r'[\u0600-\u06FF]', comment):
            try:
                time.sleep(0.5)
                return translator.translate(comment)
            except:
                return comment
        return comment
        
    new_content = re.sub(r'//.*', comment_replacer, new_content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Finished {filepath}")

translate_js_file('script.js')
translate_js_file('curriculum.js')
