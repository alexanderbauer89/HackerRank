if __name__ == '__main__':
    n, base_set    =   input(), set(map(int, input().split()))
    for _ in range(int(input())):
        operation  =   input().split()
        getattr(base_set, operation[0])(set(map(int, input().split())))
    print(sum(base_set))
