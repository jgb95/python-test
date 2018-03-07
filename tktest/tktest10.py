import tkinter as tk

def doNothing():
  print("Okay, I won't")

root = tk.Tk()
root.geometry("500x300+500+200")

# ***** Main Menu *****

mainMenu = tk.Menu(root)
root.config(menu=mainMenu)

fileMenu = tk.Menu(mainMenu, tearoff=0)
editMenu = tk.Menu(mainMenu, tearoff=0)
openRecentMenu = tk.Menu(fileMenu, tearoff=0)

mainMenu.add_cascade(label="File", menu=fileMenu)
mainMenu.add_cascade(label="Edit", menu=editMenu)

fileMenu.add_command(label="New...", command=doNothing)
fileMenu.add_cascade(label="Open Recent...", menu=openRecentMenu)
fileMenu.add_command(label="Save...", command=doNothing)

openRecentMenu.add_command(label="Reopen closed file...", command=doNothing)

editMenu.add_command(label="Undo...", command=doNothing)

# ***** Toolbar *****

toolbar = tk.Frame(root, bg="grey")

insertButt = tk.Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=tk.LEFT, padx=2, pady=2)
printButt = tk.Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=tk.LEFT, padx=2, pady=2)

toolbar.pack(side=tk.TOP, fill=tk.X)


root.mainloop()