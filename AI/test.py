import random
import functools
import matplotlib.pyplot as plt
import time
import numpy

def initpopulation():
    popsize = 20
    initpop = []
    for _ in range(popsize):
        inity = [random.randint(0,7)]*8
        initpop.append(''.join([str(elem) for elem in inity]))    
    return initpop

def fitness(instance):
    nonconflictpairs=0
    for ind,gene in enumerate(instance):
        for oind,ogene in enumerate(instance):
            if oind>ind:
                if gene!=ogene:
                    if (ogene>gene and int(ogene)-(oind-ind)!=int(gene)) or (ogene<gene and int(ogene)+(oind-ind)!=int(gene)):
                        nonconflictpairs+=1
    return nonconflictpairs+1

def reproduce(x,y):
    c = random.randint(0,7)
    return x[:c+1] + y[1+c:]

def mutate(x):
    ind1 = random.randint(0,7)
    place1 = random.randint(0,7)
    x = x[:ind1] + str(place1) + x[ind1+1:]
    return x

def compare(chrom1,chrom2):
    return (fitness(chrom2)-fitness(chrom1))

def survive(n,population,fitness):
    popunique = numpy.unique(population)
    if len(popunique)>n:
        poplist = list(popunique)
    else:
        poplist = population
    poplist.sort(key=functools.cmp_to_key(compare))
    newpoplist=poplist[0:int(0.85*n)+1]
    for _ in range(int(0.15*n)):
        newpoplist.append(random.choice(poplist[int(0.85*n)+1:]))
    return newpoplist

def pickrand(population,fitness):
    maxfit=max([fitness(elem) for elem in population])
    weights=[]
    for elem in population:
        weights.append(fitness(elem)/maxfit)
    return random.choices(population,weights)[0]

def genalgo(population,fitness):
    gagraphx=[]
    gagraphy=[]
    generation=0
    doneflag=False
    while(True) and not doneflag:
        generation+=1
        newpop = []

        n = len(population)
        for _ in range(n):
            x = pickrand(population,fitness)
            y = pickrand(population,fitness)
            while y==x:
                y = pickrand(population,fitness)
            
            child=reproduce(x,y)
            if fitness(child)==29:
                print("found",child)
                print(generation)
                gagraphx.append(generation)
                gagraphy.append(29)
                doneflag=True
                break

            m = random.random()
            if m<=0.03:
                child=mutate(child)
            if fitness(child)==29:
                print("bruh",child)
                print(generation)
                gagraphx.append(generation)
                gagraphy.append(29)
                doneflag=True
                break
            newpop.append(child)
        population = newpop

        fitmax=max([fitness(elem) for elem in population])
        gagraphx.append(generation)
        gagraphy.append(fitmax)
        if generation%100==0:
            print(generation)
            print("max ",fitmax)
            print(numpy.mean([fitness(elem) for elem in population]))
    return gagraphx,gagraphy

def genalgobetter(population,fitness):
    generation=0
    gabgraphx=[]
    gabgraphy=[]
    doneflag=False
    while(True) and not doneflag:
        generation+=1
        newpop = []

        n = len(population)
        while len(newpop)<20:
            x = pickrand(population,fitness)
            y = pickrand(population,fitness)
            while y==x:
                y = pickrand(population,fitness)
            
            # print("Reproducing ",x, "and ",y)
            child=reproduce(x,y)
            if fitness(child)==9:
                print("found",child)
                print(generation)
                gabgraphx.append(generation)
                gabgraphy.append(9)
                doneflag=True
                break

            m = random.random()
            if m<=0.1:
                # print("Mutating ",child)
                child=mutate(child)
            if fitness(child)==9:
                print("bruh",child)
                print(generation)
                gabgraphx.append(generation)
                gabgraphy.append(9)
                doneflag=True
                break
            newpop.append(child)
        population.extend(newpop)
        population=survive(20,population,fitness)
        fitmax=max([fitness(elem) for elem in population])
        gabgraphx.append(generation)
        gabgraphy.append(fitmax)
    return gabgraphx,gabgraphy

startpop=initpopulation()
x1,y1 = genalgobetter(startpop,fitness)
plt.plot(x1,y1, label = 'better')
x2,y2 = genalgo(startpop,fitness)
plt.plot(x2,y2 , label = 'original')
plt.show()
# plt.plot(genalgobetter(startpop,fitness)[0],genalgobetter(startpop,fitness)[1])
# plt.show()
# plt.plot(genalgo(startpop,fitness)[0],genalgo(startpop,fitness)[1])
# plt.show()