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
        for jj in range(9):
            if self.m[i][jj]==k:
                return 0
        for ii in range(9):
            if self.m[ii][j]==k:
                return 0
        ii=(i//3)*3
        jj=(j//3)*3
        for i in range(ii,ii+3):
            for j in range(jj,jj+3):
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
