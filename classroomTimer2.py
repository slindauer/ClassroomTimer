import tkinter as tk
import datetime as dt
# import calendar
import time
import math


window = tk.Tk()
window.attributes('-fullscreen',True)

fontSize = 100

def close():
    window.destroy()

####### TOP FRAME
frameT = tk.Frame(bg="blue")
lbl = tk.Label(master=frameT, text="Lindauer Classroom Timer", fg="white", bg="blue", font=("Arial", 30))
lbl.pack(anchor=tk.NW, side=tk.LEFT)
btn2 = tk.Button(master=frameT, text="QUIT", command=close)
btn2.pack(anchor=tk.NE, side=tk.RIGHT)
frameT.pack(fill=tk.X)
########################


####### BOTTOM FRAMES
frameL = tk.Frame(bg="green")
frameR = tk.Frame(bg="green")

labelPeriod = tk.Label(master=frameL, text="1", font=("Arial", fontSize), fg="white", bg="green")
labelPeriod.pack()

labelTime = tk.Label(master=frameR, text="x", font=("Arial", fontSize), fg="white", bg="green")
labelTime.pack()

frameL.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frameR.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
##########################

###### end of class times
# regular days
EOCS = [(9,23),(10,8),(10,53),(11,45),(12,30),(13,43),(14,28),(15,13),(15,45)]
# Wednesdays
EOCW = [(9,23),(10,1),(10,39),(11,17),(11,55),(12,33),(13,38),(14,16),(14,45)]
# period variable
period = 1


def updateTimer():
    global period
    # all frames & labels have white on green
    colBG = "green"
    colFG = "white"
    # get the datetime for NOW
    now = dt.datetime.now()
    #dow = calendar.day_name[now.weekday()]
    if(now.weekday() == 2):
      # it is Wednesday
      eoc = dt.datetime(now.year, now.month, now.day, EOCW[period-1][0], EOCW[period-1][1], 0)
    else:
      eoc = dt.datetime(now.year, now.month, now.day, EOCS[period-1][0], EOCS[period-1][1], 0)
    if( eoc < now):
      # time for next period
      period = period + 1
      labelPeriod.config(text=period)
    else:
      # calculate time left in this period
      delta = eoc - now
      Mins = math.floor(delta.seconds/60)
      labelTime.config(text = Mins)
      # change colors based on time left in class
      if(Mins < 10):
        colFG = "black"
        colBG = "yellow"
      if(Mins < 5):
        colFG = "white"
        colBG = "red"
    # set all FG and BG colors for labels & frames
    labelTime.config(bg=colBG, fg=colFG)
    frameR.config(bg=colBG)
    frameL.config(bg=colBG)
    labelPeriod.config(bg=colBG, fg=colFG)
    labelTime.after(1000, updateTimer)
    
updateTimer()

window.mainloop()