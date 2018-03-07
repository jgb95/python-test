import tkinter as tk

def doNothing():
  print("Okay, I won't")

root = tk.Tk()
root.geometry("500x300+500+200")

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

root.mainloop()