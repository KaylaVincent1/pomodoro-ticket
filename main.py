import  time
from tkinter import *
from tkinter.messagebox import showinfo

#Create an instance of Tkinter frame
root = Tk()
root.title("Pomodoro Timer")

#Set the geometry of the Tkinter frame
root.geometry("700x400")

label = Label(root, text="25:00", font=("Arial", 50))
label.config(fg="green")
label.pack(pady=20)

# Functions for each button
def start_timer():
    countdown(25 * 60)  # 25 minutes in seconds

def countdown(time):
    if time >= 0:
        mins, secs = divmod(time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=timer)
        root.after(1000, countdown, time - 1)
        if timer == "00:00":
            showinfo("Break Time!", "You can take a break!")

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