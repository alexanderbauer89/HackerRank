from itertools import groupby
for i, n in groupby(input()):
    print((len(list(n)),int(i)),end=" ")
