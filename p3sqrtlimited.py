class Problem(object):
    def sqrt(self, n):
        return n ** 1 / 2

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
        # limiting factors to sqrt of n
        i = 3
        m = self.sqrt(n)
        while n > 1 and l <= m:
            if n % i == 0:
                l = i
                n = n / i
                m = self.sqrt(n)
                while n % i == 0:
                    n = n / i
            i += 2

        if l == 1:
            return n
        else:
            return l

problem = Problem()

if __name__ == '__main__':
    print problem.run()
