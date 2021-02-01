import random


class GA:
    def __init__(self):
        self.generation = []
        self.nums = 20
        self.length = 8

    def info(self):
        for each in self.generation:
            print(str(each) + ' fitness: ' + str(self.fitness(each)))

    def fitness(self, chromosome):
        value = 0
        for i in range(self.length):
            value += chromosome[i] * (2 ** (self.length - i - 1))
        # 目标函数
        fitness = - value ** 2 + 2 * value
        return fitness

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
            parent_1_pos = random.randint(0, self.length - 1)
            parent_2_pos = random.randint(0, self.length - 1)
            if parent_1_pos != parent_2_pos:
                break
        return [self.generation[parent_1_pos], self.generation[parent_2_pos]]

    def crossover(self, parents):

        # single-point crossover

        return

    def mutation(self):
        return


if __name__ == '__main__':
    ga = GA()
    ga.initialization()
    ga.info()
