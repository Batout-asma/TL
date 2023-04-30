L1=[1,5]
L2=[2,1]
Result=[]
def repeat_by_list(Liste1,Liste2):
    for i in range(len(Liste1)):
        for j in range(Liste2[i]):
            Result.append(Liste1[i])
repeat_by_list(L1,L2)
print(Result)