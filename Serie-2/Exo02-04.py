S1 = "ab"
S2 = "ac"
def shuffle_words(str1, str2):
    Result = []
    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            permutation = str1[:i] + str2[:j] + str1[i:] + str2[j:]
            if permutation not in Result:
                Result.append(permutation)
    print(Result)
shuffle_words(S1,S2)