import sys
import numpy
import random

values = [
    [ 0, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 0.15, sys.maxsize, sys.maxsize, 0.2, sys.maxsize, 0.12, sys.maxsize, sys.maxsize ],
    [ sys.maxsize, 0, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 0.19, 0.4, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 0.13 ],
    [ sys.maxsize, sys.maxsize, 0, 0.6, 0.22, 0.4, sys.maxsize, sys.maxsize, 0.2, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize,],
    [ sys.maxsize, sys.maxsize, 0.6, 0, sys.maxsize, 0.21, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 0.3, sys.maxsize, sys.maxsize, sys.maxsize ],
    [ sys.maxsize, sys.maxsize, 0.22, sys.maxsize, 0, sys.maxsize, sys.maxsize, sys.maxsize, 0.18, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize ],
    [ sys.maxsize, sys.maxsize, 0.4, 0.21, sys.maxsize, 0, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 0.37, 0.6, 0.26, 0.9],
    [ 0.15, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 0, sys.maxsize, sys.maxsize, sys.maxsize, 0.55, 0.18, sys.maxsize, sys.maxsize ],
    [ sys.maxsize, 0.19, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 0, sys.maxsize, 0.56, sys.maxsize, sys.maxsize, sys.maxsize, 0.17],
    [ sys.maxsize, 0.4, 0.2, sys.maxsize, 0.18, sys.maxsize, sys.maxsize, sys.maxsize, 0, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 0.6 ],
    [ 0.2, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 0.56, sys.maxsize, 0, sys.maxsize, 0.16, sys.maxsize, 0.5 ],
    [ sys.maxsize, sys.maxsize, sys.maxsize, 0.3, sys.maxsize, 0.37, 0.55, sys.maxsize, sys.maxsize, sys.maxsize, 0, sys.maxsize, 0.24, sys.maxsize ],
    [ 0.12,  sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 0.6, 0.18, sys.maxsize, sys.maxsize, 0.16, sys.maxsize, 0, 0.4, sys.maxsize ],
    [ sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 0.26, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 0.24, 0.4, 0, sys.maxsize ],
    [ sys.maxsize, 0.13, sys.maxsize, sys.maxsize, sys.maxsize, 0.9, sys.maxsize, 0.17, 0.6, 0.5, sys.maxsize, sys.maxsize, sys.maxsize, 0 ]
]

def initpopulation(citylist):
    population = set({})
    popsize = 1
    while len(population)<popsize:
        route=""
        # startind=random.randint(0,len(citylist)-1)
        # curind=startind
        # route+=citylist[startind]
        route+=random.choice(citylist)
        while len(route)<len(citylist):
            possiblelist=[elem for elem in citylist if elem not in route and values[int(route[-1],16)][int(elem,16)]!=sys.maxsize and values[int(route[-1],16)][int(elem,16)]!=0]
            print("route: ",route, " possiblelist ",possiblelist)
            if len(possiblelist)==0:
                break
            route+=random.choice(possiblelist)

    return population

def routelength(route):
    routelen=0
    for ind in range(1,len(route)):
        routelen+=values[int(route[ind-1],16)][int(route[ind],16)]
    return round(routelen,2)

def fitness(route):
    return 1/round(routelength(route),2)

def reproduce(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []
    geneA = int(random.random()*len(parent1))
    geneB = int(random.random()*len(parent1))
    # print("genes ", geneA, geneB)
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)
    for i in range(startGene, endGene):
        childP1.append(parent1[i])
    childP2 = [item for item in parent2 if item not in childP1]
    # print("child ",childP1, childP2)
    # child = childP1 + childP2
    # return ''.join([str(item) for item in child])
    child = childP2[:startGene]+childP1+childP2[startGene:]
    return ''.join([str(item) for item in child])

def mutate(child):
    ind1 = int(random.random()*len(child))
    ind2 = int(random.random()*len(child))
    while ind2==ind1:
        ind2 = int(random.random()*len(child))
    temp = child[ind1]
    child = child[:ind1] + child[ind2] + child[ind1+1:]
    child = child[:ind2] + temp + child[ind2+1:]
    return child

def pickrand(population, fitness):
    poplist=list(population)
    maxfit=fitness(poplist[0])
    for elem in poplist:
        ftemp=fitness(elem)
        maxfit=max(maxfit,ftemp)
    weights=[]
    for elem in poplist:
        weights.append(fitness(elem)/maxfit)    
    return random.choices(poplist,weights,k=2)

def genalgo(population,fitness):
    generation=0
    doneflag=False
    while(True) and not doneflag:
        generation+=1
        print(generation)
        newpop = set({})

        n = len(population)
        # for _ in range(n):
        while len(newpop)<100:
            x,y = pickrand(population,fitness)
            # y = pickrand(population,fitness)
            while y==x:
                x,y = pickrand(population,fitness)
            # print("Reproducing ",x, "and ",y)
            # child=reproduce(xinstance,yinstance)
            child=reproduce(x,y)
            # if fitness(child)==28:
            #     print("found",child)
            #     doneflag=True
            #     break

            m = random.random()
            if m<=0.03:
                # print("Mutating ",child)
                child=mutate(child)
            # if fitness(child)==28:
            #     print("bruh",child)
            #     doneflag=True
            #     break
            # print("child fitness: ",fitness(child), child)
            # print("max ",max([fitness(elem) for elem in population]))
            newpop.add(child)
        population = newpop
        # print("max ",max([fitness(elem) for elem in population]))
        # print(numpy.mean([fitness(elem) for elem in population]))
        print(numpy.min([routelength(elem) for elem in population]))

startpop = initpopulation(['0','1','2','3','4','5','6','7','8','9','A','B','C','D'])
print(startpop)
# genalgo(startpop,fitness)
# for ind in range(len(startpop)):
#     print(fitness(list(startpop)[ind]))