import tkinter as tk

root = tk.Tk()

nameLabel = tk.Label(root, text="Name")
passLabel = tk.Label(root, text="Password")
nameEntry = tk.Entry(root)
passEntry = tk.Entry(root)
loginCheckbutton = tk.Checkbutton(root, text="Keep me logged in")

nameLabel.grid(row=0, sticky=tk.E)
passLabel.grid(row=1, sticky=tk.E)
nameEntry.grid(row=0, column=1)
passEntry.grid(row=1, column=1)
loginCheckbutton.grid(columnspan=2)

root.mainloop()