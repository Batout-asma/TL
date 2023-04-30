L1 = [1,3,5,7,8,6,4,2]
L2 = []
def symmetric_brows(Liste):
    x = len(Liste)-1
    if (len(Liste) % 2 == 0):
        y = int(len(Liste)/2)
    else:
        y = (len(Liste)/2 +1)
    for i in range(y):
        L2.append(Liste[i])
        if x == i:
            break
        L2.append(Liste[x])
        x-= 1
symmetric_brows(L1)
print(L2)