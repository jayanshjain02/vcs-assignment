# Copilot: Generate a 5-6 line docstring explaining what this program does.
"""
This program demonstrates basic Python functionality including printing a greeting message and defining a simple function to validate email addresses. The greeting message is printed to the console, and the email validation function checks for the presence of "@" and a period in the domain part of the email address.
"""

print("Hello from Mr.1 and Mrs.1, Boy!")

# Copilot: Write a function that checks if an email is valid (very simple check).
def is_valid_email(email):
    return "@" in email and "." in email.split("@")[-1]