import re

# Input string
input_string = "Hello! 123 This is a test string."

# Remove everything except spaces and numbers
result = re.sub(r'[^0-9\s]', '', input_string)

print(result)
