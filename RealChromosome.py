'''
Created on 23 mar. 2020

@author: a
'''

from random import randint

from Utils import generateNewValue


class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam
        self.__repres = [generateNewValue(problParam['min'], problParam['max']) for _ in range(problParam['noDim'])]
        self.__fitness = 0.0

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, c):
        r = randint(1, len(self.__repres) - 2)
        newrepres = []
        for i in range(r-1):
            newrepres.append(self.__repres[i])
        for i in range (r-1,r+2):
            newrepres.append(c.__repres[i])
        for i in range(r+2, len(self.__repres)):
            newrepres.append(self.__repres[i])

        offspring = Chromosome(c.__problParam)
        offspring.repres = newrepres
        return offspring

    def mutation(self):
        pos = randint(0, len(self.__repres) - 1)
        self.__repres[pos] = generateNewValue(self.__problParam['min'], self.__problParam['max'])

    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness