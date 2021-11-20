def runner_up_score(arr):
    score_list = list(set(arr))
    score_list.sort(reverse=True)
    return score_list[1]

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(runner_up_score(arr))
