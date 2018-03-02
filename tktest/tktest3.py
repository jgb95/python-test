import tkinter as tk

root = tk.Tk()

one = tk.Label(root, text="One", bg="red", fg="white")
two = tk.Label(root, text="Two", bg="green", fg="black")
three = tk.Label(root, text="Three", bg="blue", fg="white")

one.pack()
two.pack(fill=tk.X)
three.pack(side=tk.LEFT, fill=tk.Y)

root.mainloop()