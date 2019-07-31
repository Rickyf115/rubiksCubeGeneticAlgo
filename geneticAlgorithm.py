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
import copy

rc = RubixCube()

def initialize_pop(population_size, chromosome_size):
    population = []
    for _ in range(population_size):
        population.append(create_chromosome(chromosome_size))
    return population


def create_chromosome(size):
    possible_moves = ['backco','back', 'forwardco','forward', 'topco','top', 'bottomco','bottom', 'leftco','left', 'rightco','right', 'noMove']
    chromosome = []
    for _ in range(size):
        index = random.randint(0, 12)
        chromosome.append(possible_moves[index])
    return chromosome


def fitness(chromosome):
    cube = copy.deepcopy(rc)
    for move in chromosome:
        if move == 'backco':
            cube.backRotate(True)
        elif move == 'back':
            cube.backRotate(False)
        elif move == 'forwardco':
            cube.frontRotate(True)
        elif move == 'forward':
            cube.frontRotate(False)
        elif move == 'topco':
            cube.topRotate(True)
        elif move == 'top':
            cube.topRotate(False)
        elif move == 'bottomco':
            cube.bottomRotate(True)
        elif move == 'bottom':
            cube.bottomRotate(False)
        elif move == 'leftco':
            cube.leftRotate(True)
        elif move == 'left':
            cube.leftRotate(False)
        elif move == 'rightco':
            cube.rightRotate(True)
        elif move == 'right':
            cube.rightRotate(False)
        else:
            pass
    score = cube.getScore(0) + cube.getScore(1) + cube.getScore(2) + cube.getScore(3) + cube.getScore(4) + cube.getScore(5)
    return score

def crossover(chrom1, chrom2):
    index = random.randint(1, 4)
    chrom1slice = chrom1[:index]
    chrom2slice = chrom2[:index]

    #print('Initial Chromosome')
    #print(chrom1)
    #print(chrom2)

    #print('slices')
    #print(chrom1slice)
    #print(chrom2slice)

    chrom1[:index] = chrom2slice
    chrom2[:index] = chrom1slice

    #print('Chromosomes after crossover')
    #print(chrom1)
    #print(chrom2)

    return chrom1, chrom2


def mutation(chrom, mutation_rate):
    possible_moves = ['backco','back', 'forwardco','forward', 'topco','top', 'bottomco','bottom', 'leftco','left', 'rightco','right', 'nomove']
    move_index = random.randint(0, 12)
    for i, move in enumerate(chrom):
        if random.random() <= mutation_rate:
            chrom[i] = possible_moves[move_index]
    print('Mutation occured!')
    return chrom


def selection(population):
    top_chromosome = population[0]
    second_chromosome = population[1]
    for i, chromosome in enumerate(population):
        if fitness(chromosome) > fitness(top_chromosome):
            top_chromosome = chromosome
            top_chromosome_loc = i
            second_chromosome = top_chromosome
            second_chromosome_loc = top_chromosome_loc
        elif fitness(chromosome) > fitness(second_chromosome):
            second_chromosome = chromosome
            second_chromosome_loc = i
    return top_chromosome, second_chromosome,top_chromosome_loc, second_chromosome_loc


def find_lowest(population):
    lowest = population[0]
    lowest_index = 0
    for index, chromosome in enumerate(population, start=0):
        if fitness(chromosome) < fitness(lowest):
            lowest = chromosome
            lowest_index = index
    return lowest, lowest_index


def simulation(generation_size, pop_size, chrom_size, mutation_rate, max_pop):
    population = initialize_pop(population_size=pop_size, chromosome_size=chrom_size)
    count = 0
    while generation_size != 0:
        rand_index = random.randint(0, pop_size - 1)
        top_chromosomes = selection(population)
        chrom1 = list.copy(top_chromosomes[0])
        chrom2 = list.copy(population[find_lowest(population)[1]])
        new_chromosomes = crossover(chrom1, chrom2)
        for index, chromosome in enumerate(new_chromosomes, start=0):
            population.append(chromosome)
        if len(population)>max_pop:
            for _ in range(5):
                del population[find_lowest(population)[1]]
                print('Removing chromosome:', population[find_lowest(population)[1]])
        if random.random() < mutation_rate:
            population[rand_index] = mutation(population[rand_index], mutation_rate)
        top = selection(population)[0]
        print('Top Chromosome: ', top)
        print('fitness Score: ', fitness(top))
        prev_top = list.copy(top)
        if prev_top == top:
            count += 1
        if count > 15:
            del population[top_chromosomes[2]]
            del population[top_chromosomes[3]]
            count = 0
        if fitness(top) == 54:
            generation_size = 1
        generation_size -= 1



if __name__ == '__main__':
    simulation(1000, 50, 5, 0.5, 100)





