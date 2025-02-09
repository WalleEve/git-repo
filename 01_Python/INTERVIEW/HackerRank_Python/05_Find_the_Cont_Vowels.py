"""
re.findall()
The expression re.findall() returns all the non-overlapping matches of patterns in a string as a list of strings.
Code

>>> import re
>>> re.findall(r'\w','http://www.hackerrank.com/')
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
re.finditer()
The expression re.finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string.
Code

>>> import re
>>> re.finditer(r'\w','http://www.hackerrank.com/')
<callable-iterator object at 0x0266C790>
>>> map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
Task
You are given a string . It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of  that contains  or more vowels.
Also, these substrings must lie in between  consonants and should contain vowels only.

Note :
Vowels are defined as: AEIOU and aeiou.
Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.

Input Format

A single line of input containing string .

Constraints


Output Format

Print the matched substrings in their order of occurrence on separate lines.
If no match is found, print -1.

Sample Input

rabcdeefgyYhFjkIoomnpOeorteeeeet
Sample Output

ee
Ioo
Oeo
eeeee
Explanation

ee is located between consonant  and .
Ioo is located between consonant  and .
Oeo is located between consonant  and .
eeeee is located between consonant  and .
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

s = input()

Vowels = ['A', 'E', 'I', 'O', 'U']
Consonants = ['Q', 'W', 'R', 'T', 'Y', 'P', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

i = None
j = None
cnt = 0
str = ''
flag = False


for x in range(len(s)):
    str = ''
    if not i:
        if s[x].upper() in Consonants:
            i = x
    else:
        if s[x].upper() in Consonants:
            j = x
        if j:
            if len(s[i:j+1]) >= 4:
                for y in s[i:j+1]:
                    if y.upper() in Vowels:
                        str = str + y
                    i = j
                if len(str) >= 2:
                    print(str)
                    flag = True
                    continue
            else:
                i = j
                j = None
if not flag:
    print(-1)