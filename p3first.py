class Problem(object):
    def run(self):
        n = 600851475143

        i = 2
        l = None
        while i <= n:
            if n % i == 0:
                n = n / i
                if not l or i > l:
                    l = i
                i = 2
            else:
                i += 1

        return l

problem = Problem()

if __name__ == '__main__':
    print problem.run()
