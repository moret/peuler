class Problem(object):
    def sum_divisible_by(self, n):
        p = 1000 / n
        return n * (p * (p + 1)) / 2

    def run(self):
        return self.sum_divisible_by(3) + self.sum_divisible_by(5) - self.sum_divisible_by(15)

problem = Problem()

if __name__ == '__main__':
    print problem.run()
