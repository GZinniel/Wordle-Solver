import tkinter as tk

class OneLetterInputGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("One Letter Input")
        self.label = tk.Label(self.root, text="Enter one letter:")
        self.label.pack()
        self.entry = tk.Entry(self.root, validate="key")
        self.entry.config(validatecommand=(self.entry.register(self.validate_input), "%P"))
        self.entry.pack()
        self.entry.bind("<Button-1>", self.change_color)  # bind left-click event to change_color method
        self.entry.bind("<KeyRelease>", self.update_letter)  # bind key release event to update_letter method
        self.colors = ["green", "yellow", "gray"]  # list of colors to cycle through
        self.color_index = 0  # index of current color
        self.set_color(self.get_color())  # set initial color based on input
        self.current_input = ''  # initialize current input to None
        self.previous_input = ''
        self.root.mainloop()

    def validate_input(self, value):
        if len(value) >= 1:
            self.root.bell()
            self.current_input = value[-1]
            self.entry.delete(0, tk.END)  # remove excess characters
            self.entry.insert(0, 'l')
            return False
        self.previous_input = self.current_input
        self.current_input = value
        self.set_color(self.get_color())  # set color based on input
        return True

    def change_color(self, event):
        if self.entry.get():
            self.color_index = (self.color_index + 1) % len(self.colors)  # cycle through colors
        self.set_color(self.get_color())  # set new color based on input

    def update_letter(self, event):
        if self.current_input != self.previous_input:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.current_input)# remove excess characters
        #self.current_input = self.entry.get()  # update current input
        self.set_color(self.get_color())  # set color based on input

    def get_color(self):
        if self.entry.get():
            return self.colors[self.color_index % len(self.colors)]  # cycle through colors if there is input
        else:
            return "white"  # use white color if there is no input

    def set_color(self, color):
        self.entry.config({"background": color})

# create an instance of the OneLetterInputGUI class
gui = OneLetterInputGUI()

# print the current input
print(gui.current_input)
