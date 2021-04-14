from Board import NpBoard
from random import randrange

size = 4
# b = NpBoard(size)

# chromo = [1,1,1,1]

def collisions(arr):
    cordarr = NpBoard.getCordsArray(arr)
    totcollision = 0
    for queen in cordarr:
        totcollision += (NpBoard.checkMultipleArray(cordarr, queen) - 1) 
    return totcollision

makeParent = lambda :[randrange(size) for x in range(size)]

def crossover(parent1, parent2):
    ratio = randrange(1, size)
    child = parent1[:ratio] + parent2[ratio:]
    return child

def mutate(child):
    n = randrange(size // 2)
    for x in range(n):
        candidate = randrange(size)
        newVal = randrange(size)
        child[candidate] = newVal
    
    return child
# gen: [
#   (parent, collisions),
#   ((3, 1, 0, 3), 6)
# 
# ]

def solveGenetic(): 
    generation = [makeParent for x in range(size)]
    print(generation)
    for i in range(6):
        parent = makeParent()
        generation[i][1] = collisions(parent)
    return generation

# def getLowest(gen: list, n: int):
#     out = gen[:]
#     out.sort(key=lambda x:x[1])

#     for x in out:
        

#     return

# print(NpBoard.getCordsArray([1,1,1,1]))
solveGenetic()

# p1 = makeParent()
# p2 = makeParent()
# print("p1: \t", p1)
# print("p2: \t", p2)

# kid = crossover(p1, p2)
# print("kid:\t", kid)
# newKid = mutate(kid)
# print("newKid: ", newKid)
# b = NpBoard(board=newKid)

# b.drawboard(2, color=False)

# print(totcollision)
