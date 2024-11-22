from tkinter import *

window = Tk()
window.title("Temperature Converter")

def tempconversion():
    f = temp1.get()
    c = (5/9) * (float(f)-32)
    temp2["text"] = f'{round(c,2)}\N{DEGREE CELSIUS}'

frame = Frame(window)
frame.grid(row=0,column=0,padx=10)

temp1 = Entry(frame, width=10)
temp1.grid(row=0,column=0)

f = Label(frame, text="\N{DEGREE FAHRENHEIT}")
f.grid(row=0, column=1)

button = Button(window, text="\N{RIGHTWARDS BLACK ARROW}", command=tempconversion, bg='sky blue')
button.grid(row=0,column=1,pady=10)

temp2 = Label(window, text="\N{DEGREE CELSIUS}")
temp2.grid(row=0,column=2,padx=10)

window.mainloop()