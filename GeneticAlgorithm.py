import random
import math


class GA:
    def __init__(self):
        self.generation = []
        self.nums = 20  # 染色体个数
        self.length = 8  # 染色体长度
        self.probability = 0.05     # 变异率
        self.initialization()

    def info(self):
        for each in self.generation:
            print(str(each) + ' fitness: ' + str(self.fitness(each)))

    def fitness(self, chromosome):
        value = 0
        for i in range(self.length):
            value += chromosome[i] * (2 ** (self.length - i - 1))
        # 目标函数
        max = 2 ** len(chromosome) - 1
        min = 0
        x = (((value - min) * (2 - (-1))) / (max - min)) + (-1)
        return x * math.sin(10 * math.pi * x) + 2

    def initialization(self):
        # 采用二进制编码
        for _ in range(self.nums):
            chromosome = []
            for _ in range(self.length):
                chromosome.append(random.randint(0, 1))
            self.generation.append(chromosome)
        self.generation.sort(key=lambda f: self.fitness(f), reverse=True)

    def selection(self):
        # random selection
        while True:
            parent_0_pos = random.randint(0, self.length - 1)
            parent_1_pos = random.randint(0, self.length - 1)
            if parent_0_pos != parent_1_pos:
                break
        return [self.generation[parent_0_pos], self.generation[parent_1_pos]]

    def crossover(self):
        # single-point crossover
        parents = self.selection()
        crossover_point = random.randint(1, self.length - 2)
        offspring_0 = []
        offspring_1 = []
        offspring_0 += parents[0][0:crossover_point]
        offspring_0 += parents[1][crossover_point:]
        offspring_1 += parents[1][0:crossover_point]
        offspring_1 += parents[0][crossover_point:]
        return [offspring_0, offspring_1]

    def mutation(self):
        offsprings = self.crossover()
        for i in range(self.length):
            offsprings[0][i] = abs(offsprings[0][i] - 1) if random.random() < self.probability else offsprings[0][i]
            offsprings[1][i] = abs(offsprings[1][i] - 1) if random.random() < self.probability else offsprings[1][i]
        return offsprings

    def next_generation(self):
        offsprings = self.mutation()
        self.generation.append(offsprings[0])
        self.generation.append(offsprings[1])
        self.generation.sort(key=lambda f: self.fitness(f), reverse=True)
        self.generation = self.generation[0:self.nums]

    def run(self):
        for i in range(1000):
            self.next_generation()
            print('第{}代，最佳fitness: {}'.format(i, self.fitness(self.generation[0])))


if __name__ == '__main__':
    ga = GA()
    ga.run()
