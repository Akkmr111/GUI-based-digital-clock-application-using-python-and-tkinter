from tkinter import Label, Tk
import time
root = Tk()
root.title("Digital Clock")
root.geometry("1080x300")

label = Label(root, font='Boulder 200 bold', bg='black', fg='red', bd=6)
label.grid(row=0, column=1)
def digital_clock():
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live)
   label.after(200, digital_clock)
digital_clock()
root.mainloop()