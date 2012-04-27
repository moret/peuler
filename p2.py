class Problem(object):
    def run(self):
        s = 0
        a = 1
        b = 1
        c = a + b
        while c < 4000000:
            s += c
            a = b + c
            b = c + a
            c = a + b
        return s

problem = Problem()

if __name__ == '__main__':
    print problem.run()
