from tkinter import *
import tkinter.messagebox
# ============== settings ==============
root = Tk()
root.title("Calculator")
root.geometry("300x160")
root.resizable(width=False, height=False)
root.configure(bg="light grey")
# ============== Variables ==============
num1 = StringVar()
num2 = StringVar()
result = StringVar()
# ============== Frames ==============
firstFrame = Frame(root, width=300, height=40, bg='light grey')
firstFrame.pack(side=TOP)
secondFrame = Frame(root, width=300, height=40, bg='light grey')
secondFrame.pack(side=TOP)
thirdFrame = Frame(root, width=300, height=40, bg='light grey')
thirdFrame.pack(side=TOP)
fourthFrame = Frame(root, width=300, height=40, bg='light grey')
fourthFrame.pack(side=TOP)
# ============== Functions ==============


def errormessage(text):
    if text == "error":
        tkinter.messagebox.showerror("Error", "Something went wrong.")
    elif text == "Division Error":
        tkinter.messagebox.showerror("Error", "You can not divide a number into zero.")


def plus():
    try:
        value = float(num1.get())+float(num2.get())
        result.set(value)
    except:
        errormessage("error")


def minus():
    try:
        value = float(num1.get()) - float(num2.get())
        result.set(value)
    except:
        errormessage("error")


def multiple():
    try:
        value = float(num1.get()) * float(num2.get())
        result.set(value)
    except:
        errormessage("error")


def division():
    if num2.get() == "0":
        errormessage("Division Error")
    else:
        try:
            value = float(num1.get()) / float(num2.get())
            result.set(value)
        except:
            errormessage("error")
# ============== Labels and entries ==============


firstLabel = Label(firstFrame, text="First number:", bg="light grey")
firstLabel.pack(side=LEFT, padx=5, pady=5)

firstLabelEntry = Entry(firstFrame, textvariable=num1)
firstLabelEntry.pack(side=LEFT, padx=5, pady=5)

secondLabel = Label(secondFrame, text="Second number:", bg="light grey")
secondLabel.pack(side=LEFT, padx=5, pady=5)

secondLabelEntry = Entry(secondFrame, textvariable=num2)
secondLabelEntry.pack(side=LEFT, padx=5, pady=5)

bottommostLabel = Label(fourthFrame, text="Result:", bg="light grey")
bottommostLabel.pack(side=LEFT, padx=5, pady=5)

bottommostLabelEntry = Entry(fourthFrame, textvariable=result)
bottommostLabelEntry.pack(side=LEFT, padx=5, pady=5)

# ============== Buttons ==============
sumButton = Button(thirdFrame, text="+", width=4, command=lambda: plus())
sumButton.pack(side=LEFT, padx=10, pady=10)

minButton = Button(thirdFrame, text="-", width=4, command=lambda: minus())
minButton.pack(side=LEFT, padx=10, pady=10)

mulButton = Button(thirdFrame, text="×", width=4, command=lambda: multiple())
mulButton.pack(side=LEFT, padx=10, pady=10)

divButton = Button(thirdFrame, text="÷", width=4, command=lambda: division())
divButton.pack(side=LEFT, padx=10, pady=10)




























root.mainloop()

