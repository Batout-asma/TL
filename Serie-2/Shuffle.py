S1 = "ab"
S2 = "ac"
def shuffle_symbol(word, c):
    results = []
    for i in range(len(word)+1):
        permutation = word[:i] + c + word[i:]
        results.append(permutation)
    print(results)

def shuffle_words(str1, str2):
    Result = []
    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            C = str2[:j]
            permutation = shuffle_symbol(S1,C) + [str2[j:]]
            if permutation not in Result:
                Result.append(permutation)
    print(Result)
shuffle_words(S1,S2)