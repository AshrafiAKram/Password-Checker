import tkinter as tk
from tkinter import messagebox
import re
import random
import string

def check_password_strength(password):
    if len(password) < 8:
        return "Weak (Too short)"

    if not re.search("[a-z]", password):
        return "Weak (No lowercase letter)"

    if not re.search("[A-Z]", password):
        return "Weak (No uppercase letter)"

    if not re.search("[0-9]", password):
        return "Weak (No digit)"

    if not re.search("[@#$%^&+=]", password):
        return "Weak (No special character)"

    return "Strong"

def generate_password(length=12, strength_criteria=None):
    if not strength_criteria:
        strength_criteria = {
            'length': 12,
            'uppercase': True,
            'lowercase': True,
            'digits': True,
            'special_characters': True
        }

    characters = ''
    if strength_criteria['uppercase']:
        characters += string.ascii_uppercase
    if strength_criteria['lowercase']:
        characters += string.ascii_lowercase
    if strength_criteria['digits']:
        characters += string.digits
    if strength_criteria['special_characters']:
        characters += string.punctuation

    if not characters:
        raise ValueError("Strength criteria must include at least one character set")

    return ''.join(random.choice(characters) for _ in range(strength_criteria['length']))

def check_password():
    password = entry_password.get()
    strength = check_password_strength(password)
    messagebox.showinfo("Password Strength", f"Password Strength: {strength}")

def generate_new_password():
    strength_criteria = {
        'length': 12,
        'uppercase': True,
        'lowercase': True,
        'digits': True,
        'special_characters': True
    }
    new_password = generate_password(strength_criteria=strength_criteria)
    entry_password.delete(0, tk.END)
    entry_password.insert(0, new_password)

def toggle_password_visibility():
    if entry_password.cget("show") == "*":
        entry_password.config(show="")
        button_view_password.config(text="Hide Password")
    else:
        entry_password.config(show="*")
        button_view_password.config(text="View Password")

# Create the main window
root = tk.Tk()
root.title("Password Checker and Generator")

# Create the password entry field
label_password = tk.Label(root, text="Enter Password:")
label_password.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=0, column=1, padx=10, pady=5)

# Create the buttons
button_check = tk.Button(root, text="Check", command=check_password)
button_check.grid(row=1, column=0, padx=10, pady=5)

button_generate = tk.Button(root, text="Generate", command=generate_new_password)
button_generate.grid(row=1, column=1, padx=10, pady=5)

button_view_password = tk.Button(root, text="View Password", command=toggle_password_visibility)
button_view_password.grid(row=2, column=1, padx=10, pady=5)

# Run the main event loop
root.mainloop()
