import tkinter as tk

class Application(tk.Frame):
  def __init__(self, master=None):
    super().__init__(self, master)
    self.grid()
    self.create_widgets()


  def create_widgets(self):
    self.gram = tk.Button(self, text='Gram', width=10, command=self.gramClick)
    self.eighth = tk.Button(self, text='Eighth', width=10, command=self.eighthClick)
    self.quarter = tk.Button(self, text='Quarter', width=10, command=self.quarterClick)
    self.half = tk.Button(self, text='Half', width=10, command=self.halfClick)
    self.oz = tk.Button(self, text='Ounce', width=10, command=self.ozClick)



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

app = Application(master=root)

app.mainloop()
