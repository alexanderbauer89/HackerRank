def perform_command(arr, command):
    attr, *args = command.split() # split attr and args
    args = list(map(int, args)) # make list of ints
    print(arr) if attr == 'print' else getattr(arr, attr)(*args)

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        perform_command(arr, input())
