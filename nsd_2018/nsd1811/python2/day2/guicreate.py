import tkinter
from functools import partial

window = tkinter.Tk()
lb = tkinter.Label(window, text='hello john', font="Arial 20")
mybutton = partial(tkinter.Button, window, fg='yellow', bg='red')
b1 = mybutton(text='button 1')
b2 = mybutton(text='button 2')
b3 = mybutton(text='button 3')
b4 = mybutton(text='button 4')
qb = mybutton(text='QUIT')

lb.pack()
b1.pack()
b2.pack()
b3.pack()

window.mainloop()