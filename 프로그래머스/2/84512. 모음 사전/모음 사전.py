from itertools import product

def solution(word):
    answer = 0
    dic=[]
    vowel=['A','E','I','O','U']
    for i in range(5):
        for v in product(vowel, repeat=i+1):
            dic.append(''.join(v))
        
    dic.sort()
    return dic.index(word)+1