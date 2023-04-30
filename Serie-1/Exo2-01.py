C1 = "A"
C2 = "D"
def crage(c1, c2):
    Result = ""
    for i in range(ord(c1), ord(c2)+1):
        Result += chr(i)
    print(Result)
crage(C1,C2)
