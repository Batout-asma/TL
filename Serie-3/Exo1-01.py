W1 = "cdbaabbcdb"
W2 = "acdbab"
def simulate_fsa(word):
     state = 0
     for current_char in word:
          if state == 0:
               if current_char in ['a']:
                    state = 1
               elif current_char in ['b','c','d']:
                    state = 0
               elif current_char in ['b']:
                    state = 2
               elif current_char in ['a','c','d']:
                    state = 0
print (simulate_fsa(W1))
print (simulate_fsa(W2))