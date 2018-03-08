import tkinter as tk


class Application():
  def __init__(self, master=None):
    self.root = master

    self.gram = tk.Button(self.root, text='Gram', width=10, command=self.gramClick)
    self.eighth = tk.Button(self.root, text='Eighth', width=10, command=self.eighthClick)
    self.quarter = tk.Button(self.root, text='Quarter', width=10, command=self.quarterClick)
    self.half = tk.Button(self.root, text='Half', width=10, command=self.halfClick)
    self.oz = tk.Button(self.root, text='Ounce', width=10, command=self.ozClick)

    self.gram.grid(column=1,row=1)
    self.eighth.grid(column=1,row=2)
    self.quarter.grid(column=1,row=3)
    self.half.grid(column=1,row=4)
    self.oz.grid(column=1,row=5)

  def gramClick(self):
    print('You selected a gram!')

  def eighthClick(self):
    print('You selected a eighth!')

  def quarterClick(self):
    print('You selected a quarter!')

  def halfClick(self):
    print('You selected a half!')

  def ozClick(self):
    print('You selected an ounce!')


root = tk.Tk()
root.geometry("200x200+50+60")

app = Application(master=root)

root.mainloop()
