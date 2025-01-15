# 1. Write a Python program to calculate the length of a string.

a = 'sayed mahfuze raheman'

print(len(a))  # 21 

# python function
def get_string_length(in_str):
    n = 0
    for i in in_str:
        n +=1
    return n

print(get_string_length(a))




# 2. Write a Python program to sum all the items in a list.

l = [2, 5, 7, 9, 12, 17]

print(sum(l)) 

l = [2, 5, 7, 9, 'a', 17]

def get_sum(ln_list):
    n = 0
    for i in ln_list:
        try:
           if int(i):
                print(i)
                n = n + i 
        except:
            print(f"{i} is not a numeric value!")
    return n 

print(get_sum(l))

# using lambda 

# importing functools for reduce()
import functools as fn

l = [2, 5, 7, 9, 12, 17]
result = fn.reduce(lambda x,y: x + y, l)
print(f"The sum of {l} is : {result}")

# 3. Write a Python program to multiplies all the items in a list.

l = [3, 5, 8, 'p', 9]

def get_multiply(ln_list):
    n = 1
    for i in l:
        try:
            if int(i):
                n = n * i 
        except:
            print(f"List {ln_list} contains non numeric value!")
    return n 

print(f"We are getting the multiplication of numeric value exists in the given list {l} is : {get_multiply(l)}")


# 4. Write a Python program to get the largest number from a list. 
l = [3, 6, 9, 1, 12]

def get_greatest(ln_list):
    n = ln_list[0]
    for i in ln_list:
        if n < i:
            n = i 
    return n 

print(f"The Greatest value in {l} is : {get_greatest(l)}")


# using lambda 
# importing functools for reduce()
import functools as fn
l = [25, 2, 5, 31, 7, 9, 19]
greatest = fn.reduce(lambda x, y: x if x > y else y, l)
print(f"greatest value: {greatest}")


# 5. Write a Python program to get the smallest number from a list.

l = [0, 9, 8, -1, 11, 5, 1]

def get_smalest(ln_list):
    n = ln_list[0]
    for i in ln_list:
        if n > i:
            n = i 
    return n 

print(f"Smalest values from the list {l} is: {get_smalest(l)}")

# using lambda function 
# importing functools for reduce()
import functools as fn 

l = [-8, 8, 3, -1, 0, -5]
smalest = fn.reduce(lambda x, y: x if x < y else y, l)
print(f"smalest value from the list {l} is  {smalest}")

# 6. Write a Python program to count the number of characters in a string.
# Sample String : 'google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

def get_letter_count(Is_String):   # Is Input String 
    resultDict = dict()
    cnt = 0
    for i in set(Is_String):
        try:
            cnt = Is_String.count(i)
            resultDict[i] = cnt 
        except:
            print("Please check the String!")
    return resultDict

s = "google.com"
print(get_letter_count(s))


def get_letter_count_2(Is_String):
    resultDict = dict()
    n = 1
    for i in Is_String:
        if i in resultDict.keys():
            resultDict[i] = resultDict[i]+1
        else:
            resultDict[i] = 1
    return resultDict

name = "Yamaha fashino"
print(f"String char count: {get_letter_count_2(name)}")


# 8. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

  
s = ['abc', 'xyz', 'aba', '1221', 'amma', 'eye']

def get_count(lnString):
    #result = []
    n = 0 
    for i in lnString:
        if i[0] == i[-1]:
            n = n+1
    return n 

count_of_string = get_count(s)
print(f"count of string where length is 2 or more and first and last character are same: {count_of_string}")


 # Write a program to sort an given list and add the sorted values to a new list:

a = [0, 2, 6, 8, 1, 5, 4, -1]

b = [] 
b.append(a[0])
ind = 0
flag = False

for i in a[1:]:
    #print(f"i : {i}")
    for j in b:
        #print(f"j : {j}")
        if i < j:
            ind = b.index(j)
            flag = True
            break
        else:
            flag = False
    if  flag:       
        b.insert(ind, i)
        #print(f"B: {b}")
    else:
        b.append(i)
        #print(f"B: {b}")

print(f"B: {b}")

# 9. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Go to the editor
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

a = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

b = [] 
b.append(a[0])
ind = 0
flag = False

for i in a[1:]:
    for j in b:
        if i[1] < j[1]:
            ind = b.index(j)
            flag = True
            break
        else:
            flag = False
    if  flag:       
        b.insert(ind, i)
    else:
        b.append(i)

print(f"given list {a} and after sorted new list is: {b}")            

# Optimized way

def last(n): return n[-1]  
  
def sort_list_last(tuples):  
  return sorted(tuples, key=last)  
  
print(sort_list_last(a))  


# 10. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is \
# less than 2, return instead the empty string. 
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

sam_string = 'w3resource'

if len(sam_string) > 2:
    print(sam_string[0:2]+sam_string[-2:])
elif len(sam_string) == 2:
    print(sam_string * 2)
else:
    print(None)

# Function 
def string_both_ends(str):  
  if len(str) < 2:  
    return ''    
  return str[0:2] + str[-2:] 

print(string_both_ends(sam_string))


# 11.Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor
# Sample String : 'restart'
# Expected Result : 'resta$t'


def change_char(str1):  
  char = str1[0]  
  #length = len(str1)  
  str1 = str1.replace(char, '$')  
  str1 = char + str1[1:]  
  
  return str1  
  
print(change_char('restart'))  

# 

SampleString = 'restart'

def replace_string(lnString):
    temp = ''
    for i in lnString:
        if i not in temp:
            temp = temp+i
        else:
            temp = temp+'$'
    return temp 

print(f"Replaced String: {replace_string(SampleString)}")


# 12. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters 
# of each string. 
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

s1 = 'abc'
s2 = 'xyz'

result = s2[0:2] + s1[-1] + ' ' + s1[0:2] + s2[-1]

print(f"Result String: {result}")



def get_string(inString1, inString2):
    temp1 = inString1[0:2]
    temp2 = inString2[0:2]
    result = temp2 + inString1[2:] +' '+temp1+inString2[2:]
    return result

print(f"Final String {get_string('sayed', 'mahfuze')}") 


def chars_mix_up(a, b):  
  new_a = b[:2] + a[2:]  
  new_b = a[:2] + b[2:]  
  
  return new_a + ' ' + new_b  
print(chars_mix_up('abc', 'xyz')) 

# 13. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string is already ends with 'ing' then add 'ly' instead. If the string length of the given 
# string is less than 3, leave it unchanged. 
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

gstring = 'abc'

def get_ing_at_end(inString):
    if len(gstring) >=3:
        if gstring[-3:] == 'ing' or gstring[-3:] == 'ING':
            return inString+'ly'
        else:
            return inString+'ing'
    else:
        return inString
    
print(f"String: {get_ing_at_end('gstring')}")

# 14. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, 
# if 'bad' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. 
# Sample String : 'The lyrics is not that poor!'
# Expected Result : 'The lyrics is good!'

Sample_String = 'The lyrics is not that poor!'

def replace_string(lnString):    
    index_not = lnString.find('not')
    index_poor = lnString.find('poor')
    replace_string = lnString[index_not: index_poor+4]
    replaced_string = lnString.replace(replace_string, 'good')

    return f"replace string: {replace_string} after replaced string: {replaced_string}"


print(replace_string(Sample_String))


def not_poor(str1):  
  snot = str1.find('not')  
  sbad = str1.find('poor')   
  
  if sbad > snot:  
    str1 = str1.replace(str1[snot:(sbad+4)], 'good')  
  
  return str1  
print(not_poor('The lyrics is not that poor!'))  


# 15. Write a Python function that takes a list of words and returns the length of the longest one.

sample_list = ['sayed', 'mahfuze',  'misha tate', 'raheman']

def get_length(lnList):
    temp = list()
    for i in lnList:
        temp.append(len(i))
        temp.sort()
    return  temp[-1]

print(get_length(sample_list))


def find_longest_word(words_list):  
    word_len = []  
    for n in words_list:  
        word_len.append((len(n), n))  
    word_len.sort()  
    return word_len[-1][1]  
  
print(find_longest_word(["PHP", "Exercises", "Backend"]))  


# 16. Write a Python program to test whether an input is an integer.

def check_input(lnInt):
    try:
        if int(lnInt):
            return "Input is Integer."
    except:
        return "Input is not an Integer!"


a = 10 
print(check_input(a))


def check_input(lnInt):
    if lnInt.isnumeric():
        return "Given Input is an Integer."
    else:
        return "Sorry! Given input is not an Integer!"

a = '10a'
print(check_input(a))


# 17. Write a Python program to sort (ascending and descending) a dictionary by value. 

d = {'hindi': 93, 'english': 67, 'math': 89, 'science': 83, 'history': 35, 'geography': 42}

def dictionary_sort(InDict):
