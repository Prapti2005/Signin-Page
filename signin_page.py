import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to connect to the MySQL database
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",   
            user="root",  
            password="root",   
            database="student"
        )
        return connection
    except mysql.connector.Error as err:
        messagebox.showerror("Database Connection Error", f"Error: {err}")
        return None

# Function to handle sign in
def sign_in():
    username = entry_username.get()
    passwordd = entry_password.get()

    if not username or not passwordd:
        messagebox.showwarning("Input Error", "Please enter both username and password.")
        return

    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username=%s AND passwordd=%s"
        cursor.execute(query, (username, passwordd))
        result = cursor.fetchone()
        if result:
            messagebox.showinfo("Success", "Signed in successfully!")
        else:
            messagebox.showerror("Error", "Invalid username or password.")
        cursor.close()
        connection.close()

# Creating the main window
root = tk.Tk()
root.geometry("300x200")
root.title("Sign In Form")

# Username label and entry
label_username = tk.Label(root, text="Username")
label_username.grid(row=0, column=0, padx=10, pady=10)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

# Password label and entry
label_password = tk.Label(root, text="Password")
label_password.grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

# Sign in button
button_sign_in = tk.Button(root, text="Sign In", command=sign_in)
button_sign_in.grid(row=2, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()