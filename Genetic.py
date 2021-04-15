from Board import NpBoard
from random import randrange, choice, random
from tqdm import tqdm, trange
import matplotlib.pyplot as plt
from time import time

size = 20
epsilon = 0.8
DEPSILON = 0.99
N_CHILDREN = 10
GEN_SIZE = 250
trials = 10
# b = NpBoard(size)

# chromo = [1,1,1,1]

def collisions(arr):
    cordarr = NpBoard.getCordsArray(arr)
    totcollision = 0
    for queen in cordarr:
        totcollision += (NpBoard.checkMultipleArray(cordarr, queen) - 1) 
    return totcollision

makeParent = lambda :tuple([randrange(size) for x in range(size)])

def crossover(parent1, parent2, rand=True):
    ratio = randrange(1, size)
    if rand:
        ratio = size//2
    child = parent1[:ratio] + parent2[ratio:]
    return child

def mutate(child):
    c = list(child)

    if random() < epsilon:
        n = randrange(size // 2)
        for x in range(n):
            candidate = randrange(size)
            newVal = randrange(size)
            c[candidate] = newVal

    if len(c) != len(set(c)):
        missed = set(range(size)).difference(c)
        for i, n in enumerate(c):
            if c.count(n) > 1:
                new_val = choice(list(missed))
                c[i] = new_val
                missed.remove(new_val)

    
    
    
    return tuple(c)

# gen: [
#   (parent, collisions),
#   ((3, 1, 0, 3), 6)
# 
# ]

def getLowest(gen: list, n: int):
    # lägst först
    return sorted(list(set(gen)), key=lambda x:x[1])[:n]

def genGeneration(population = 250):
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
    best = getLowest(generation, N_CHILDREN)
    while len(out) < len(generation):
        kid = crossover(choice(best)[0], choice(best)[0])
        out.append(mutate(kid))

    return out

def main():
    global epsilon
    gen0 = genGeneration()
    t = tqdm(range(200), desc='Starting')
    for gen in t:
        epsilon *= DEPSILON
        temp = solveGenetic(gen0)
        gen0 = temp
        if type(temp) == tuple:
            break
        t.set_description(f"gen: {gen}, Lowest colision: {collisions(gen0[0])}, gensize: {len(gen0)}, epsilon: {round(epsilon, 3)}")

    b = NpBoard(size=size)
    if type(gen0) == tuple:
        b.placeQueenArr(gen0)
    else:
        b.placeQueenArr(gen0[0])
    b.drawboard(2, color=True)

def tryGenSize(popSize):
    t1 = time()
    epsilon = 0.8
    DEPSILON = 0.99
    
    gen0 = genGeneration(popSize)
    t = tqdm(range(200), desc='Starting', leave=False)
    for gen in t:
        epsilon *= DEPSILON
        temp = solveGenetic(gen0)
        gen0 = temp
        if type(temp) == tuple:
            return time()-t1

        t.set_description(f"gen: {gen}, Lowest colision: {collisions(gen0[0])}, gensize: {len(gen0)}, epsilon: {round(epsilon, 3)}")
    return 0
    
        
    

def drawPlot(arr, trials=trials):
    from colour import Color    
    # sizes = [x[0] for x in arr]
    # times = [x[1] for x in arr]
    red = Color("red")
    colours = list(red.range_to(Color("green"), trials))
    for s, t in arr:
        c = colours[round(t/trials)]
        plt.bar(x=s, height=t, width=3, color=c.get_rgb() + (1,))
    plt.savefig('plot.png')
    plt.show()

if __name__ == '__main__':
    
    results = []
    t = trange(40, 210, 10, desc="Starting...")
    for popSize in t:
        for i in trange(trials, desc='trials', leave=False):
            t.set_description(f'PopSize {popSize}. Results: {len(results)}')
            # print(f"Trying size: {size} i: {i}")
            times = tryGenSize(popSize)
            if times:
                results.append((popSize, times))
    
    fixed = {}
    for popSize in range(40,210,10):
        fixed[popSize] = []
        
    for popSize, time in results:
        fixed[popSize].append(time)

    out = []
    for popSize, times in fixed.items():
        out.append((popSize, sum(times)/len(times)))

    drawPlot(out)
    # main()

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
