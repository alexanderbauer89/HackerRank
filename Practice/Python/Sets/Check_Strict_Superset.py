if __name__ == '__main__':
    a = set(map(int, input().split()))
    for _ in range(int(input())):
        b = set(map(int, input().split()))
        c = a.issuperset(b)
        if c == False: 
            break
    print(c)
