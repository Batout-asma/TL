W1 = "cdbaabbcdb"
W2 = "acdbab"


def simulate_fsa(word):
    state = 0
    for current_char in word:

        if state == 0:
            if current_char in ['a']:
                state = 1
            elif current_char in ['b', 'c', 'd']:
                state = 0

        if state == 1:
            if current_char in ['b']:
                state = 2
            elif current_char in ['c', 'd']:
                state = 0
            elif current_char in ['a']:
                state = 1

        if state == 2:
            if current_char in ['c']:
                state = 3
            elif current_char in ['a', 'b', 'd']:
                state = 2

        if state == 3:
            if current_char in ['d']:
                state = 4
            elif current_char in ['c']:
                state = 3
            elif current_char in ['a', 'b']:
                state = 2

        if state == 4:
            if current_char in ['a', 'b', 'c', 'd']:
                state = 4
    return state == 4


print(simulate_fsa(W1))
print(simulate_fsa(W2))
