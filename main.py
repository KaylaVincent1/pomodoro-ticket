import  time
from tkinter import *

#Create an instance of Tkinter frame
root = Tk()
root.title("Pomodoro Timer")

#Set the geometry of the Tkinter frame
root.geometry("700x400")

timer = "25:00"

label = Label(root, text=f"""{timer}""", font=("Arial", 50))
label.config(fg="green")
label.pack(pady=20)

# Functions for each button
def start_timer():
    label.config(text="Timer Started")




def pause_timer():
    label.config(text="Timer Paused")

def reset_timer():
    label.config(text="25:00")

# Create a frame to hold the buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

#Create Multiple Buttons with different commands
button_dict = {}
options = {"Start":start_timer, "Pause":pause_timer, "Reset":reset_timer}

for text, func in options.items():
    button_dict[text] = Button(root, text=text, width=25, command=func)
    button_dict[text].pack(side=LEFT, padx=25)

root.mainloop()