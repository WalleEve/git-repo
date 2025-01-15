'''
Created on 26-Dec-2023

@author: sayed
'''

l = [5, 1, 2, 6, 8, 1, 5, 3, 2, 1, 9, 1, 3, 5, 6, 1, 3, 1]

# find the duplicate values and number of occurrence

duplicate_values = []
occurrence = []
cnt = 1


for i in range(len(l)):
    if l[i] not in duplicate_values:
        for j in range(i + 1, len(l)):
            if l[i] == l[j]:
                cnt += 1
        if cnt > 1:
            duplicate_values.append(l[i])
            occurrence.append(cnt)
        cnt = 1
print(list(zip(duplicate_values, occurrence)))

