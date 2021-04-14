# Board:
# 1 = queen
# 0 = empty
# [
#     [0, 0, 0, 0],
#     [0, 1, 0, 0],
#     [0, 0, 0, 1],
#     [1, 0, 0, 0],
# ]

from Board import Board, NpBoard



from random import randrange
from time import time
from tqdm import tqdm



# import numbatest


size = 28
b = NpBoard(size=size)
queens = []
i = 0
t = tqdm()

def recursiveTester(row, startcol = 0) -> bool:
    global i
    i += 1
    t.update()
    if row >= size:
        return True
    for col in range(startcol, size + startcol):
        if NpBoard.checkArray(queens, (col%size, row)):
            queens.append((col%size, row))
            if recursiveTester(row + 1): 
                return True
            queens.pop()
    return False 
    

if recursiveTester(0, 0):
    result = []
    for x in queens:
        result.append(x[0])
    b.placeQueenArr(result)
    print()
    b.drawboard(True)
    print("Done")
else:
    print("No possible solution")
print(f"Tried {i} solutions")

# n = 100
# size = 8

# # b = Board()
# # b.placeQueenArr([1,1,1,1,1,1,1,1])
# # b.drawboard()

# for x in range(n+1):
# # for x in range(4):
#     t1 = time()
#     while 1:
#         b = NpBoard(size)
#         # print("!!!")
#         a = 0
#         while a != x:
#         # while len(b.queens) < 5:
#             b.placeQueen((randrange(size),randrange(size)))
#             # print(i)
#             if t1 + 20 < time():
#                 break
#             a += 1 
#         if len(b.queens) == x or t1 + 20 < time():
#             break
        
#     if t1 + 20 < time():
#         print("timeout 20 sec")
#         break
#     t2 = time()
#     b.drawboard(True)

#     print(len(b.queens))
#     print(f"Det tog {t2-t1} sekunder")

# print("\n".join(b.debug))

# board=[
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 1, 0],
#     [0, 0, 0, 0],
# ]