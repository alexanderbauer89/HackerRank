def print_string_validators(string):
    print(any([char.isalnum() for char in string]))
    print(any([char.isalpha() for char in string]))
    print(any([char.isdigit() for char in string]))
    print(any([char.islower() for char in string]))
    print(any([char.isupper() for char in string]))

if __name__ == '__main__':
    s = input()
    print_string_validators(s)
