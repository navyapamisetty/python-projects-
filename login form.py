import tkinter as tk
from tkinter import messagebox

def validate_login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # Replace this with your actual authentication logic
    correct_username = "Navya"
    correct_password = "123"

    if entered_username == correct_username and entered_password == correct_password:
        messagebox.showinfo("Login Successful", "Welcome, " + entered_username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login Form")

# Create and place widgets (labels, entries, buttons)
tk.Label(root, text="Username:").grid(row=0, column=0, sticky="E")
tk.Label(root, text="Password:").grid(row=1, column=0, sticky="E")

username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")  # 'show' attribute hides the password

username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)

login_button = tk.Button(root, text="Login", command=validate_login)
login_button.grid(row=2, column=1, pady=10)

# Start the GUI event loop
root.mainloop()
