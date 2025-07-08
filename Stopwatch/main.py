# ***** IMPORTS *****
from tkinter import *
from customtkinter import *
import os

# ***** CLASS *****
class Stopwatch():
    def __init__(self, root):
        self.root = root

        # ***** GUI *****
        self.root.title("Stopwatch")
        self.root.geometry('380x250')
        self.root.resizable(False, False)

        # ***** VARIABLES *****
        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.pinned = False

        # colours
        background = "#DBEAFE"
        
        # ***** SETTINGS *****
        # favicon
        icon_path = os.path.join(os.path.dirname(__file__), "img", "icon.ico")
        root.iconbitmap(icon_path)
        
        # background
        root.configure(bg=background)

        # ***** WIDGETS *****
        # header frame
        header_frame = Frame(root, bg=background)
        header_frame.pack()
        
        # timer frame
        timer_frame = Frame(root, bg=background)
        timer_frame.pack()

        # button frame
        button_frame = Frame(root, bg=background)
        button_frame.pack()
    
        # timer label
        self.timer_label = Label(timer_frame, text='00:00:00', font=('Arial', 30, 'bold'), bg=background)
        self.timer_label.pack(pady=35)

        # start button
        self.start_button = CTkButton(button_frame, text='Start', font=('Arial', 20), width=10, command=self.start)
        self.start_button.pack(side=LEFT, padx=5, ipadx=10, ipady=5)

        # pause button
        self.pause_button = CTkButton(button_frame, text='Pause', font=('Arial', 20), width=10, command=self.pause)
        self.pause_button.pack(side=LEFT, padx=5, ipadx=10, ipady=5)

        # reset button
        self.reset_button = CTkButton(button_frame, text='Reset', font=('Arial', 20), width=10, command=self.reset)
        self.reset_button.pack(side=LEFT, padx=5, ipadx=10, ipady=5)

        # quit button
        self.quit_button = CTkButton(button_frame, text='Quit', font=('Arial', 20), width=10, command=root.quit)
        self.quit_button.pack(side=LEFT, padx=5, ipadx=10, ipady=5)

        # pin button
        pin_image = os.path.join(os.path.dirname(__file__), "img", "pin.png")
        self.pin_img = PhotoImage(file=pin_image)

        self.pin_button = CTkButton(header_frame, image=self.pin_img, text="Pin", font=('Arial', 15), corner_radius=20, command=self.pin)
        self.pin_button.pack(pady=(30, 0))


    # ***** FUNCTIONS *****
    # update function
    def update(self):
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
        if self.minutes == 60:
            self.hours += 1
            self.minutes = 0

        timer_text = f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
        self.timer_label.config(text=timer_text)
        self.update_time = self.root.after(1000, self.update)

    # start function
    def start(self):
        if not self.running:
            self.update()
            self.running = True

    # pause function
    def pause(self):
        if self.running and self.update_time:
            self.root.after_cancel(self.update_time)
            self.running = False

    # reset function
    def reset(self):
        if self.update_time is not None:
            self.timer_label.after_cancel(self.update_time)
            self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.timer_label.config(text='00:00:00')

    # pin bar
    def pin(self):
        self.pinned = not self.pinned
        self.root.attributes("-topmost", self.pinned)
        self.pin_button.configure(text="Unpin" if self.pinned else "Pin")

# ***** STARTING *****
root = Tk()
app = Stopwatch(root)
root.mainloop()