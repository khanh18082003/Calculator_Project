# from tkinter import Tk, W, E, Listbox
# from tkinter.ttk import Frame, Button, Style
# from tkinter.ttk import Entry
 
# class Example(Frame):
  
#  def __init__(self, parent):
#    Frame.__init__(self, parent) 
  
#    self.parent = parent
#    self.initUI()
 
  
#  def initUI(self):
  
#    self.parent.title("Calculator")
  
#    Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')
  
#    self.columnconfigure(0, pad=3)
#    self.columnconfigure(1, pad=3)
#    self.columnconfigure(2, pad=3)
#    self.columnconfigure(3, pad=3)
  
#    self.rowconfigure(0, pad=3)
#    self.rowconfigure(1, pad=3)
#    self.rowconfigure(2, pad=3)
#    self.rowconfigure(3, pad=3)
#    self.rowconfigure(4, pad=3)
  
#    listbox = Listbox(self, height=1)
#    listbox.grid(row=0, columnspan=4, sticky=W+E)
#    cls = Button(self, text="Cls", command=lambda: self.clear(listbox))
#    cls.grid(row=1, column=0)
#    bck = Button(self, text="Back")
#    bck.grid(row=1, column=1)
#    lbl = Button(self)
#    lbl.grid(row=1, column=2) 
#    clo = Button(self, text="Close", command=quit)
#    clo.grid(row=1, column=3) 
#    sev = Button(self, text="7", command=lambda:self.add_char(7, listbox))
#    sev.grid(row=2, column=0) 
#    eig = Button(self, text="8", command=lambda:self.add_char(8, listbox))
#    eig.grid(row=2, column=1) 
#    nin = Button(self, text="9", command=lambda:self.add_char(9, listbox))
#    nin.grid(row=2, column=2) 
#    div = Button(self, text="/")
#    div.grid(row=2, column=3) 
   
#    fou = Button(self, text="4", command=lambda:self.add_char(4, listbox))
#    fou.grid(row=3, column=0) 
#    fiv = Button(self, text="5", command=lambda:self.add_char(5, listbox))
#    fiv.grid(row=3, column=1) 
#    six = Button(self, text="6", command=lambda:self.add_char(6, listbox))
#    six.grid(row=3, column=2) 
#    mul = Button(self, text="*")
#    mul.grid(row=3, column=3) 
  
#    one = Button(self, text="1", command=lambda:self.add_char(1, listbox))
#    one.grid(row=4, column=0) 
#    two = Button(self, text="2",command=lambda:self.add_char(2, listbox))
#    two.grid(row=4, column=1) 
#    thr = Button(self, text="3", command=lambda:self.add_char(3, listbox))
#    thr.grid(row=4, column=2) 
#    mns = Button(self, text="-")
#    mns.grid(row=4, column=3) 
  
#    zer = Button(self, text="0", command=lambda:self.add_char(0, listbox))
#    zer.grid(row=5, column=0) 
#    dot = Button(self, text=".")
#    dot.grid(row=5, column=1) 
#    equ = Button(self, text="=")
#    equ.grid(row=5, column=2) 
#    pls = Button(self, text="+")
#    pls.grid(row=5, column=3)
  
#    self.pack()

#  def add_char(self, number, listbox):
#     listbox.insert("end", number)
#  def clear(self, listbox):
#     listbox.delete(0, "end")
 
# root = Tk()
# app = Example(root)

# root.mainloop()


from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Caculator App")
root.iconbitmap("Calculator.ico")

myImage = ImageTk.PhotoImage(Image.open("Calculator.ico"))
myLabel = Label(root, image=myImage)
myLabel.grid(row=0, column=0, columnspan=3)
entry = Entry(root, width=48, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=2, pady=5)
# entry.insert(0, "Enter")

def button_click(number):
  currentNumber = entry.get()
  entry.delete(0, END)
  entry.insert(END, str(currentNumber) + str(number))

def button_clear():
  entry.delete(0, END)

def button_add():
  global firstNum
  global operator
  operator = "addition"
  firstNum = int(entry.get())
  entry.delete(0, END)

def button_subtract():
  global firstNum
  global operator
  operator = "subtract"
  firstNum = int(entry.get())
  entry.delete(0, END)

def button_multiply():
  global firstNum
  global operator
  operator = "multiply"
  firstNum = int(entry.get())
  entry.delete(0, END)

def button_divide():
  global firstNum
  global operator
  operator = "divide"
  firstNum = int(entry.get())
  entry.delete(0, END)

def button_equal():
  secondNum = entry.get()
  entry.delete(0, END)
  if operator == "addition":
    entry.insert(0, firstNum + int(secondNum))
  
  if operator == "subtract":
    entry.insert(0, firstNum - int(secondNum))

  if operator == "multiply":
    entry.insert(0, firstNum * int(secondNum))

  if operator == "divide":
    entry.insert(0, firstNum / int(secondNum))

# define button
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
buttonAdd = Button(root, text="+", padx=39, pady=20, command=button_add)
buttonSubtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
buttonMultiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
buttonDivide = Button(root, text="/", padx=41, pady=20, command=button_divide)
buttonEqual = Button(root, text="=", padx=91, pady=20, command=button_equal)
buttonClear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)
# show button
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)

buttonAdd.grid(row=5, column=0)
buttonClear.grid(row=4, column=1, columnspan=2)
buttonSubtract.grid(row=5, column=1)
buttonMultiply.grid(row=5, column=2)
buttonDivide.grid(row=6, column=0)
buttonEqual.grid(row=6, column=1, columnspan=2)
root.mainloop()
