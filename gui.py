from tkinter import *

class gui():

    def __init__(self,core):
        self.w=Tk()
        self.b=Button(self.w,text='solve',command=core)
        self.m=[[0 for i in range(9)] for i in range(9)]

    def format(self):
        self.w.title('Sudoku Solver')
        self.b.grid(row=0,column=10)
        for i in range(9):
            for j in range(9):
                self.m[i][j]=Entry(self.w,width=2)
                self.m[i][j].grid(row=i,column=j)

    def pullinput(self):
        for i in range(9):
            for j in range(9):
                self.m[i][j]=self.m[i][j].get()
                if self.m[i][j]:
                    self.m[i][j]=int(self.m[i][j])
                else:
                    self.m[i][j]=0

    def pushoutput(self,s):
        self.m=s.m
        for i in range(9):
            for j in range(9):
                l=Label(self.w,text=str(self.m[i][j]))
                l.grid(row=i,column=j)
        Label(self.w,text='Solved!').grid(row=0,column=10)
