#!C:\Software\Python\Python310\python.exe

from tkinter import *

root = Tk()
root.geometry("400x500")
expresion = ""

def setExpression(num):
    global expresion
    expresion += str(num)
    value.set(expresion)

def calculator():
    try:
        global expresion
        while (expresion.startswith('0',0,1)):
            expresion[0] = ''
        answer = str(eval(expresion))
        value.set(answer)
        expresion = ""
    except:
        value.set("Syntax Error")
        expresion = ""

def clear():
    global expresion
    expresion = ""
    value.set(expresion)

large_font = ('Verdana', 15)
small_font = ('Verdana', 10)

# Display
value = StringVar(value = 'Insert a Expresion!')
Entry(root, textvariable = value, font = large_font).grid(row=0, column=0, columnspan=4, ipadx=70)

# Buttons

Button(root, text = '/', fg = 'blue', command = lambda:
        setExpression('/'), height = 4, width = 8).grid(row = 1, column = 2, pady = 10)
Button(root, text = '*', fg = 'blue', command = lambda:
        setExpression('*'), height = 4, width = 8).grid(row = 1, column = 3, pady = 10)
Button(root, text = '7', fg = 'blue', command = lambda:
        setExpression('7'), height = 4, width = 8).grid(row = 2, column = 0, pady = 10)
Button(root, text = '8', fg = 'blue', command = lambda:
        setExpression('8'), height = 4, width = 8).grid(row = 2, column = 1, pady = 10)
Button(root, text = '9', fg = 'blue', command = lambda:
        setExpression('9'), height = 4, width = 8).grid(row = 2, column = 2, pady = 10)
Button(root, text = '-', fg = 'blue', command = lambda:
        setExpression('-'), height = 4, width = 8).grid(row = 2, column = 3, pady = 10)
Button(root, text = '4', fg = 'blue', command = lambda:
        setExpression('4'), height = 4, width = 8).grid(row = 3, column = 0, pady = 10)
Button(root, text = '5', fg = 'blue', command = lambda:
        setExpression('5'), height = 4, width = 8).grid(row = 3, column = 1, pady = 10)
Button(root, text = '6', fg = 'blue', command = lambda:
        setExpression('6'), height = 4, width = 8).grid(row = 3, column = 2, pady = 10)
Button(root, text = '+', fg = 'blue', command = lambda:
        setExpression('+'), height = 4, width = 8).grid(row = 3, column = 3, pady = 10)
Button(root, text = '1', fg = 'blue', command = lambda:
        setExpression('1'), height = 4, width = 8).grid(row = 4, column = 0, pady = 10)
Button(root, text = '2', fg = 'blue', command = lambda:
        setExpression('2'), height = 4, width = 8).grid(row = 4, column = 1, pady = 10)
Button(root, text = '3', fg = 'blue', command = lambda:
        setExpression('3'), height = 4, width = 8).grid(row = 4, column = 2, pady = 10)
Button(root, text = '0', fg = 'blue', command = lambda:
        setExpression('0'), height = 4, width = 22).grid(row = 5, column = 0, columnspan = 2, pady = 10)
Button(root, text = '.', fg = 'blue', command = lambda:
        setExpression('.'), height = 4, width = 8).grid(row = 5, column = 2, pady = 10)

# Result
Button(root, text = '=', fg = 'blue', command = calculator, height = 10, width = 8).grid(row = 4, column = 3, rowspan = 2, pady = 10)

# Clear
Button(root, text = 'AC', fg = 'blue', command = clear, height = 4, width = 22).grid(row = 1, column = 0, columnspan = 2, pady = 10)

root.mainloop()
