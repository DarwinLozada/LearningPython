import tkinter as tk
from tkinter import *
from tkinter.font import Font


class MainFrame(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.grid()
        self.config(bg="white")

        numbers_in_labeltk = StringVar(self)

        implicitconjunt = StringVar(self)
        operationtk = StringVar(self)

        def number_function(number):
            numbers = numbers_in_labeltk.get()
            s = str(number)
            i = numbers + s
            numbers_in_labeltk.set(i)

        def function_operationbutton(symbol):
            operationtk.set(symbol)
            implicitconjunt.set(numbers_in_labeltk.get())
            numbers_in_labeltk.set("")

        def do_operation():
            result = int
            symbol = operationtk.get()
            num1 = implicitconjunt.get()
            first = int(num1)
            num2 = numbers_in_labeltk.get()
            second = int(num2)
            if symbol == "+":
                result = first + second
            elif symbol == "-":
                result = first - second
            elif symbol == "X":
                result = first * second
            elif symbol == "/":
                result = first / second
            elif symbol == "C":
                pass
            elif symbol == "CE":
                pass
            numbers_in_labeltk.set(int(result))
        myfont = Font(family="Arial", size=15)

        # Numbers Buttons

        num_pad = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]

        for index, sublist in enumerate(num_pad):
            for subindex, subvalue in enumerate(sublist):
                button = tk.Button(self, text=subvalue, command=lambda numb=subvalue: number_function(numb),
                                   relief=FLAT,
                                   font=myfont, bg="ghost white", activebackground="LightSteelBlue2")
                button.grid(row=index + 1, column=subindex, padx=3, pady=4, sticky="NSEW")

        button0 = tk.Button(self, text="0", relief=FLAT, font=myfont, bg="ghost white",
                            activebackground="LightSteelBlue2")
        button0.grid(row=4, column=1, padx=3, pady=4, sticky="NSEW")

        # Result Label

        tk.Label(self, textvariable=numbers_in_labeltk, font=myfont).grid(column=0, row=0, sticky="NSEW", columnspan=3,
                                                                          padx=2.5, pady=2.5)

        # Operations Buttons

        operations_pad = ["+", "-", "X", "/"]

        for index, indexvalueP in enumerate(operations_pad):
            buttonop = tk.Button(self, text=indexvalueP,
                                 command=lambda symbol=indexvalueP: function_operationbutton(symbol),
                                 font=myfont,
                                 relief=FLAT,
                                 activebackground="LightSteelBlue2")
            buttonop.grid(row=index, column=3, padx=3, pady=4, sticky="NSEW")

        tk.Button(self, text="C", font=myfont, command=lambda: do_operation(), relief=FLAT).grid(
            column=0, row=4, sticky="NSEW", padx=3, pady=3)
        tk.Button(self, text="CE", font=myfont, command=lambda: do_operation(), relief=FLAT).grid(
            column=2, row=4, sticky="NSEW", padx=3, pady=3)

        tk.Label(self, textvariable=numbers_in_labeltk, font=myfont).grid(column=0, row=0, sticky="NSEW",
                                                                          columnspan=3,
                                                                          padx=2.5, pady=2.5)
        # Result Button

        tk.Button(self, text="=", font=myfont, relief=FLAT, command=lambda: do_operation()) \
            .grid(column=3,
                  row=4,
                  sticky="NSEW",
                  padx=3,
                  pady=3)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)


def main():
    root = tk.Tk()
    root.title("Calculadora")
    root.minsize(300, 350)

    buttons_frame = MainFrame(root)
    buttons_frame.grid(row=0, column=0, sticky="NSEW")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    root.mainloop()


if __name__ == "__main__":
    main()
