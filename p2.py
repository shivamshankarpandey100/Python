import re

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Example usage
email = "user@example.com"
if re.match(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address.")
