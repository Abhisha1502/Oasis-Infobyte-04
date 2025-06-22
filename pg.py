import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 6:
            messagebox.showwarning("Weak Password", "Password should be at least 6 characters long.")
            return

        characters = ""
        if var_letters.get():
            characters += string.ascii_letters
        if var_numbers.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Invalid Selection", "Please select at least one character set.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid password length.")

# Function to copy password
def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "Generate a password first.")

# GUI Setup
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Title
title = tk.Label(root, text="Random Password Generator", font=("Helvetica", 16, "bold"))
title.pack(pady=10)

# Input for password length
tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root, width=10)
length_entry.pack(pady=5)

# Options
var_letters = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters (A-Z, a-z)", variable=var_letters).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Numbers (0-9)", variable=var_numbers).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Symbols (!@#...)", variable=var_symbols).pack(anchor='w', padx=20)

# Generate Button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white")
generate_btn.pack(pady=10)

# Display password
password_entry = tk.Entry(root, font=("Courier", 12), justify="center")
password_entry.pack(pady=5)

# Copy Button
copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2196F3", fg="white")
copy_btn.pack(pady=5)

root.mainloop()

YtjjwbrO