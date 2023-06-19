import tkinter as tk
from guessing import *
import numpy as np


class LanguageSelector:
    def __init__(self, asdf):
        self.master = asdf
        self.master.title("Choose Your Character")

        # Main Message
        self.label = tk.Label(self.master, text="Choose Your Character")
        self.label.pack()

        # Default Language is English
        self.selected_language = tk.StringVar(value="English")

        # Create four radio buttons for the languages and set the variable to the selected_language StringVar
        self.english_button = tk.Radiobutton(self.master, text="English", variable=self.selected_language, value="English")
        self.german_de_button = tk.Radiobutton(self.master, text="German (DE)", variable=self.selected_language,
                                               value="German (DE)")
        self.german_at_button = tk.Radiobutton(self.master, text="German (AT)", variable=self.selected_language,
                                               value="German (AT)")
        self.spanish_button = tk.Radiobutton(self.master, text="Spanish", variable=self.selected_language, value="Spanish")

        # Pack the radio buttons onto the window
        self.english_button.pack()
        self.german_de_button.pack()
        self.german_at_button.pack()
        self.spanish_button.pack()

        # Create a "Done" button that will call the done_button_clicked function when clicked
        self.done_button = tk.Button(self.master, text="Done", command=self.done_button_clicked)
        self.done_button.pack()

        # Bind the Return key to the "Done" button
        self.master.bind("<Return>", self.done_button_clicked)

        # Initialize the selected_language_window to None
        self.selected_language_window = None

    # Create a function to be called when the "Done" button is clicked
    def done_button_clicked(self, event=None):
        self.selected_character = self.selected_language.get()
        # print("Selected Language:", selected_language_value)

        # Open a new window with the selected language message
        self.selected_language_window = tk.Toplevel(self.master)
        self.selected_language_window.title("Language Selected")

        # Create a label to display the selected language message
        self.label = tk.Label(self.selected_language_window, text=f"You selected {self.selected_character}")
        self.label.pack()


        # Create a "ok" button that will call the done_button_clicked function when clicked
        self.ok_button = tk.Button(self.selected_language_window, text="Ok", command=self.ok_button_clicked)
        self.ok_button.pack()

        # Unbinds the Return key from the "Done" button
        self.master.unbind("<Return>")
        # Bind the Return key to the "Done" button
        self.master.bind("<Return>", self.ok_button_clicked)

    def ok_button_clicked(self, event=None):
        print('amd I here')
        # close the window
        self.master.destroy()


root = tk.Tk()
language = LanguageSelector(root)
root.mainloop()

language = language.selected_character
possible_words = get_words(language)
all_words = possible_words

