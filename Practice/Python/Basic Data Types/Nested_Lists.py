if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        students.append([input(), float(input())])
    students.sort(key = lambda x: x[1])
    low_count = sum(x.count(students[0][1]) for x in students)
    out = sorted(x[0] for x in students if x[1] == students[low_count][1])
    print('\n'.join(out))
