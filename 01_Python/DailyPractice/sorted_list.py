'''
Created on 26-Dec-2023

@author: sayed
'''

l = [1, 5, 9, 8, 7, 3, 6, 2, 4, -1, 23, 0, 19, 1, 16]
sorted_list = []

for i in l:
    print(i)
    if len(sorted_list) == 0:
        sorted_list.append(i)
    else:
        for j in range(len(sorted_list)):
            if i < sorted_list[j]:
                if len(sorted_list) - 1 == j:
                    sorted_list.append(i)
                else:
                    continue
            else:
                sorted_list.insert(j, i)
                break

print(sorted_list)