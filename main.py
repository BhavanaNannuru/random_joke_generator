import requests
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style


# Function to fetch a joke on call form the API
def get_joke():
    pass

# Creating the window: Gui
window = tk.Tk()
window.title("Joke Generator")
window.geometry("700x400")
style = Style(theme='darkly')
window.style = style

# Creating the label widget
joke_label = tk.Label(text="Click the button to get a joke!", font=("Arial", 16))
joke_label.place(relx=0.5, rely=0.4, anchor="center")

# Creating the get joke button 
get_button = ttk.Button(text="Get Joke", command=get_joke)
get_button.pack(pady=20)

window.mainloop()