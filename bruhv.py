import os
import time
from tkinter import *
import webbrowser


activated = 0

def pp(var):
    print(var)
    activated = 1
    

# root / tk setup

root = Tk()
canvas = Canvas(height=500,width=750)
canvas.pack()
T = Text(root, height=2, width=30)
T.pack()
T.insert(END, "would you like a virus?\nType \'yes\'")

# ui setup, credit: Stack overflow dude

messages = Text(canvas)
messages.pack()

input_user = StringVar()
input_field = Entry(canvas, text=input_user)
input_field.pack(side=BOTTOM)

def Enter_pressed(event):
    input_get = input_field.get()
    print(input_get)
    # messages.insert(INSERT, '%s\n' % input_get)
    #  label = Label(window, text=input_get)
    # input_user.set('')
    #  label.pack()
    # return "break"
    if input_get == "yes":
        print("niggbob")
        for x in range(10):
            webbrowser.open('https://www.youtube.com/watch?v=2ZIpFytCSVc')
            
        time.sleep(10.0)
        os.system("TASKKILL /F /IM chrome.exe")

frame = Frame(canvas)  # , width=300, height=300)
input_field.bind("<Return>", Enter_pressed)
frame.pack()

# if input, virus


root.mainloop()

