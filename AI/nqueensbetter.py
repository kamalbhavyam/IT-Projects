import random
import functools
import time
import numpy

def initpopulation():
    popsize = 100
    initpop = set({})
    for _ in range(popsize):
        inity = numpy.random.permutation(8)
        initpop.add(numpy.array2string(inity,separator='')[1:9])    
    return initpop

def fitness(instance):
    nonconflictpairs=0
    for ind,gene in enumerate(instance):
        for oind,ogene in enumerate(instance):
            if oind>ind:
                if gene!=ogene:
                    if (ogene>gene and int(ogene)-(oind-ind)!=int(gene)) or (ogene<gene and int(ogene)+(oind-ind)!=int(gene)):
                        nonconflictpairs+=1
    return nonconflictpairs

def reproduce(x,y):
    c = random.randint(0,7)
    return x[:c+1] + y[1+c:]

def mutate(x):
    ind1 = random.randint(0,7)
    # ind2 = random.randint(0,7)
    # while ind2==ind1:
    #     ind2 = random.randint(0,7)
    place1 = random.randint(0,7)
    # place2 = random.randint(0,7)
    x = x[:ind1] + str(place1) + x[ind1+1:]
    # x = x[:ind2] + str(place2) + x[ind2+1:]
    return x

def compare(chrom1,chrom2):
    return (fitness(chrom2)-fitness(chrom1))

def survive(n,population,fitness):
    poplist = list(population)
    poplist.sort(key=functools.cmp_to_key(compare))
    newpoplist=poplist[0:int(0.85*n)+1]
    for _ in range(int(0.15*n)):
        newpoplist.append(random.choice(poplist[int(0.85*n)+1:]))
    return set(newpoplist)

def pickrand(population,fitness):
    poplist=list(population)
    sumtot=0
    maxfit=fitness(poplist[0])
    for elem in poplist:
        ftemp=fitness(elem)
        sumtot+=ftemp
        maxfit=max(maxfit,ftemp)
    weights=[]
    for elem in poplist:
        weights.append(fitness(elem)/maxfit)
    
    return random.choices(poplist,weights)[0]

def genalgobetter(population,fitness):
    generation=0
    doneflag=False
    while(True) and not doneflag:
        generation+=1
        # print(generation)
        newpop = set({})

        n = len(population)
        # for _ in range(n):
        while len(newpop)<100:
            x = pickrand(population,fitness)
            y = pickrand(population,fitness)
            while y==x:
                y = pickrand(population,fitness)
            
            # print("Reproducing ",xinstance, "and ",yinstance)
            # child=reproduce(xinstance,yinstance)
            child=reproduce(x,y)
            if fitness(child)==28:
                print("found",child)
                print(generation)
                doneflag=True
                break

            m = random.random()
            if m<=0.1:
                # print("Mutating ",child)
                child=mutate(child)
            if fitness(child)==28:
                print("bruh",child)
                print(generation)
                doneflag=True
                break
            # print("child fitness: ",fitness(child), child)
            # print("max ",max([fitness(elem) for elem in population]))
            newpop.add(child)
        population.update(newpop)
        population=survive(100,population,fitness)
        # print("max ",max([fitness(elem) for elem in population]))
        # print(numpy.mean([fitness(elem) for elem in population]))

for _ in range(25):
    startpop=initpopulation()
    genalgobetter(startpop,fitness)