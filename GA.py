import random
import math
import pygame
import main
import QLearning as Q
import constant as C
import main

def random_chromosome():
    return [random.randint(1,(len(C.actions)))-1 for i in range(C.statespace)]

def updateAction(player, chromosome):
    return C.actions[chromosome[C.state.index(player.state)]]

def average_fitness(fitness_scores):
    total_fitness = 0
    for each in range(C.PopulationSize):
        total_fitness += fitness_scores[each]
    return total_fitness/C.PopulationSize

def selection_chance(fitness_scores, chromosome, remaining):
    this_fitness = fitness_scores[chromosome]
    fit_sum = 0
    for each in range(remaining):
        fit_sum += fitness_scores[each]
    if fit_sum == 0: return 0
    else: return this_fitness/fit_sum

def select(fitness_scores, remaining, blacklist):
    r = random.random()
    lower = upper = 0
    #TODO: surround this in an infinite loop so that it cant ever not find a parent to select
    for chromosome in range(remaining):
        lower = upper
        upper += selection_chance(fitness_scores, chromosome, remaining)
        if r > lower and r < upper and chromosome != blacklist: return chromosome
    return -1

def select_pair(population, fitness_scores, remaining):
    p1 = select(fitness_scores, remaining, -1)
    if p1 == -1: p1 = 0
    p2 = p1
    while p2 == p1: p2 = select(fitness_scores, remaining-1, p1)
    if p2 == -1:
        if p1 == 0: p2 = 1
        else: p2 = 0
    if C.Replacement: return [population[max(p1, p2)], population[min(p1, p2)]]
    else: return [population.pop(max(p1, p2)), population.pop(min(p1, p2))], population

def breed(population, fitness_scores):
    newPopulation = []
    newFitnessScores = []
    remaining = C.PopulationSize
    while remaining > 0:
        if C.Replacement: p = select_pair(population, fitness_scores, C.PopulationSize)
        else: p, population = select_pair(population, fitness_scores, remaining)
        p1 = p[0]
        p2 = p[1]
        r = random.randrange(1, C.statespace)
        c1 = p1[:r]+p2[r:]
        c2 = p2[:r]+p1[r:]
        if random.random() < C.MutationPct:
            g1 = random.randrange(C.statespace)
            g2 = random.randrange(C.statespace)
            c1[g1], c1[g2] = c1[g2], c1[g1]
        if random.random() < C.MutationPct:
            g1 = random.randrange(C.statespace)
            g2 = random.randrange(C.statespace)
            c2[g1], c2[g2] = c2[g2], c2[g1]
        if C.Elitism:
            p1score = fitness_scores[population.index(p[0])]
            p2score = fitness_scores[population.index(p[1])]
            c1score = main.simulate(main.newGameContainer(), c1)
            c2score = main.simulate(main.newGameContainer(), c2)
            contenderscores = [p1score, p2score, c1score, c2score]
            contenders = [p1, p2, c1, c2]
            m1 = contenderscores.index(max(contenderscores))
            newFitnessScores.append(contenderscores[m1])
            newPopulation.append(contenders.pop(m1))
            del contenderscores[m1]
            m2 = contenderscores.index(max(contenderscores))
            newFitnessScores.append(contenderscores[m2])
            newPopulation.append(contenders.pop(m2))
        else:
            newPopulation.append(c1)
            newPopulation.append(c2)
        remaining -= 2
        print("remaining: ",remaining)
    return newPopulation, newFitnessScores

def best_solution(fitness_scores):
    return fitness_scores.index(max(fitness_scores))
