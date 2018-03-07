import tkinter as tk

root = tk.Tk()
root.geometry("500x300+60+50")

canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()


blackline = canvas.create_line(0,0, 200,50)
redline = canvas.create_line(0,100, 200,50, fill="red")

root.mainloop()