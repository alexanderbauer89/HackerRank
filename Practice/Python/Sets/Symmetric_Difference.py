def symmetric_difference(a, b):
    x = a.difference(b)
    y = b.difference(a)
    return sorted(x.union(y), key=float)

if __name__ == '__main__':
    _,a = input(), set(raw_input().split())
    _,b = input(), set(raw_input().split())
    print('\n'.join(symmetric_difference(a, b)))
