'''
Genetic Algorithm
Steps Initialize population
Fitness function construction
selection
crossover
mutation
'''

import random
from rubixCube import RubixCube


def initialize_pop(population_size, chromosome_size):
    population = []
    for _ in range(population_size):
        population.append(create_chromosome(chromosome_size))
    return population


def create_chromosome(size):
    possible_moves = ['backco','back', 'forwardco','forward', 'topco','top', 'bottomco','bottom', 'leftco','left', 'rightco','right', 'nothing']
    chromosome = []
    for _ in range(size):
        index = random.randint(0, 12)
        chromosome.append(possible_moves[index])
    return chromosome


def fitness(chromosome):
    rubixCube = RubixCube()
    for move in chromosome:
        if move == 'backco':
            rubixCube.backRotate(True)
        elif move == 'back':
            rubixCube.backRotate(False)
        elif move == 'forwardco':
            rubixCube.frontRotate(True)
        elif move == 'forward':
            rubixCube.frontRotate(False)
        elif move == 'topco':
            rubixCube.topRotate(True)
        elif move == 'top':
            rubixCube.topRotate(False)
        elif move == 'bottomco':
            rubixCube.bottomRotate(True)
        elif move == 'bottom':
            rubixCube.bottomRotate(False)
        elif move == 'leftco':
            rubixCube.leftRotate(True)
        elif move == 'left':
            rubixCube.leftRotate(False)
        elif move == 'rightco':
            rubixCube.rightRotate(True)
        elif move == 'right':
            rubixCube.rightRotate(False)
    totalScore = 0
    for i in range(6):
        totalScore += rubixCube.getScore(i)
    return totalScore


def crossover(chrom1, chrom2):
    index = random.randint(0, 5)
    chrom1slice = chrom1[:index]
    chrom2slice = chrom2[:index]

    # print('Initial Chromosome')
    # print(chrom1)
    # print(chrom2)

    # print('slices')
    # print(chrom1slice)
    # print(chrom2slice)

    chrom1[:index] = chrom2slice
    chrom2[:index] = chrom1slice

    # print('Chromosomes after crossover')
    # print(chrom1)
    # print(chrom2)

    return chrom1, chrom2


def mutation(chrom):
    possible_moves = ['backco','back', 'forwardco','forward', 'topco','top', 'bottomco','bottom', 'leftco','left', 'rightco','right', 'nothing']
    move_index = random.randint(0, 12)
    index = random.randint(0,len(chrom)-1)
    chrom[index] = possible_moves[move_index]
    return chrom


def selection(population):
    top_chromosome = population[0]
    second_chromosome = population[1]
    for chromosome in population:
        if fitness(chromosome) > fitness(top_chromosome):
            top_chromosome = chromosome
            second_chromosome = top_chromosome
        elif fitness(chromosome) > fitness(second_chromosome):
            second_chromosome = chromosome
    return top_chromosome, second_chromosome


def find_lowest(population):
    lowest = population[0]
    lowest_index = 0
    for index, chromosome in enumerate(population, start=0):
        if fitness(chromosome) < fitness(lowest):
            lowest = chromosome
            lowest_index = index
    return lowest, lowest_index


def simulation(generation_size, pop_size, chrom_size):
    population = initialize_pop(population_size=pop_size, chromosome_size=chrom_size)
    while generation_size != 0:
        rand_index = random.randint(0, pop_size - 1)
        top_chromosomes = selection(population)
        chrom1 = top_chromosomes[0]
        chrom2 = top_chromosomes[1]
        new_chromosomes = crossover(chrom1, chrom2)
        for index, chromosome in enumerate(new_chromosomes, start=0):
            population[find_lowest(population)[1]] = new_chromosomes[index]
        population[rand_index] = mutation(population[rand_index])
        print('Top Chromosome: ', chrom1)
        print('fitness Score: ', fitness(chrom1))
        generation_size -= 1



if __name__ == '__main__':
    simulation(500, 25, 4)





