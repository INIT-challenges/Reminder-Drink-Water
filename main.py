import os
from threading import Thread
from tkinter import *
import time
from tkinter import messagebox

from TimerModule import start_music

seconds_to_sip = 15 * 60

class main_window:

    def decrement(self):
        while self.temp > -1:
            mins, secs = divmod(self.temp, 60)
            self.minute['text'] = "{:02d}".format(mins)
            self.second['text'] = "{:02d}".format(secs)
            self.root.update()
            time.sleep(1)

            if (self.temp == 0):
                start_music(os.path.abspath("audio/YTCartoonMetalThunk.mp3"), 13, 1, 1)
                messagebox.showinfo("Water", "DRINK WATER")
            self.temp -= 1

        self.start["state"] = 'active'

    def reset_timer(self):
        self.temp = seconds_to_sip
        if not self.timer_already_running:
            self.start_timer()

    def start_timer(self):
        # reset temp
        self.timerThread = Thread(target=self.decrement())
        self.timerThread.start()
        self.timerThread.join()
        self.start["state"] = 'disabled'

    def __init__(self):
        self.temp = seconds_to_sip
        self.timer_already_running = False

        self.root = Tk()
        self.root.geometry('400x300')
        self.root.title("Drink water reminder")

        self.minute = Label(self.root, text="15", width=4, font=("bold", 18), bg='grey')
        self.minute.place(x=50, y=40)

        self.second = Label(self.root, text="00", width=4, font=("bold", 18), bg='grey')
        self.second.place(x=130, y=40)

        self.colon = Label(self.root, text=":", width=1, font=("bold", 18))
        self.colon.place(x=110, y=40)

        self.root.iconbitmap("images/water.ico")

        self.name = Label(self.root, text="Time to next sip", width=20, font=("bold", 10))
        self.name.place(x=30, y=20)

        self.reset = Button(self.root,
                             text='Reset',
                             width=9,
                             bg='brown',
                             fg='white',
                             command=lambda: self.reset_timer())
        self.reset.place(x=40, y=90)

        self.start = Button(self.root,
                            text='Start',
                            width=9,
                            bg='brown',
                            fg='white',
                            command=lambda: self.start_timer())

        self.start.place(x=130, y=90)

        self.root.mainloop()
        print("main window created!")

if __name__ == "__main__":
    root1 = main_window()

