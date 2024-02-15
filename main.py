import tkinter as tk
from tkinter import ttk
from ui import store_new_password_tab, retrieve_password_tab, update_password_tab

def main():
    root = tk.Tk()
    root.title("Password Manager")

    tab_control = ttk.Notebook(root)
    store_new_password_tab(tab_control)
    retrieve_password_tab(tab_control)
    update_password_tab(tab_control)

    tab_control.pack(expand=1, fill="both")
    root.mainloop()

if __name__ == "__main__":
    main()