def symmetric_difference(a, b):
    return sorted(set(a ^ b), key=int)

if __name__ == '__main__':
    _,a = input(), set(input().split())
    _,b = input(), set(input().split())
    print('\n'.join(symmetric_difference(a, b)))
