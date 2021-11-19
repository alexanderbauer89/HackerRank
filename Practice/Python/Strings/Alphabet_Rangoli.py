import string

def print_rangoli(size):
    alpha  = string.ascii_lowercase
    mylist = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        mylist.append((s[::-1] + s[1:]).center(4  * n - 3, "-"))
    print('\n'.join(mylist[:0:-1] + mylist))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
