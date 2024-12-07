import  time
from cProfile import label
from tkinter import *

#Create an instance of Tkinter frame
root = Tk()
root.title("Pomodoro Timer")

#Set the geometry of the Tkinter frame
root.geometry("700x400")

label = Label(root, text="00:00")
label.pack(pady=20)


# Create a frame to hold the buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

#Create Multiple Buttons with different commands
button_dict = {}
option = ["Start", "Pause", "Reset"]

for i in option:
    button_dict[i] = Button(root, text=i, width=25)
    button_dict[i].pack(side=LEFT, padx=25)

root.mainloop()