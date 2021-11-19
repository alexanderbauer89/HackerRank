def minion_game(string):
    # define vowels and scores
    vowels          =   'AEIOU'
    score_stuart    =   0
    score_kevin     =   0

    # calculate scores
    for i in range(len(string)):
        if string[i] in vowels:
            score_kevin += (len(string) - i)
        else:
            score_stuart += (len(string) - i)

    # calculate result
    if score_kevin > score_stuart:
        print("Kevin", score_kevin)
    elif score_kevin < score_stuart:
        print("Stuart", score_stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
