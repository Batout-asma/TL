W = "abba"
C = "?"
def shuffle_symbol(word, c):
    results = []
    for i in range(len(word)+1):
        permutation = word[:i] + c + word[i:]
        results.append(permutation)
    print(results)
shuffle_symbol(W,C)