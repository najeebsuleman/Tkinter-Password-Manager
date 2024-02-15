import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from password_manager import generate_password, save_password, get_password, update_password


# Store New Password Tab UI
def store_new_password_tab(tab_control):
    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text='Store New Password')

    def save_new_password():
        app_name = app_name_entry.get()
        user_name = user_name_entry.get()
        password = password_entry.get()

        if app_name and user_name and password:
            save_password(app_name, user_name, password)
            messagebox.showinfo("Success", "Password saved successfully.")
            app_name_entry.delete(0, tk.END)
            user_name_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "All fields are required.")

    def on_generate_password():
        password_entry.delete(0, tk.END)
        password_entry.insert(0, generate_password())

    # Application Name
    tk.Label(tab, text="Application Name:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
    app_name_entry = tk.Entry(tab)
    app_name_entry.grid(row=0, column=1, padx=5, pady=5)

    # For Username
    tk.Label(tab, text="Username:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
    user_name_entry = tk.Entry(tab)
    user_name_entry.grid(row=1, column=1, padx=5, pady=5)

    # For Password
    tk.Label(tab, text="Password:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
    password_entry = tk.Entry(tab, show="*")
    password_entry.grid(row=2, column=1, padx=5, pady=5)

    # To Generate Password Button
    generate_password_button = tk.Button(tab, text="Generate Random Password", command=on_generate_password)
    generate_password_button.grid(row=3, column=1, padx=5, pady=5, sticky=tk.E)

    # To Save Password Button
    save_password_button = tk.Button(tab, text="Save Password", command=save_new_password)
    save_password_button.grid(row=4, column=1, padx=5, pady=5, sticky=tk.E)

    return tab


# Retrieve Password Tab
def retrieve_password_tab(tab_control):
    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text='Retrieve Password')

    def on_get_password():
        app_name = app_name_entry.get()
        if app_name:
            user_name, password = get_password(app_name)
            if user_name and password:
                user_name_value.set(user_name)
                password_value.set(password)
            else:
                messagebox.showerror("Error", "Password not found.")
        else:
            messagebox.showerror("Error", "Application name is required.")

    # Application Name
    tk.Label(tab, text="Application Name:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
    app_name_entry = tk.Entry(tab)
    app_name_entry.grid(row=0, column=1, padx=5, pady=5)

    # Username Display
    user_name_value = tk.StringVar()
    tk.Label(tab, text="Username:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
    user_name_label = tk.Label(tab, textvariable=user_name_value)
    user_name_label.grid(row=1, column=1, padx=5, pady=5)

    # Password Display
    password_value = tk.StringVar()
    tk.Label(tab, text="Password:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
    password_label = tk.Label(tab, textvariable=password_value)
    password_label.grid(row=2, column=1, padx=5, pady=5)

    # Get Password Button
    get_password_button = tk.Button(tab, text="Get Password", command=on_get_password)
    get_password_button.grid(row=3, column=1, padx=5, pady=5, sticky=tk.E)

    return tab


# Update Password Tab
def update_password_tab(tab_control):
    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text='Update Password')

    def on_update_password():
        app_name = app_name_entry.get()
        user_name = user_name_entry.get()
        old_password = old_password_entry.get()
        new_password = new_password_entry.get()

        if app_name and user_name and old_password and new_password:
            update_password(app_name, user_name, old_password, new_password)
            # messagebox.showerror("Done", "Successful")
        else:
            messagebox.showerror("Error", "All fields are required.")

    # Application Name
    tk.Label(tab, text="Application Name:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
    app_name_entry = tk.Entry(tab)
    app_name_entry.grid(row=0, column=1, padx=5, pady=5)

    # Username
    tk.Label(tab, text="Username:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
    user_name_entry = tk.Entry(tab)
    user_name_entry.grid(row=1, column=1, padx=5, pady=5)

    # Old Password
    tk.Label(tab, text="Old Password:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
    old_password_entry = tk.Entry(tab, show="*")
    old_password_entry.grid(row=2, column=1, padx=5, pady=5)

    # New Password
    tk.Label(tab, text="New Password:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
    new_password_entry = tk.Entry(tab, show="*")
    new_password_entry.grid(row=3, column=1, padx=5, pady=5)

    # Update Password Button
    update_password_button = tk.Button(tab, text="Update Password", command=on_update_password)
    update_password_button.grid(row=4, column=1, padx=5, pady=5, sticky=tk.E)


    return tab

