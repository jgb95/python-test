import tkinter as tk


class BuckysButtons:
  def __init__(self, master):
    frame = tk.Frame(master)
    frame.pack()

    self.printButton = tk.Button(master, text="Print Message", command=self.printMessage)
    self.printButton.pack(side=tk.LEFT)

    self.quitButton = tk.Button(master, text="Quit", command=frame.quit)
    self.quitButton.pack(side=tk.LEFT)

  def printMessage(self):
    print("Wow this actually worked!")
		


root = tk.Tk()
b = BuckysButtons(root)
root.mainloop()