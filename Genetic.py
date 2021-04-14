from Board import NpBoard
from random import randrange, choice
from tqdm import tqdm

size = 28
# b = NpBoard(size)

# chromo = [1,1,1,1]

def collisions(arr):
    cordarr = NpBoard.getCordsArray(arr)
    totcollision = 0
    for queen in cordarr:

        totcollision += (NpBoard.checkMultipleArray(cordarr, queen) - 1) 
    return totcollision

makeParent = lambda :tuple([randrange(size) for x in range(size)])

def crossover(parent1, parent2):
    ratio = randrange(1, size)
    child = parent1[:ratio] + parent2[ratio:]
    return child

def mutate(child):
    c = list(child)
    n = randrange(size // 2)
    for x in range(n):
        candidate = randrange(size)
        newVal = randrange(size)
        c[candidate] = newVal
    
    return tuple(c)

# gen: [
#   (parent, collisions),
#   ((3, 1, 0, 3), 6)
# 
# ]

def getLowest(gen: list, n: int):
    # lägst först
    return sorted(list(set(gen)), key=lambda x:x[1])[:n]

def genGeneration(population = 500):
    # generation = []
    # for i in range(population):
    #     parent = makeParent()
    #     generation.append((parent, collisions(parent)))
    return [makeParent() for i in range(population)]

def solveGenetic(parents): 
    generation = []
    for parent in parents:
        col = collisions(parent)
        if col == 0:
            return parent          
        generation.append((parent, collisions(parent)))

    out = []
    best = getLowest(generation, len(generation)//50)
    while len(out) < len(generation):
        kid = crossover(choice(best)[0], choice(best)[0])
        out.append(kid)
        out.append(mutate(kid))

    return out

gen0 = genGeneration()
t = tqdm(range(1000), desc='Starting')
for gen in t:
    temp = solveGenetic(gen0)
    gen0 = temp
    if type(temp) == tuple:
        break
    t.set_description(f"gen: {gen}, Lowest colision: {collisions(gen0[0])}")

b = NpBoard(size=size)
if type(gen0) == tuple:
    b.placeQueenArr(gen0)
else:
    b.placeQueenArr(gen0[0])
b.drawboard(2, color=True)

# print(NpBoard.getCordsArray([1,1,1,1]))

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
