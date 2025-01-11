import tkinter as tk
import random
import string

root = tk.Tk()
root.title("Password Generator")

password_label = tk.Label(root, text="Click the button to generate a password", font=("Arial", 12))
password_label.pack(pady=10)


def generate_password():
    length = 12  
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text=f"Password: {password}")

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12))
generate_button.pack(pady=10)

root.mainloop()