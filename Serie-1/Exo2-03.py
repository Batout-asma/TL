S = "abc=ded"
Sub1 = "="
Sub2 = "f"
Sub3 = "=e"
Sub4 = "=f"
def conditional_replace(string, sub1, sub2, sub3, sub4):
    result = ''
    for i in range(len(string)):
        if string[i:i+len(sub1)] == sub1:
            if i+len(sub1)+len(sub2) <= len(string) and string[i+len(sub1):i+len(sub1)+len(sub2)] == sub2:
                result += sub3
                i += len(sub1) + len(sub2) - 1
                continue
            else:
                result += sub4
                i += len(sub1) - 1
                continue
        result += string[i]
    print(result)
conditional_replace(S, Sub1,Sub2, Sub3,Sub4)