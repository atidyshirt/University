
# write a function select(population, error, max_error, r) that takes a list of
# individuals, an error function, max error value possible and a floating random
# number r within [0, 1] and returns an individual from the population using the rulette
# wheel selection mechanism

def select(population, error, max_error, r):
    # calculate the total error
    total_error = 0
    for individual in population:
        total_error += error(individual)
    # calculate the cumulative error
    cumulative_error = 0
    for individual in population:
        cumulative_error += error(individual)
        if cumulative_error / total_error >= r:
            return individual
    for individual in population:
        cumulative_error += error(individual) / total_error
        if cumulative_error > r:
            return individual



population = ['a', 'b']

def error(x):
    return {'a': 14, 'b': 12}[x]

max_error = 15

for r in [0, 0.1, 0.24, 0.26, 0.5, 0.9]:
    print(select(population, error, max_error, r))

# since the fitness of 'a' is 1 and the fitness of 'b' is 3,
# for r's below 0.25 we get 'a', for r's above it we get 'b'.
