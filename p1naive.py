class Problem(object):
    def run(self):
        s = 0
        for i in range(1, 1000):
            if i % 3 == 0 or i % 5 == 0:
                s += i
        return s

problem = Problem()

if __name__ == '__main__':
    print problem.run()
