from tkinter import *
from gui import gui
from sudoku import sudoku

def core():
    g.pullinput()
    s=sudoku(g.m)
    if s.solve():
        g.pushoutput(s)

if __name__=='__main__':
    g=gui(core)
    g.format()
    mainloop()
