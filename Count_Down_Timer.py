import time
from tkinter import*
from tkinter import messagebox

root = Tk()
root.geometry = ('700x250')

root.title("Counter")

hour = StringVar()
minute = StringVar()
second=StringVar()

hour.set("00")
minute.set("00")
second.set("00")

'''Build elements'''

hourEntry = Entry(root, width=3, textvariable = hour,
                  font = ("Arial", 18, ""))
hourEntry.place(x=10,y=30)
minuteEntry = Entry(root, width=3, textvariable = minute,
                    font = ("Arial", 18, ""))
minuteEntry.place(x=80,y=30)
secondEntry = Entry(root, width=3, textvariable = second,
                    font = ("Arial", 18, ""))
secondEntry.place(x=150,y=30)


'''Build fxn'''

def submit():
    try:
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:
        mins,secs = divmod(temp,60)
        hours = 0
        if mins >60:
            hours, mins = divmod(mins, 60)
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        root.update()
        time.sleep(1)
        
        if (temp == 0):
            messagebox.showinfo("Time countdown", "Time's Up")
        temp -=1

button = Button(root, text = "Set Timer Countdown", bd = '5', command = submit)
button.place(x = 35, y=120)


'''Labels'''
h = Label (root, text = "Hour",font = ("Arial", 10, ""))
h.place(x = 10, y=5)

m = Label (root, text = "Minute",font = ("Arial", 10, ""))
m.place(x = 80, y=5)

s = Label (root, text = "Seconds",font = ("Arial", 10, ""))
s.place(x = 145, y=5)

root.mainloop()
