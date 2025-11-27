print("Hello from Mr.1 and Mrs.1, Boy!")

# Copilot: Write a function that checks if an email is valid (very simple check).
def is_valid_email(email):
    return "@" in email and "." in email.split("@")[-1]