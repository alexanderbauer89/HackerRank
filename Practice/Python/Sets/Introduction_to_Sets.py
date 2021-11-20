def average(array):
    set_array = set(array)
    return round(sum(set_array) / len(set_array), 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
