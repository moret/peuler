class Problem(object):
    def run(self):
        n = 600851475143
        l = 1

        # ruling out even numbers
        if n % 2 == 0:
            l = 2
            n = n / 2
            while n % 2 == 0:
                n = n / 2

        # going over odd numbers only
        i = 3
        while n > 1:
            if n % i == 0:
                l = i
                n = n / i
                while n % i == 0:
                    n = n / i
            i += 2

        return l

problem = Problem()

if __name__ == '__main__':
    print problem.run()
