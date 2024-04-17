import ttkbootstrap as tb
from  tkinter import *
import time
import pygame


pygame.mixer.init()
beep = pygame.mixer.Sound('beep-07a.wav')
font1= ("helvetica", 20)
root = tb.Window(themename= "vapor")
root.title("Time countdown")


#seconds
lab_s =tb.Label(root,text="Seconds : ",style="danger",font=font1)
lab_s.grid(row="0",column="0")
spin_s = tb.Spinbox(root, style="danger", from_=0, to=59,font=font1)
spin_s.grid(row="0", column="1")
spin_s.set(0)

#minutes
lab_m = tb.Label(root,text="minutes : ",style="warning",font=font1)
lab_m.grid(row="1",column="0")
spin_m = tb.Spinbox(root, style="warning", from_=0, to=59,font=font1)
spin_m.grid(row="1", column="1")
spin_m.set(0)

#hours
lab_h = tb.Label(root,text="hour : ",style="success",font=font1)
lab_h.grid(row="2",column="0")
spin_h = tb.Spinbox(root, style="danger", from_=0, to=23,font=font1)
spin_h.grid(row="2", column="1")
spin_h.set(0)

def count_down():
    min = int(spin_m.get())
    sec = int(spin_s.get())
    hr= int(spin_h.get())
    timee = (min * 60) + (hr * 3600) + (sec  *1)
    
    for x in range(timee,0,-1):
        #print (f"{hr:02d}:{min:02d}:{sec:02d}")
        #use above code only if we want to check whether its working
        root.after(1000)
        
    label = tb.Label(root, text="TIME IS UP!!", style="light",font=font1)
    label.grid(row="3",column="1")
    beep.play()
        
    
#button
but = tb.Button(root, text="start", style="info ,outline", command= count_down)
but.grid(row="3", column="0")  
    


root.mainloop()