import time
from tkinter import *
from tkinter.messagebox import showinfo

# Create an instance of Tkinter frame
root = Tk()
root.title("Pomodoro Timer")

# Set the geometry of the Tkinter frame
root.geometry("700x400")

label = Label(root, text="25:00", font=("Arial", 50))
label.config(fg="green")
label.pack(pady=20)

timer_id = None
time_remaining = 25 * 60  # 25 minutes in seconds
paused = False

# Functions for each button
def start_timer():
    global paused
    if paused:
        resume_timer()
    else:
        countdown(time_remaining)


def countdown(time):
    global timer_id, time_remaining
    if time >= 0:
        mins, secs = divmod(time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=timer)
        time_remaining = time
        timer_id = root.after(1000, countdown, time - 1)
    else:
        showinfo("Break Time!", "You can take a break!")


def pause_timer():
    global timer_id, paused
    label.config(text="Timer Paused")
    if timer_id:
        root.after_cancel(timer_id)  # Cancel the ongoing countdown
        timer_id = None
        paused = True
        label.config(text="Timer Paused")

def resume_timer():
    global paused
    paused = False
    countdown(time_remaining)



def reset_timer():
    global timer_id, time_remaining, paused
    if timer_id:
        root.after_cancel(timer_id)
        timer_id = None
    time_remaining = 25 * 60  # Reset time to 25 minutes
    paused = False
    label.config(text="25:00")



# Create a frame to hold the buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

# Create Multiple Buttons with different commands
button_dict = {}
options = {"Start": start_timer, "Pause": pause_timer, "Reset": reset_timer}

for text, func in options.items():
    button_dict[text] = Button(root, text=text, width=25, command=func)
    button_dict[text].pack(side=LEFT, padx=25)

root.mainloop()
