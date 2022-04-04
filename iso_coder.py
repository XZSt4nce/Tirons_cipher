from time import time
from sys import setrecursionlimit
import random
setrecursionlimit(100000)
def Q(n, results):
    if n == 1 or n == 2: return 1
    elif n in results: return results[n]
    else:
        res = Q(n - Q(n - 1, results), results) + Q(n - Q(n - 2, results), results)
        results[n] = res
        return res
random.seed(time())
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c',
            'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5',
            '6', '7', '8', '9', '!', '@', '#', '$', '%' , '^', '&', '*', '(', ')', '',
            '\"', '№', ';', ':', '/', '\\', "\'", ',', '.', '?', '-', '_', '+', '=', '[', ']', '{', '}', '|', '`', '~']

def make_ni_word(): #make not isogram word
    length = random.randint(2, 15)
    word = ''
    
    for i in range(length):
        word += random.choice(alphabet)
        
    index1 = random.randint(0, len(word)-1)
    index2 = random.randint(0, len(word)-1)
    
    while index2 == index1:
        index2 = random.randint(0, len(word)-1)

    word = list(word)
    word[index1] = word[index2]
    word = ''.join(word)
    
    return word

def make_i_space(word):
    q_len = Q(len(word), {})
    word.insert(0, '\\')
    word.insert(1, 's')
    word = list(set(word))
    if '\\' in word and 's' in word:
        index_sl = word.index('\\')
        index_sp = word.index('s')
        
        word[index_sl] = word[q_len]
        word[q_len] = '\\'
        
        word[index_sp] = word[q_len+1]
        word[q_len+1] = 's'
    else:
        make_i_space(word)
    return word

def make_i_word(char): #make isogram word
    length = random.randint(2, 15)
    word = ''

    for i in range(length):
        word += random.choice(alphabet)

    word = set(word)
    word = list(word)
    q_len = Q(len(word), {})

    if char == ' ':
        make_i_space(word)
    else:
        if char in word:
            index = word.index(char)
            word[index] = word[q_len]
            word[q_len] = char
        else:
            word[q_len] = char
    
    word = ''.join(word)
    return word
        
text = list(input())
result = ''
ni_word = ''
i_words = ''
for i in text:
    ni_words = random.randint(0, 10) #not isogram words interval
    for j in range(ni_words):
        result += make_ni_word()
        result += ' '
        
    result += make_i_word(i)
    result += ' '

    ni_words = random.randint(0, 10) #not isogram words interval
    for k in range(ni_words):
        result += make_ni_word()
        result += ' '

print(result)
