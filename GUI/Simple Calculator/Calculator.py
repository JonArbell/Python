import re
from tkinter import *
import tkinter.font as font
class myCalculator:
    def __init__(self,root):
        self.__root = root
        self.__root.title("Calculator")
        self.done = False
        self.oldVal = 0
        self.doneEqual = False

        # Entry
        self.entry = Entry(self.__root, borderwidth=5, width=50)
        self.entry.grid(row=0, column=0,columnspan=4)  # Column span is sasakupin lahat ng buong row, if 4 lahat ng column, 4 ang ilalagay
        self.entry.insert(0,0)

        # Clear Button
        self.buttonClear = Button(root, text="clear", padx=19,width=20 ,command=self.button_Clear)
        self.buttonClear['font'] = f
        self.buttonClear.grid(row=1, column=0,columnspan=3)

        # Delete Button
        self.buttonDelete = Button(root, text="⌫", padx=17, command=self.deleteOperator)
        self.buttonDelete['font'] = f
        self.buttonDelete.grid(row=1, column=3)

        # Divide Button
        self.buttonDivide = Button(text="÷", padx=23,command=lambda : self.addOperator("/"))
        self.buttonDivide['font'] = f
        self.buttonDivide.grid(row=2, column=3)

        # Multi Button
        self.buttonMulti = Button(text="×", padx=23,command=lambda : self.addOperator("*"))
        self.buttonMulti['font'] = f
        self.buttonMulti.grid(row=3, column=3)

        # Add Button
        self.buttonAdd = Button(text="+", padx=22,command=lambda : self.addOperator("+"))
        self.buttonAdd['font'] = f
        self.buttonAdd.grid(row=4, column=3)

        # Minus Button
        self.buttonMinus = Button(text="-", padx=24,command=lambda : self.addOperator("-"))
        self.buttonMinus['font'] = f
        self.buttonMinus.grid(row=5, column=3)

        # Equal Button
        self.buttonEqual = Button(text="=", padx=21,width=11,command=lambda :self.equal())
        self.buttonEqual['font'] = f
        self.buttonEqual.grid(row=5, column=1,columnspan=2)

    def button_Clear(self):
        self.entry.delete(0, 'end')
        self.entry.insert(0,0)
        self.oldVal = 0

    def addNumberToEntry(self,number):
        if self.entry.get() == '0':
            self.entry.delete(0, 'end')
            self.entry.insert('end', number)
        else:
            if self.doneEqual:
                self.oldVal = 0
                self.entry.delete(0, 'end')
                self.entry.insert('end', number)
                self.doneEqual = False
            else:
                self.entry.insert('end', number)


    def addOperator(self,operator):

        if len(self.entry.get()) > 0:
            if self.doneEqual:
                self.doneEqual = False
                if self.entry.get() != 'Cannot divide by 0':
                    self.oper = operator
                    self.oldVal = float(self.entry.get())
                    self.entry.delete(0, 'end')
                    self.done = True
                else:
                    self.button_Clear()
                    self.oldVal = 0
            else:
                if self.entry.get() != 'Cannot divide by 0':
                    self.oper = operator
                    self.oldVal = float(self.entry.get())
                    self.entry.delete(0, 'end')
                    self.done = True
                else:
                    self.button_Clear()
                    self.oldVal = 0



    def deleteOperator(self):
        self.entry.delete(len(self.entry.get())-1)
        if self.entry.get()=='':
            self.entry.insert('end',0)
            self.oldVal = 0

    def equal(self):
        if  len(self.entry.get())>0 and self.done:
            try:
                newVal = float(self.entry.get())

                if self.oper == '+':
                    sum = self.oldVal + newVal
                    self.entry.delete(0, 'end')
                    self.entry.insert('end', sum)

                elif self.oper == '-':
                    difference = self.oldVal - newVal
                    self.entry.delete(0, 'end')
                    self.entry.insert('end', difference)
                elif self.oper == '*':
                    product = self.oldVal * newVal
                    self.entry.delete(0, 'end')
                    self.entry.insert('end', product)
                elif self.oper == '/':
                    quotient = self.oldVal / newVal
                    self.entry.delete(0, 'end')
                    self.entry.insert('end', float(quotient))
                self.doneEqual = True
            except Exception as e:
                self.entry.delete(0, 'end')
                self.entry.insert('end',"Cannot divide by 0")

    def numbersButton(self):

        self.button7 = Button(root, text="7", padx=25,command=lambda: self.addNumberToEntry("7"))
        self.button7['font'] = f
        self.button7.grid(row=2, column=0)

        # Button 8
        self.button8 = Button(root, text="8", padx=25,command=lambda: self.addNumberToEntry("8"))
        self.button8['font'] = f
        self.button8.grid(row=2, column=1)

        # Button 9
        self.button9 = Button(root, text="9", padx=25,command=lambda: self.addNumberToEntry("9"))
        self.button9['font'] = f
        self.button9.grid(row=2, column=2)

        # Button 6
        self.button6 = Button(root, text="6", padx=25,command=lambda: self.addNumberToEntry("6"))
        self.button6['font'] = f
        self.button6.grid(row=3, column=0)

        # Button 5
        self.button5 = Button(root, text="5", padx=25,command=lambda: self.addNumberToEntry("5"))
        self.button5['font'] = f
        self.button5.grid(row=3, column=1)

        # Button 4
        self.button4 = Button(root, text="4", padx=25,command=lambda: self.addNumberToEntry("4"))
        self.button4['font'] = f
        self.button4.grid(row=3, column=2)

        # Button 1
        self.button1 = Button(root, text="1", padx=25,command=lambda: self.addNumberToEntry("1"))
        self.button1['font'] = f
        self.button1.grid(row=4, column=0)

        # Button 2
        self.button2 = Button(root, text="2", padx=25,command=lambda: self.addNumberToEntry("2"))
        self.button2['font'] = f
        self.button2.grid(row=4, column=1)

        # Button 3
        self.button3 = Button(root, text="3", padx=25,command=lambda: self.addNumberToEntry("3"))
        self.button3['font'] = f
        self.button3.grid(row=4, column=2)

        # Zero Button
        self.buttonZero = Button(text="0", padx=25,command=lambda:self.checkZeros("0"))
        self.buttonZero['font'] = f
        self.buttonZero.grid(row=5,column=0)

    def start(self):
        self.__root.mainloop()
    def checkZeros(self,zero):

        if not self.done:
            if re.match('[1-9]', self.entry.get()):
                if zero == '0':
                    self.addNumberToEntry("0")
        else:
            if zero == '0':
                self.addNumberToEntry("0")

root = Tk()
f = font.Font(family="Bell MT")
calculator = myCalculator(root)
calculator.numbersButton()
calculator.start()
