import random
import time
import numpy

def initpopulation():
    popsize = 20
    initpop = []

    # for _ in range(popsize):
    #     inity = [random.randint(0,7)]*8
    #     initpop.append(''.join([str(elem) for elem in inity]))
    inity = [random.randint(0,7)]*8
    inity = ''.join([str(elem) for elem in inity])
    initpop = [inity]*popsize
    
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
    # nonattackingqueens=0
    # for ind,gene in enumerate(instance):
    #     conflictflag=False
    #     for oind,ogene in enumerate(instance):
    #         if oind!=ind:
    #             if gene==ogene or (ogene>gene and int(ogene)-abs(oind-ind)==int(gene)) or (ogene<gene and int(ogene)+abs(oind-ind)==int(gene)):
    #                 conflictflag=True
    #                 break
    #     if not conflictflag:
    #         nonattackingqueens+=1
    # return nonattackingqueens+1

def reproduce(x,y):
    c = random.randint(0,7)
    return x[:c+1] + y[1+c:]

def mutate(x):
    ind = random.randint(0,7)
    place = random.randint(0,7)
    x = x[:ind] + str(place) + x[ind+1:]
    return x

def pickrand(population,fitness):
    poplist=list(population)
    # sumtot=0
    maxfit=max([fitness(elem) for elem in poplist])
    # for elem in poplist:
    #     ftemp=fitness(elem)
    #     sumtot+=ftemp
    #     maxfit=max(maxfit,ftemp)
    weights=[]
    for elem in poplist:
        weights.append(fitness(elem)/maxfit)
    
    return random.choices(poplist,weights)[0]

def genalgo(population,fitness):
    generation=0
    doneflag=False
    while(True) and not doneflag:
        generation+=1
        # print(generation)
        # print(population)
        # newpop = set({})
        newpop = []

        n = len(population)
        for _ in range(n):
        # while len(newpop)<100:
            x = pickrand(population,fitness)
            y = pickrand(population,fitness)
            # while y==x:
            #     y = pickrand(population,fitness)
            
            # print("Reproducing ",xinstance, "and ",yinstance)
            # child=reproduce(xinstance,yinstance)
            child=reproduce(x,y)
            if fitness(child)==29:
                print("found",child)
                print(generation)
                doneflag=True
                break

            m = random.random()
            if m<=0.1:
                # print("Mutating ",child)
                child=mutate(child)
            if fitness(child)==29:
                print("bruh",child)
                print(generation)
                doneflag=True
                break
            # print("child fitness: ",fitness(child), child)
            # print("max ",max([fitness(elem) for elem in population]))
            newpop.append(child)
        population = newpop
        # if generation%100==0:
        #     print(generation)
        #     print("max ",max([fitness(elem) for elem in population]))
        #     print(numpy.mean([fitness(elem) for elem in population]))

for _ in range(25):
    startpop=initpopulation()
    genalgo(startpop,fitness)