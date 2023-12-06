import copy
import os
import time
from random import randint

import configs as cnf

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from scoop import futures

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

def init_individual(icls, content):
    return icls(content)

def init_population(pcls, ind_init, list_of_decks):
    return pcls(ind_init(c) for c in list_of_decks)

def generate_individual(card_pool):
    individual = []
    card_pool_size = len(card_pool)
    while len(individual) < 40:
        genome = randint(0, card_pool_size - 1)
        number_of_genome_present = individual.count(genome) #count number of copy of a card
        if number_of_genome_present < card_pool[genome][1]: #check legality of card copies
            individual.append(genome)
    return individual

def generate_first_generation_decks(card_pool):
    population = [] #set of individuals (decks)
    for i in range(cnf.POPSIZE):
        population.append(generate_individual(card_pool))
    return population

def mutation(individual):
    size = len(individual)
    mutation_site = randint(0, size - 1)
    mutated = False
    while not mutated:
        new_gene = randint(0, cnf.CARD_POOL_SIZE - 1)
        gene_limit = cnf.CARD_POOL[new_gene][1]
        if individual.count(new_gene) < gene_limit:
            individual[mutation_site] = new_gene
            mutated = True
    return individual,  # MUST RETURN TUPLE


def mating(individual1, individual2):
    size = len(individual1)
    cxpoint1 = randint(1, size - 1)
    cxpoint2 = randint(1, size - 1)
    if cxpoint1 >= cxpoint2:
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1 + 1
    else:
        cxpoint2 += 1
    individual1[cxpoint1:cxpoint2], individual2[cxpoint1:cxpoint2] \
        = individual2[cxpoint1:cxpoint2], individual1[cxpoint1:cxpoint2]
    return individual1, individual2

def main():
    #Register toolbox
    toolbox = base.Toolbox()
    toolbox.register("individual", generate_individual, cnf.CARD_POOL)
    toolbox.register("population", generate_first_generation_decks, cnf.CARD_POOL)
    toolbox.register("mate", mating)
    toolbox.register("mutate", mutation)

    number_of_matches = int(cnf.MATCHES_PER_OPPONENT) * len(cnf.OPPONENTS) * cnf.NUMBER_OF_GENERATIONS * cnf.POPSIZE
    first_gen_decks = generate_first_generation_decks(cnf.CARD_POOL)





if __name__ == '__main__':
    main()