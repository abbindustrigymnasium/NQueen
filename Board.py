class Board:
    def __init__(self, size=8, board=[]):
        self.queens = []
        self.queenchar = "♕"
        self.blockchar = "■"
        self.debug = []
        

        if len(board):
            if len(board[0]) != len(board):
                raise TypeError("inconsistent size")
            self.grid = board
            self.size = len(board)
            
            for i, y in enumerate(board):
                for j, x in enumerate(y):
                    if x:
                        self.queens.append((j,i))

        else:
            self.grid = [[0 for x in range(size)] for y in range(size)]
            self.size = size
            self.queens = []
    
    def updateGridFromQueens(self):
        self.grid = [[0 for x in range(self.size)] for y in range(self.size)]
        for x, y in self.queens:
            self.grid[y][x] = 1

    def drawboard(self, placements=False):

        print("-"*(self.size*4 + 1))
        for i, y in enumerate(self.grid):
            print("|", end="")
            for j, x in enumerate(y):
                if x:
                    print(f" \033[96m{self.queenchar}\033[0m |", end="")
                elif placements and not self.checkPlacement((j, i)):
                    print(f" \033[91m{self.blockchar}\033[0m |", end="")
                else:
                    print("   |", end="")
            print("\n" + "-"*(self.size*4 + 1))

    def checkPlacement(self, pos):
        for queen in self.queens:
            if queen[0] == pos[0] or queen[1] == pos[1]:
                return False
            elif abs((pos[1]-queen[1])/(pos[0]-queen[0])) == 1:
                return False
        return True
    
    @staticmethod
    def checkArray(arr, pos):
        print(arr)
        print(pos)
        for queen in arr:
            if queen[0] == arr[0] or queen[1] == arr[1]:
                return False
            elif abs((pos[1]-arr[1])/(pos[0]-arr[0])) == 1:
                return False
        return True
    
    def placeQueenArr(self, posarray):
        for i in range(self.size):
            self.queens.append((posarray[i], i))            
            self.grid[i][posarray[i]] = 1
        pass

    def placeQueen(self, pos, force=False):
        if force or self.checkPlacement(pos):
            self.queens.append(pos)
            self.updateGridFromQueens()



import numpy as np
# import numba

class NpBoard:
    def __init__(self, size: int=8, board: list=[]):
        self.queens = []
        self.queenchar = "♕"
        self.blockchar = "■"
        self.debug = []
        

        if len(board):
            if len(board[0]) != len(board):
                raise TypeError("inconsistent size")
            self.size = len(board)
            self.grid = np.zeros((self.size, self.size), dtype=bool)
            
            for i, y in enumerate(board):
                for j, x in enumerate(y):
                    self.grid[j][i] = bool(x)
                    if x:
                        self.queens.append((j,i))

        else:
            self.grid = np.zeros((size, size), dtype=bool)
            self.size = size

    def updateGridFromQueens(self):
        self.grid = np.zeros((self.size, self.size), dtype=bool)
        for x, y in self.queens:
            self.grid[y][x] = True

    def drawboard(self, placements=False):
        print("-"*(self.size*4 + 1))
        for i, y in enumerate(self.grid):
            print("|", end="")
            for j, x in enumerate(y):
                if x:
                    print(f" \033[96m{self.queenchar}\033[0m |", end="")
                elif placements and not self.checkPlacement((j, i)):
                    print(f" \033[91m{self.blockchar}\033[0m |", end="")
                else:
                    print("   |", end="")
            print("\n" + "-"*(self.size*4 + 1))

    def checkPlacement(self, pos: tuple) -> bool:
        'Returns True if placement is valid'
        for i in range(len(self.queens)):
            if self.queens[i][0] == pos[0] or self.queens[i][1] == pos[1]:
                return False
            elif abs((pos[1]-self.queens[i][1])/(pos[0]-self.queens[i][0])) == 1:
                return False
        return True
    
    @staticmethod
    def checkArray(arr, pos):
        'Returns True if placement in arr is valid'
        for queen in arr:
            if queen[0] == pos[0] or queen[1] == pos[1]:
                return False
            elif abs((pos[1]-queen[1])/(pos[0]-queen[0])) == 1:
                return False
        return True


    def placeQueenArr(self, posarray):
        for i in range(self.size):
            self.queens.append((posarray[i], i))
            self.updateGridFromQueens()

    def placeQueen(self, pos, force=False):
        if force or self.checkPlacement(pos):
            self.queens.append(pos)
            self.updateGridFromQueens()
    
# @numba.njit(gil=False)
def checkArray(arr, pos):
    'Returns True if placement in arr is valid'
    for queen in arr:
        if queen[0] == pos[0] or queen[1] == pos[1]:
            return False
        elif abs((pos[1]-queen[1])/(pos[0]-queen[0])) == 1:
            return False
    return True