import tkinter as tk
from tkinter.messagebox import showinfo
import tkinter.ttk

master = tk.Tk()
master.title("Sudoku Solver")


# Board space initialization
e00, e01, e02, e03, e04, e05, e06, e07, e08 = tk.Entry(
    master, width=3), tk.Entry(
        master, width=3), tk.Entry(
            master, width=3), tk.Entry(
                master, width=3), tk.Entry(
                    master, width=3), tk.Entry(
                        master, width=3), tk.Entry(
                            master, width=3), tk.Entry(
                                master, width=3), tk.Entry(
                                    master, width=3)
e10, e11, e12, e13, e14, e15, e16, e17, e18 = tk.Entry(
    master, width=3), tk.Entry(
        master, width=3), tk.Entry(
            master, width=3), tk.Entry(
                master, width=3), tk.Entry(
                    master, width=3), tk.Entry(
                        master, width=3), tk.Entry(
                            master, width=3), tk.Entry(
                                master, width=3), tk.Entry(
                                    master, width=3)
e20, e21, e22, e23, e24, e25, e26, e27, e28 = tk.Entry(
    master, width=3), tk.Entry(
        master, width=3), tk.Entry(
            master, width=3), tk.Entry(
                master, width=3), tk.Entry(
                    master, width=3), tk.Entry(
                        master, width=3), tk.Entry(
                            master, width=3), tk.Entry(
                                master, width=3), tk.Entry(
                                    master, width=3)
e30, e31, e32, e33, e34, e35, e36, e37, e38 = tk.Entry(
    master, width=3), tk.Entry(
        master, width=3), tk.Entry(
            master, width=3), tk.Entry(
                master, width=3), tk.Entry(
                    master, width=3), tk.Entry(
                        master, width=3), tk.Entry(
                            master, width=3), tk.Entry(
                                master, width=3), tk.Entry(
                                    master, width=3)
e40, e41, e42, e43, e44, e45, e46, e47, e48 = tk.Entry(
    master, width=3), tk.Entry(
        master, width=3), tk.Entry(
            master, width=3), tk.Entry(
                master, width=3), tk.Entry(
                    master, width=3), tk.Entry(
                        master, width=3), tk.Entry(
                            master, width=3), tk.Entry(
                                master, width=3), tk.Entry(
                                    master, width=3)
e50, e51, e52, e53, e54, e55, e56, e57, e58 = tk.Entry(
    master, width=3), tk.Entry(
        master, width=3), tk.Entry(
            master, width=3), tk.Entry(
                master, width=3), tk.Entry(
                    master, width=3), tk.Entry(
                        master, width=3), tk.Entry(
                            master, width=3), tk.Entry(
                                master, width=3), tk.Entry(
                                    master, width=3)
e60, e61, e62, e63, e64, e65, e66, e67, e68 = tk.Entry(
    master, width=3), tk.Entry(
        master, width=3), tk.Entry(
            master, width=3), tk.Entry(
                master, width=3), tk.Entry(
                    master, width=3), tk.Entry(
                        master, width=3), tk.Entry(
                            master, width=3), tk.Entry(
                                master, width=3), tk.Entry(
                                    master, width=3)
e70, e71, e72, e73, e74, e75, e76, e77, e78 = tk.Entry(
    master, width=3), tk.Entry(
        master, width=3), tk.Entry(
            master, width=3), tk.Entry(
                master, width=3), tk.Entry(
                    master, width=3), tk.Entry(
                        master, width=3), tk.Entry(
                            master, width=3), tk.Entry(
                                master, width=3), tk.Entry(
                                    master, width=3)
e80, e81, e82, e83, e84, e85, e86, e87, e88 = tk.Entry(
    master, width=3), tk.Entry(
        master, width=3), tk.Entry(
            master, width=3), tk.Entry(
                master, width=3), tk.Entry(
                    master, width=3), tk.Entry(
                        master, width=3), tk.Entry(
                            master, width=3), tk.Entry(
                                master, width=3), tk.Entry(
                                    master, width=3)

# Board space placement

e00.grid(
    row=0, column=0), e01.grid(
        row=0, column=1), e02.grid(
            row=0, column=2),
e03.grid(
    row=0, column=3), e04.grid(
        row=0, column=4), e05.grid(
            row=0, column=5),
e06.grid(
    row=0, column=6), e07.grid(
        row=0, column=7), e08.grid(
            row=0, column=8),

e10.grid(
    row=1, column=0), e11.grid(
        row=1, column=1), e12.grid(
            row=1, column=2),
e13.grid(
    row=1, column=3), e14.grid(
        row=1, column=4), e15.grid(
            row=1, column=5),
e16.grid(
    row=1, column=6), e17.grid(
        row=1, column=7), e18.grid(
            row=1, column=8),

e20.grid(
    row=2, column=0), e21.grid(
        row=2, column=1), e22.grid(
            row=2, column=2),
e23.grid(
    row=2, column=3), e24.grid(
        row=2, column=4), e25.grid(
            row=2, column=5),
e26.grid(
    row=2, column=6), e27.grid(
        row=2, column=7), e28.grid(
            row=2, column=8),

e30.grid(
    row=3, column=0), e31.grid(
        row=3, column=1), e32.grid(
            row=3, column=2),
e33.grid(
    row=3, column=3), e34.grid(
        row=3, column=4), e35.grid(
            row=3, column=5),
e36.grid(
    row=3, column=6), e37.grid(
        row=3, column=7), e38.grid(
            row=3, column=8),

e40.grid(
    row=4, column=0), e41.grid(
        row=4, column=1), e42.grid(
            row=4, column=2),
e43.grid(
    row=4, column=3), e44.grid(
        row=4, column=4), e45.grid(
            row=4, column=5),
e46.grid(
    row=4, column=6), e47.grid(
        row=4, column=7), e48.grid(
            row=4, column=8),

e50.grid(
    row=5, column=0), e51.grid(
        row=5, column=1), e52.grid(
            row=5, column=2),
e53.grid(
    row=5, column=3), e54.grid(
        row=5, column=4), e55.grid(
            row=5, column=5),
e56.grid(
    row=5, column=6), e57.grid(
        row=5, column=7), e58.grid(
            row=5, column=8),

e60.grid(
    row=6, column=0), e61.grid(
        row=6, column=1), e62.grid(
            row=6, column=2),
e63.grid(
    row=6, column=3), e64.grid(
        row=6, column=4), e65.grid(
            row=6, column=5),
e66.grid(
    row=6, column=6), e67.grid(
        row=6, column=7), e68.grid(
            row=6, column=8),

e70.grid(
    row=7, column=0), e71.grid(
        row=7, column=1), e72.grid(
            row=7, column=2),
e73.grid(
    row=7, column=3), e74.grid(
        row=7, column=4), e75.grid(
            row=7, column=5),
e76.grid(
    row=7, column=6), e77.grid(
        row=7, column=7), e78.grid(
            row=7, column=8),

e80.grid(
    row=8, column=0), e81.grid(
        row=8, column=1), e82.grid(
            row=8, column=2),
e83.grid(
    row=8, column=3), e84.grid(
        row=8, column=4), e85.grid(
            row=8, column=5),
e86.grid(row=8, column=6), e87.grid(row=8, column=7), e88.grid(row=8, column=8)


def pop_up(msg):
    """ Creates a pop-up with the input message. """
    showinfo(title="Error", message=msg)


def insert_zeros():
    """ Inserts a zero in every space of the board. """
    e00.insert(0, 0), e01.insert(0, 0), e02.insert(0, 0), e03.insert(0, 0), e04.insert(0, 0), e05.insert(0, 0), \
        e06.insert(0, 0), e07.insert(0, 0), e08.insert(0, 0), \
        e10.insert(0, 0), e11.insert(0, 0), e12.insert(0, 0), e13.insert(0, 0), e14.insert(0, 0), e15.insert(0, 0), \
        e16.insert(0, 0), e17.insert(0, 0), e18.insert(0, 0), \
        e20.insert(0, 0), e21.insert(0, 0), e22.insert(0, 0), e23.insert(0, 0), e24.insert(0, 0), e25.insert(0, 0), \
        e26.insert(0, 0), e27.insert(0, 0), e28.insert(0, 0), \
        e30.insert(0, 0), e31.insert(0, 0), e32.insert(0, 0), e33.insert(0, 0), e34.insert(0, 0), e35.insert(0, 0), \
        e36.insert(0, 0), e37.insert(0, 0), e38.insert(0, 0), \
        e40.insert(0, 0), e41.insert(0, 0), e42.insert(0, 0), e43.insert(0, 0), e44.insert(0, 0), e45.insert(0, 0), \
        e46.insert(0, 0), e47.insert(0, 0), e48.insert(0, 0), \
        e50.insert(0, 0), e51.insert(0, 0), e52.insert(0, 0), e53.insert(0, 0), e54.insert(0, 0), e55.insert(0, 0), \
        e56.insert(0, 0), e57.insert(0, 0), e58.insert(0, 0), \
        e60.insert(0, 0), e61.insert(0, 0), e62.insert(0, 0), e63.insert(0, 0), e64.insert(0, 0), e65.insert(0, 0), \
        e66.insert(0, 0), e67.insert(0, 0), e68.insert(0, 0), \
        e70.insert(0, 0), e71.insert(0, 0), e72.insert(0, 0), e73.insert(0, 0), e74.insert(0, 0), e75.insert(0, 0), \
        e76.insert(0, 0), e77.insert(0, 0), e78.insert(0, 0), \
        e80.insert(0, 0), e81.insert(0, 0), e82.insert(0, 0), e83.insert(0, 0), e84.insert(0, 0), e85.insert(0, 0), \
        e86.insert(0, 0), e87.insert(0, 0), e88.insert(0, 0) \



def full_delete():
    """ Clears every space on the board. """
    e00.delete(0, tk.END), e01.delete(0, tk.END), e02.delete(0, tk.END), e03.delete(0, tk.END), e04.delete(0, tk.END), \
        e05.delete(0, tk.END), e06.delete(0, tk.END), e07.delete(0, tk.END), e08.delete(0, tk.END), \
        e10.delete(0, tk.END), e11.delete(0, tk.END), e12.delete(0, tk.END), e13.delete(0, tk.END), e14.delete(0, tk.END), \
        e15.delete(0, tk.END), e16.delete(0, tk.END), e17.delete(0, tk.END), e18.delete(0, tk.END), \
        e20.delete(0, tk.END), e21.delete(0, tk.END), e22.delete(0, tk.END), e23.delete(0, tk.END), e24.delete(0, tk.END), \
        e25.delete(0, tk.END), e26.delete(0, tk.END), e27.delete(0, tk.END), e28.delete(0, tk.END), \
        e30.delete(0, tk.END), e31.delete(0, tk.END), e32.delete(0, tk.END), e33.delete(0, tk.END), e34.delete(0, tk.END), \
        e35.delete(0, tk.END), e36.delete(0, tk.END), e37.delete(0, tk.END), e38.delete(0, tk.END), \
        e40.delete(0, tk.END), e41.delete(0, tk.END), e42.delete(0, tk.END), e43.delete(0, tk.END), e44.delete(0, tk.END), \
        e45.delete(0, tk.END), e46.delete(0, tk.END), e47.delete(0, tk.END), e48.delete(0, tk.END), \
        e50.delete(0, tk.END), e51.delete(0, tk.END), e52.delete(0, tk.END), e53.delete(0, tk.END), e54.delete(0, tk.END), \
        e55.delete(0, tk.END), e56.delete(0, tk.END), e57.delete(0, tk.END), e58.delete(0, tk.END), \
        e60.delete(0, tk.END), e61.delete(0, tk.END), e62.delete(0, tk.END), e63.delete(0, tk.END), e64.delete(0, tk.END), \
        e65.delete(0, tk.END), e66.delete(0, tk.END), e67.delete(0, tk.END), e68.delete(0, tk.END), \
        e70.delete(0, tk.END), e71.delete(0, tk.END), e72.delete(0, tk.END), e73.delete(0, tk.END), e74.delete(0, tk.END), \
        e75.delete(0, tk.END), e76.delete(0, tk.END), e77.delete(0, tk.END), e78.delete(0, tk.END), \
        e80.delete(0, tk.END), e81.delete(0, tk.END), e82.delete(0, tk.END), e83.delete(0, tk.END), e84.delete(0, tk.END),
    e85.delete(
        0, tk.END), e86.delete(
        0, tk.END), e87.delete(
            0, tk.END), e88.delete(
                0, tk.END)


def sudoku(table):
    def square_set(x, y):
        """
        Given an x, y value, returns a set of values
        that exist on the same square of x, y
        """

        set_ = set()

        # assumption squares are 3 x 3 blocks

        # top x of square
        top_x = (x // 3) * 3

        # top y of square
        top_y = (y // 3) * 3

        for x in range(3):
            for y in range(3):
                if table[top_x + x][top_y + y] != 0:
                    set_.add(table[top_x + x][top_y + y])

        return set_

    def x_set(x):
        """ Given an x value, returns a set of values
        that lie on the x plane. """
        set_ = set()
        for y in range(len(table)):
            if table[x][y] != 0:
                set_.add(table[x][y])

        return set_

    def y_set(y):
        """ Given an y value, returns a set of values
        that lie on the y plane. """
        set_ = set()
        for x in range(len(table)):
            if table[x][y] != 0:
                set_.add(table[x][y])

        return set_

    def solve():

        # get next 0 x, y coord
        for x, row in enumerate(table):
            if 0 in row:
                x, y = x, row.index(0)
                break
        else:
            # no more 0s left
            return True

        # try every possible combination
        for i in range(1, 10):
            master_set = x_set(x) | y_set(y) | square_set(x, y)
            if i not in master_set:
                # Let's set table[x][y] to i and see if it works!
                table[x][y] = i

                if solve():
                    return True
                else:
                    # revert our changes
                    table[x][y] = 0

        return False

    return solve()


def collect_input():
    """ Receives all the board inputs and runs them through the sorting algorithm """
    board = [[e00.get(), e01.get(), e02.get(), e03.get(), e04.get(), e05.get(), e06.get(), e07.get(), e08.get()],
             [e10.get(), e11.get(), e12.get(), e13.get(), e14.get(), e15.get(), e16.get(), e17.get(), e18.get()],
             [e20.get(), e21.get(), e22.get(), e23.get(), e24.get(), e25.get(), e26.get(), e27.get(), e28.get()],
             [e30.get(), e31.get(), e32.get(), e33.get(), e34.get(), e35.get(), e36.get(), e37.get(), e38.get()],
             [e40.get(), e41.get(), e42.get(), e43.get(), e44.get(), e45.get(), e46.get(), e47.get(), e48.get()],
             [e50.get(), e51.get(), e52.get(), e53.get(), e54.get(), e55.get(), e56.get(), e57.get(), e58.get()],
             [e60.get(), e61.get(), e62.get(), e63.get(), e64.get(), e65.get(), e66.get(), e67.get(), e68.get()],
             [e70.get(), e71.get(), e72.get(), e73.get(), e74.get(), e75.get(), e76.get(), e77.get(), e78.get()],
             [e80.get(), e81.get(), e82.get(), e83.get(), e84.get(), e85.get(), e86.get(), e87.get(), e88.get()]]

    try:  # Check to see if all inputs are integers
        for i in range(9):
            for j in range(9):
                board[i][j] = int(board[i][j])
    except BaseException:
        pop_up("Non-integer value entered. Please try again.")
        master.mainloop()
    try:  # Check to see if all inputs are integers
        for i in range(9):
            for j in range(9):
                if board[i][j] < 0 or board[i][j] > 9:
                    raise Exception
    except BaseException:
        pop_up("Please only enter numbers between 1-9. Leave 0's for blanks!")
        master.mainloop()
    pop_up("Solving")
    if not (sudoku(board)):
        pop_up("There is no valid solution to this sudoku board.")
        master.mainloop()
    else:

        output(board)


def instructions():
    """ Specific instance of popup that displays the instructions. """
    pop_up(
        "Welcome to Sudoku Solver. Enter a valid board with numbers ranging from 1-9.\
    If a space is empty, please leave a 0 in it's respective spot. Press Solve to get the board's solution or\
           click Reset to start over.")


def full_reset():
    """ Clears the entire board and replaces it with zeroes. """
    full_delete()
    insert_zeros()


# Board set up and initialization of buttons
full_reset()
tk.Button(
    master,
    text='Reset',
    command=full_reset).grid(
        column=4,
        row=9,
        sticky=tk.W,
    pady=4)
tk.Button(
    master,
    text='Solve',
    command=collect_input).grid(
        column=3,
        row=9,
        sticky=tk.W,
    pady=4)
tk.Button(
    master,
    text='Instru',
    command=instructions).grid(
        column=3,
        row=10,
        sticky=tk.W,
    pady=4)
tk.Button(
    master,
    text='ctions',
    command=instructions).grid(
        column=4,
        row=10,
        sticky=tk.W,
    pady=4)


def output(board):
    """ Replaces the board spaces with the correct solution. """
    pop_up("Solution calculated!")
    full_delete()
    e00.insert(0, board[0][0]), e01.insert(0, board[0][1]), e02.insert(0, board[0][2]), e03.insert(0, board[0][3]), \
        e04.insert(0, board[0][4]), e05.insert(0, board[0][5]), e06.insert(0, board[0][6]), e07.insert(0, board[0][7]), \
        e08.insert(0, board[0][8]), \
        e10.insert(0, board[1][0]), e11.insert(0, board[1][1]), e12.insert(0, board[1][2]), e13.insert(0, board[1][3]), \
        e14.insert(0, board[1][4]), e15.insert(0, board[1][5]), e16.insert(0, board[1][6]), e17.insert(0, board[1][7]), \
        e18.insert(0, board[1][8]), \
        e20.insert(0, board[2][0]), e21.insert(0, board[2][1]), e22.insert(0, board[2][2]), e23.insert(0, board[2][3]), \
        e24.insert(0, board[2][4]), e25.insert(0, board[2][5]), e26.insert(0, board[2][6]), e27.insert(0, board[2][7]), \
        e28.insert(0, board[2][8]), \
        e30.insert(0, board[3][0]), e31.insert(0, board[3][1]), e32.insert(0, board[3][2]), e33.insert(0, board[3][3]), \
        e34.insert(0, board[3][4]), e35.insert(0, board[3][5]), e36.insert(0, board[3][6]), e37.insert(0, board[3][7]), \
        e38.insert(0, board[3][8]), \
        e40.insert(0, board[4][0]), e41.insert(0, board[4][1]), e42.insert(0, board[4][2]), e43.insert(0, board[4][3]), \
        e44.insert(0, board[4][4]), e45.insert(0, board[4][5]), e46.insert(0, board[4][6]), e47.insert(0, board[4][7]), \
        e48.insert(0, board[4][8]), \
        e50.insert(0, board[5][0]), e51.insert(0, board[5][1]), e52.insert(0, board[5][2]), e53.insert(0, board[5][3]), \
        e54.insert(0, board[5][4]), e55.insert(0, board[5][5]), e56.insert(0, board[5][6]), e57.insert(0, board[5][7]), \
        e58.insert(0, board[5][8]), \
        e60.insert(0, board[6][0]), e61.insert(0, board[6][1]), e62.insert(0, board[6][2]), e63.insert(0, board[6][3]), \
        e64.insert(0, board[6][4]), e65.insert(0, board[6][5]), e66.insert(0, board[6][6]), e67.insert(0, board[6][7]), \
        e68.insert(0, board[6][8]), \
        e70.insert(0, board[7][0]), e71.insert(0, board[7][1]), e72.insert(0, board[7][2]), e73.insert(0, board[7][3]), \
        e74.insert(0, board[7][4]), e75.insert(0, board[7][5]), e76.insert(0, board[7][6]), e77.insert(0, board[7][7]), \
        e78.insert(0, board[7][8]), \
        e80.insert(0, board[8][0]), e81.insert(0, board[8][1]), e82.insert(0, board[8][2]), e83.insert(0, board[8][3]), \
        e84.insert(0, board[8][4]), e85.insert(0, board[8][5]), e86.insert(0, board[8][6]), e87.insert(0, board[8][7]), \
        e88.insert(0, board[8][8])


master.mainloop()
