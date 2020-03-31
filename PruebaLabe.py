import tkinter as tk

root = tk.Tk()

text_var = tk.StringVar(root)
text_var.set("Hello")

l1 = tk.Label(root, textvariable=text_var)
l1.pack()

tk.Button(root, command=lambda: text_var.set("Good Bye"), text="Change").pack()

root.mainloop()
