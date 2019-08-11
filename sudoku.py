class sudoku():

    def __init__(self,m):
        self.m=m

    def full(self):
        for i in range(9):
            for j in range(9):
                if not self.m[i][j]:
                    return 0
        return 1

    def tile(self):
        for i in range(9):
            for j in range(9):
                if not self.m[i][j]:
                    return i,j

    def safe(self,i,j,k):
        for c in range(9):
            if self.m[i][c]==k:
                return 0
        for r in range(9):
            if self.m[r][j]==k:
                return 0
        si=(i//3)*3
        sj=(j//3)*3
        for i in range(si,si+3):
            for j in range(sj,sj+3):
                if self.m[i][j]==k:
                    return 0
        return 1

    def solve(self):
        if self.full():
            return 1
        i,j=self.tile()
        for k in range(1,10):
            if self.safe(i,j,k):
                self.m[i][j]=k
                if self.solve():
                    return 1
                else:
                    self.m[i][j]=0
        return 0
