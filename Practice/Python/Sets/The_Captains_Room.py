def captains_room(rooms, group):
    return ((sum(set(rooms)) * group) - (sum(rooms))) // (group - 1)

if __name__ == '__main__':
    group_size  =   int(input())                     
    rooms_list  =   list(map(int, input().split()))
    print(captains_room(rooms_list, group_size))
