from tkinter import *
from tkinter import messagebox


class Connect4(Canvas):
    def __init__(self, master=None, size=490, grid=7):
        # set/calculate variables
        self.root = master
        self.CANVAS_SIZE = size
        self.GRID_NUM = grid
        self.GRID_SIZE = int(self.CANVAS_SIZE / self.GRID_NUM)
        self.cancelid = 0

        # initialize the canvas
        super(Connect4, self).__init__(self.root, width=self.CANVAS_SIZE, height=self.CANVAS_SIZE, bg="white")

        # draw grid
        for i in range(0, self.CANVAS_SIZE, self.GRID_SIZE):
            self.create_line(i, 0, i, self.CANVAS_SIZE)  # vertical
            self.create_line(0, i, self.CANVAS_SIZE, i)  # horizontal

        # bind mouse button clicks to their respective functions
        self.bind("<Button-1>", self.left_click)
        self.bind("<Button-3>", self.right_click)

    def convert_coords_to_circle(self, coords):
        # converts coordinates of the form (x, y) to the form (x1, y1), (x2, y2) for drawing things in the grid
        (xcoord, ycoord) = coords
        x1 = xcoord * self.GRID_SIZE
        y1 = ycoord * self.GRID_SIZE
        x2 = x1 + self.GRID_SIZE
        y2 = y1 + self.GRID_SIZE
        return x1, y1, x2, y2

    def draw_circle(self, coords, color="Black"):
        (x1, y1, x2, y2) = self.convert_coords_to_circle(coords)  # get circle coordinates
        coordtag = str(coords[0]) + "," + str(coords[1])
        self.create_oval(x1, y1, x2, y2, fill=color)  # draw circle

        # add tags for identifying each individual circle
        self.addtag_enclosed(coordtag, x1 - 1, y1 - 1, x2 + 1, y2 + 1)  # tag with x, y coordinates
        self.addtag_enclosed(color, x1 - 1, y1 - 1, x2 + 1, y2 + 1)  # color tag
        self.addtag_enclosed("circle", x1 - 1, y1 - 1, x2 + 1, y2 + 1)  # tag applied to all circles for easy deletion

    def delete_circle(self, coords):
        coordtag = str(coords[0]) + "," + str(coords[1])
        self.delete(coordtag)

    def has_piece(self, coords):
        (x1, y1, x2, y2) = self.convert_coords_to_circle(coords)
        match = self.find_enclosed(x1 - 1, y1 - 1, x2 + 1, y2 + 1)
        if match:
            tags = self.gettags(match)
            if "Blue" in tags:
                return "Blue"
            if "Red" in tags:
                return "Red"
        else:
            return None

    def drop_piece(self, col, row=-1, color="Black"):
        #self.after_cancel(self.cancelid)
        xcoord = col  # x position is always the column that the user clicked on
        ycoord = row  # start y position at the top
        if row == -1:
            self.draw_circle((xcoord, ycoord), color)  # draw initial circle

        if self.has_piece((xcoord, ycoord + 1)) is None:  # if a piece exists in the next y position, break the loop
            self.delete_circle((xcoord, ycoord))        # delete old circle
            ycoord += 1                                 # increment y position
            self.draw_circle((xcoord, ycoord), color)   # draw new circle
            if ycoord < self.GRID_NUM - 1 or self.has_piece((xcoord, ycoord + 1)):
                self.cancelid = self.after(100, self.drop_piece, xcoord, ycoord, color)
            else:
                self.calculate_win()
                #self.after_cancel(self.cancelid)

    def calculate_win(self):
        playerwon = None
        for x in range(0, self.GRID_NUM):       # loop every x position
            for y in range(0, self.GRID_NUM):   # loop every y position
                color = self.has_piece((x, y))  # get color of currently selected piece
                if self.has_piece((x, y)):
                    # horizontal right
                    if self.has_piece((x, y)) == self.has_piece((x + 1, y)) == \
                            self.has_piece((x + 2, y)) == self.has_piece((x + 3, y)):
                        playerwon = color
                    # vertical down
                    if self.has_piece((x, y)) == self.has_piece((x, y + 1)) == \
                            self.has_piece((x, y + 2)) == self.has_piece((x, y + 3)):
                        playerwon = color
                    # diagonal \
                    if self.has_piece((x, y)) == self.has_piece((x + 1, y + 1)) == \
                            self.has_piece((x + 2, y + 2)) == self.has_piece((x + 3, y + 3)):
                        playerwon = color
                    # diagonal /
                    if self.has_piece((x, y)) == self.has_piece((x - 1, y + 1)) == \
                            self.has_piece((x - 2, y + 2)) == self.has_piece((x - 3, y + 3)):
                        playerwon = color
        print("pl")
        if playerwon:  # if won, ask if user wants to play again
            play_new_game = messagebox.askyesno("Winner!", playerwon + " player has won the game!"
                                                                       "\n\nWould you like to play again?")
            if play_new_game:           # if yes
                self.delete("circle")   # clear board to start a new game
                print("cl")
            else:                       # if no
                print("ex")                  # exit the program
        return None

    def new_game(self):
        startnewgame = messagebox.askyesno("New Game", "Would you like to start a new game?")
        if startnewgame:
            self.delete("circle")

    def left_click(self, event=None):
        x = int(event.x / self.GRID_SIZE)
        #self.calculate_win()
        self.drop_piece(x, color="Blue")
        #self.calculate_win()

    def right_click(self, event=None):
        x = int(event.x / self.GRID_SIZE)
        #self.calculate_win()
        self.drop_piece(x, color="Red")
        #self.calculate_win()


class Application(Frame):
    def __init__(self, master=None, size=490, grid=7):
        self.root = master
        self.size = size
        self.grid = grid
        super(Application, self).__init__(self.root)

        self.connect = Connect4(self, size=self.size, grid=self.grid)
        self.connect.pack(side=BOTTOM, anchor=NW)

        self.menubar = Frame(self)
        self.menubar.pack(side=TOP, fill=X)
        self.newgamebutton = Button(self.menubar, text="New Game", padx=2, pady=2, command=self.connect.new_game)
        self.newgamebutton.pack(side=LEFT, anchor=W)
        self.quitbutton = Button(self.menubar, text="Quit", padx=2, pady=2, command=exit)
        self.quitbutton.pack(side=LEFT, anchor=W)

        self.pack()


def main():
    root = Tk()
    size = 560
    num_grids = 7

    window_offset = (int((root.winfo_screenwidth() - size) / 2), int((root.winfo_screenheight() - size) / 2))

    root.title("Connect Four")
    root.geometry("+%d+%d" % window_offset)

    app = Application(master=root, size=size, grid=num_grids)
    app.mainloop()


if __name__ == '__main__':
    main()
