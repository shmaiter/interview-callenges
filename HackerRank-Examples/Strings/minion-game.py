def minion_game(string):
    k_score = 0
    s_score = 0
    for i in range(len(s)):
        if s[i] in "AEIOU":
            k_score += (len(s)-i)
        else:
            s_score += (len(s)-i)

    if k_score > s_score:
        print("Kevin", k_score)
    elif k_score < s_score:
        print("Stuart", s_score)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
