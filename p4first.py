class Problem(object):
    def get_reversed(self, n):
        r = 0
        while n > 0:
            r = r * 10 + n % 10
            n = n / 10
        return r

    def is_palindrome(self, n):
        return n == self.get_reversed(n)

    def run(self):
        top = 999
        lower = 99

        l = 0
        i = top
        while i > lower:
            j = top
            while j > i:
                n = i * j
                if n > l and self.is_palindrome(n):
                    l = n
                j -= 1
            i -= 1
        return l

problem = Problem()

if __name__ == '__main__':
    print problem.run()
