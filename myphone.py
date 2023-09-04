from tkinter import *


ui=Tk()
Val = Entry(ui, width=50, borderwidth=3)
Val.insert(0,"Enter Ph no. with Country code and click Enter")
Val.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def myclick():
    global number
    number=Val.get()
    Val.delete(0,END)
    ui.destroy()


mybutton=Button(ui,text="Enter",padx=50,pady=10,command=myclick)
mybutton.grid()


ui.mainloop()