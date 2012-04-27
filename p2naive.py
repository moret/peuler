def main():
    s = 0
    n = 1
    m = 2
    while m < 4000000:
        if m % 2 == 0:
            s += m
        o = n + m
        n = m
        m = o
    return s

if __name__ == '__main__':
    print main()
