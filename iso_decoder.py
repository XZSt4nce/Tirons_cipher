"""
Iterates through the words in the text. If the word is an isogram, then the first letter is taken and added to the result, otherwise it is skipped. Isogram - a combination of letters, numbers, in which there are no repetitions
"""
from sys import setrecursionlimit
setrecursionlimit(100000)
def Q(n, results):
    if n == 1 or n == 2: return 1
    elif n in results: return results[n]
    else:
        res = Q(n - Q(n - 1, results), results) + Q(n - Q(n - 2, results), results)
        results[n] = res
        return res
def iso_check(word):
    return True if len(word) == len(set(word)) else False
s = input().split(' ')
res=''
for i in s:
    if iso_check(i):
        if i[:2] == '\\s':
            res += ' '
        else:
            res += i[Q(len(i), {})]
print(res)
