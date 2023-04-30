word="abcd"
def prefixe(W):
    result=[]
    for i in range(len(W)):
        result.append(W[0:i])
    print(result)
prefixe(word)