Word = "asma"
def unflatten_word(word):
    Result = []
    Char_Times = 0
    for i in range(len(word)):
        if i == 0 or word[i] != word[i-1]:
            if i > 0:
                Result.append((word[i-1], Char_Times))
            Char_Times = 1
        else:
            Char_Times += 1
    Result.append((word[-1], Char_Times))
    print(Result)
unflatten_word(Word)
