# GA-for-prediction-problem
# Pro
![image](https://github.com/Thien-mathematics/GA-for-prediction-problem/assets/116644640/86211e08-182f-4cc6-a958-347cf60d71ae)





## Genetic Algorithms

Genetic Algorithms (GAs) are a powerful type of evolutionary algorithm, inspired by the processes of genetic inheritance and natural selection in the natural world.

To understand further, a group of solutions is represented as a set of vectors, and these vectors within the population evolve through various stages.

The evolutionary process comprises three main stages:

-  Selection: Choosing the n most promising vectors from the set of vectors to perform crossover, while retaining some other vectors to explore better solutions and avoid local convergence.
-  Crossover: The process of exchanging information between 2 vectors among the n potential vectors.
-  Mutation: A random process of altering the genetic information of an individual, aimed at exploring broader regions of information.

Genetic Algorithms offer an effective method for optimization and search problems, leveraging principles from nature to find optimal or near-optimal solutions across various domains.

## Implementing the algorithm
- n: size individual
- m: size population
- n_generations: Number of generations
- losses: save loss

## Initialize the required calculation functions
- generate_random_value(bound)
- compute_fitness(individual)
- compute_loss(individual)
- create_individual()
- crossover(individual1, individual2, crossover_rate =number_)
- mutate(individual, mutation_rate = number)
- selection(sorted_old_population)
- create_new_population(old_population, elitism=2, gen=1)

## Train
- Initial Population
- Fitness function
- Selection
- Cross-over
- Mutation
