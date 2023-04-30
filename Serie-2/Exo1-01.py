T1 = (("a",2),("b",5),("c",1))
def flatten_word(Tuple):
    Result = ""
    for Char, Times in Tuple:
        Result += Char * Times
    print(Result)
flatten_word(T1)