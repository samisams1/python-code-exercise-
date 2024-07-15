import re

def match_pattern(pattern, text):
    matches = re.findall(pattern, text)
    return matches

pattern = r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'
text = "Contact us at support@example.com"
print(match_pattern(pattern, text))