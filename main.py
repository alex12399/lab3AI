'''
Created on 23 mar. 2020

@author: a
'''

import warnings 

from GA import GA 
from RealChromosome import Chromosome
from modularity import modularity
import matplotlib.pyplot as plt 
import networkx as nx
from nrComunitati import nrComunitati
import numpy as np 
from read import readGML


def main():
    warnings.simplefilter('ignore')
    
    net=readGML("data/football.gml")
    
    A=np.matrix(net["mat"])
    G=nx.from_numpy_matrix(A)
    pos = nx.spring_layout(G)  # compute graph layout
    plt.figure(figsize=(4, 4))  # image is 8 x 8 inches 
    nx.draw_networkx_nodes(G, pos, node_size = 600, cmap = plt.cm.get_cmap('RdYlBu'))
    nx.draw_networkx_edges(G, pos, alpha = 0.3)
    
    MIN=1
    if net['noNodes']<=11:
        MAX=net["noNodes"]
    else:
        MAX=11
    noDim=net["noNodes"]
    
    gaParam = {'popSize' : 100, 'noGen' : 50, 'pc' : 0.8, 'pm' : 0.1, 'net': net}

    problParam = {'min' : MIN, 'max' : MAX, 'function' : modularity, 'noDim' : noDim, 'noBits' : 8}
    
    allBestFitnesses = []
    generations = []
    
    
    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()
    maximFitness=-1
    bestRepres=[]
    fileName_output="football_out.txt"
    f=open(fileName_output,'w')
    for g in range(gaParam['noGen']):
        bestSolX = ga.bestChromosome().repres
        bestSolY = ga.bestChromosome().fitness
        if bestSolY>maximFitness:
            maximFitness=bestSolY
            bestRepres=bestSolX
        allBestFitnesses.append(bestSolY)
        generations.append(g)
    
#         ga.oneGeneration()
        ga.oneGenerationElitism()
#         ga.oneGenerationSteadyState()
        
        bestChromo = ga.bestChromosome()
        f.write('Best solution in generation ' + str(g) + ' is: x = ' + str(bestChromo.repres) + ' f(x) = ' + str(bestChromo.fitness))
        f.write('\n')
    f.write("Best repres&fitness: "+str(bestRepres)+" "+str(maximFitness))
    f.write('\n')
    f.write("Nr. de comunitati: "+str(nrComunitati(bestRepres)))
        
    f.close()
    
    A2=np.matrix(net["mat"])
    G2=nx.from_numpy_matrix(A2)
    pos2 = nx.spring_layout(G2)  # compute graph layout
    plt.figure(figsize=(4, 4))  # image is 8 x 8 inches 
    nx.draw_networkx_nodes(G2, pos2, node_size = 600, cmap = plt.cm.get_cmap('RdYlBu'), node_color = bestRepres)
    nx.draw_networkx_edges(G2, pos2, alpha = 0.3)
    plt.show(G)
    plt.show(G2)

if __name__ == '__main__':
    main()