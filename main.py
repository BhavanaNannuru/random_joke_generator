import requests
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style


# Function to fetch a joke on call form the API
def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        joke_data = response.json()
        setup = joke_data['setup']
        punchline = joke_data['punchline']
        joke_label.configure(text=f"{setup}\n\n{punchline}")
    else:
        joke_label.configure(text="Failed to retrieve a joke.")

# Creating the window: Gui
window = tk.Tk()
window.title("Joke Generator")
window.geometry("500x400")
style = Style(theme='darkly')
window.style = style

# Creating the label widget
joke_label = tk.Label(text="Click the button to get a joke!", font=("Arial", 16), wraplength=450, justify="center", anchor="center")
joke_label.place(relx=0.5, rely=0.4, anchor="center")

# Creating the get joke button 
get_button = ttk.Button(text="Get Joke", command=get_joke)
get_button.pack(pady=20)

window.mainloop()