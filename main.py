#!/usr/bin/python2.7
'''
I'm gonna "throw" random dots into a square with 1x1 unit dimensions.
Then decide if that dot landed inside or outside a circle with the
same diameter. Collect these stats into two piles, then divide inside
by outside, multiply by 4 and hopefully get a Pi. All within a GUI
with automated calculation.
'''
import math
from random import random
from Tkinter import *
import ttk
import time

main = Tk()
main.title("Darts Pi")

mainframe = ttk.Frame(main, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

main.dotsInside = IntVar()
main.dotsOutside = IntVar()
main.piCalculated = StringVar()
main.piError = StringVar()

ttk.Label(mainframe, text="Dots landed inside:").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, textvariable=main.dotsInside).grid(column=2, row=1, sticky=(N, W, E, S))

ttk.Label(mainframe, text="Dots landed outside:").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, textvariable=main.dotsOutside).grid(column=2, row=2, sticky=(N, W, E, S))

ttk.Label(mainframe, textvariable=main.piCalculated).grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, textvariable=main.piError).grid(column=2, row=3, sticky=(N, W, E, S))

class App:
  def __init__(self, master):
    main.dotsInside.set(0)
    main.dotsOutside.set(0)
    main.piCalculated.set(0.0)
    self.w = Button(main, text="Calculate", command=self.start)
    self.w.grid(column=2,row=4,sticky=(N, W, E, S))
    
  def start(self):
    self.id = self.w.after(1000, self.timer)
    self.w['command']=self.stop
    self.w['text']="Stop"
  
  def timer(self):
    self.horizShot = random()
    self.vertShot = random()
    if (((0.5-self.horizShot)**2 + (0.5-self.vertShot)**2) < 0.25):
      main.dotsInside.set(main.dotsInside.get() + 1)
    else:
      main.dotsOutside.set(main.dotsOutside.get() + 1)
    main.piCalculated.set("{0:.8f}".format((float(main.dotsInside.get()) / (main.dotsInside.get()+main.dotsOutside.get())) * 4.0))
    main.piError.set("{0:.2f}".format((float(main.piCalculated.get()) - math.pi) / math.pi * 100.0))
    self.id = self.w.after(1, self.timer)
  
  def stop(self):
    self.w['command']=self.start
    self.w['text']="Calculate"
    self.w.after_cancel(self.id)

app = App(mainframe)

main.mainloop()
