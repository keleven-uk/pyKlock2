###############################################################################################################
#     pyKlock2.py   Copyright (C) <2023>  <Kevin Scott>                                                       #                                                                                                             #                                                                                                             #
#     For changes see history.txt                                                                             #
#                                                                                                             #
###############################################################################################################
#    Copyright (C) <2023>  <Kevin Scott>                                                                      #
#                                                                                                             #
#    This program is free software: you can redistribute it and/or modify it under the terms of the           #
#    GNU General Public License as published by the Free Software Foundation, either Version 3 of the         #
#    License, or (at your option) any later Version.                                                          #
#                                                                                                             #
#    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without        #
#    even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#    GNU General Public License for more details.                                                             #
#                                                                                                             #
#    You should have received a copy of the GNU General Public License along with this program.               #
#    If not, see <http://www.gnu.org/licenses/>.                                                              #
#                                                                                                             #
###############################################################################################################

from tkinter import *
from tkinter import ttk

import datetime

import src.selectTime as time
import src.utils.klock_utils as utils

current_time = time.SelectTime()



root = Tk()
root.title("Klock")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.option_add('*tearOff', FALSE)      #  Eliminate tear-off menus

klock = ttk.Frame(root, padding="3 3 12 12")
klock.grid(column=0, row=0, sticky=(N, W, E, S))
klock.columnconfigure(0, weight=1)
klock.columnconfigure(1, weight=1)
klock.columnconfigure(2, weight=1)
klock.rowconfigure(0, weight=1)
klock.rowconfigure(1, weight=1)

currentTime = StringVar()
currentDate = StringVar()
currentStts = StringVar()
currentIdle = StringVar()

time_label = ttk.Label(klock, textvariable=currentTime, text="00:00:00", font="helvetica 36")
empy_label = ttk.Label(klock, text="")
date_label = ttk.Label(klock, textvariable=currentDate, text="Date", anchor=W, relief="sunken")
stts_label = ttk.Label(klock, textvariable=currentStts, text="Status", anchor="center", relief="sunken")
idle_label = ttk.Label(klock, textvariable=currentIdle, text="Idle", anchor=E, relief="sunken")

time_label.grid(column=0, row=0, columnspan=3)
empy_label.grid(column=0, row=1)
date_label.grid(column=0, row=2, sticky=(W, E, S))
stts_label.grid(column=1, row=2, sticky=(W, E, S))
idle_label.grid(column=2, row=2, sticky=(W, E, S))


def tick():

    currentTime.set(current_time.getTime("Fuzzy Time"))

    strNow = datetime.datetime.now()
    currentDate.set(f"{ strNow:%A %d %B %Y}")

    currentStts.set(utils.get_state())

    currentIdle.set(utils.get_idle_duration())


    root.after(1000, tick)


root.after(1, tick)
root.mainloop()
