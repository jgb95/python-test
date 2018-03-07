import tkinter as tk
import tkinter.messagebox as messagebox

root = tk.Tk()
root.geometry("500x300+60+50")

answer = messagebox.askquestion("Question Tit", "Do you like weed?")
if answer == "yes":
  messagebox.showinfo("Window Tit", "Secret message hahahaha....")

root.mainloop()