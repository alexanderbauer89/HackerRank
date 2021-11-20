def score(arr, a, b):
    score = 0
    for number in arr:
        if number in a: score += 1
        if number in b: score -= 1
    return score

if __name__ == '__main__':
    n, m    =   input().split()
    arr     =   input().split()
    a       =   set(input().split())
    b       =   set(input().split())
    print(score(arr, a, b))
