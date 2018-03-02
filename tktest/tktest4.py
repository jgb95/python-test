import tkinter as tk

root = tk.Tk()

nameLabel = tk.Label(root, text="Name")
passLabel = tk.Label(root, text="Password")
nameEntry = tk.Entry(root)
passEntry = tk.Entry(root)

nameLabel.grid(row=0)
passLabel.grid(row=1)
nameEntry.grid(row=0, column=1)
passEntry.grid(row=1, column=1)

root.mainloop()