import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            result_label.config(text="Length must be positive.")
            return
        global current_length
        current_length = length
        create_password(length)
    except ValueError:
        result_label.config(text="Please enter a valid number.")


def create_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=f"Your password: {password}")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.configure(bg="#e6f7ff")

current_length = 0

title_label = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), bg="#e6f7ff")
title_label.pack(pady=10)

length_frame = tk.Frame(root, bg="#e6f7ff")
length_frame.pack(pady=5)

tk.Label(length_frame, text="Password Length:", font=("Arial", 12), bg="#e6f7ff").pack(side=tk.LEFT)

length_entry = tk.Entry(length_frame, width=5, font=("Arial", 12))
length_entry.pack(side=tk.LEFT, padx=5)

generate_btn = tk.Button(root, text="Generate", font=("Arial", 12), bg="#4CAF50", fg="white", command=generate_password)
generate_btn.pack(pady=8)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#e6f7ff", wraplength=380, justify="center")
result_label.pack(pady=15)

root.mainloop()

