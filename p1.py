def sum_divisible_by(n):
    p = 1000 / n
    return n * (p * (p + 1)) / 2


def main():
    return sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)

if __name__ == '__main__':
    print main()
