import hashlib
import tkinter as tk
from tkinter import messagebox

def generate_hash():
    
    user_input = entry.get()
    
    hash_object = hashlib.sha256(user_input.encode())
    hash_hex = hash_object.hexdigest()
    
    messagebox.showinfo("SHA-256 Hash", f"The SHA-256 hash of '{user_input}' is:\n{hash_hex}")

root = tk.Tk()
root.title("SHA-256 Hash Generator")


label = tk.Label(root, text="Enter a string to hash:")
label.pack(pady=10)


entry = tk.Entry(root, width=50)
entry.pack(pady=10)


button = tk.Button(root, text="Generate Hash", command=generate_hash)
button.pack(pady=10)


root.mainloop()
