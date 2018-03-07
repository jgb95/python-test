import tkinter as tk
import tkinter.messagebox as messagebox

def doNothing():
  print("Okay, I won't")

root = tk.Tk()
root.geometry("500x300+60+50")



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



# ***** Status Bar *****

status = tk.Label(root, text="Preparing to do nothing...", bd=1, relief=tk.SUNKEN, anchor=tk.W, padx=5, pady=3)
status.pack(side=tk.BOTTOM, fill = tk.X)



root.mainloop()