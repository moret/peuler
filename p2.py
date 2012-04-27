def main():
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

if __name__ == '__main__':
    print main()
