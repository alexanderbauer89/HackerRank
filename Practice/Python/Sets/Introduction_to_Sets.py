from __future__ import division

def average(array):
    set_array = set(array)
    return round(sum(set_array) / len(set_array), 3)

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
