def symmetric_difference(a, b):
    return sorted(set(a ^ b), key=int)

if __name__ == '__main__':
    _,a = input(), set(raw_input().split())
    _,b = input(), set(raw_input().split())
    print('\n'.join(symmetric_difference(a, b)))
