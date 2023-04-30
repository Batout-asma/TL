L1=[1,2,3,4]
L2=[4,5,6,7]
Result=[]
def substract(Liste1,Liste2):
    for i in Liste1:
        if i not in Liste2:
            Result.append(i)
substract(L1,L2)
print(Result)