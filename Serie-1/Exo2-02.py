s="aabc"
L1 = ["a","b","c"]
L2 = ["b","a","d"]
def replace_many(s,Liste1,liste2):
    Result = []
    for i in range(len(s)):
        Result += liste2[Liste1.index(s[i])]
    print(Result)
replace_many(s,L1,L2)
