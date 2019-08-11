from tkinter import *
from gui import gui
from sudoku import sudoku

def core():
    g.pullinput()
    s=sudoku(g.m)
    if s.solve():
        g.pushoutput(s)

def main():
    global g
    g=gui(core)
    g.format()
    mainloop()

if __name__=='__main__':
    main()
