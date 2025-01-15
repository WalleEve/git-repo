# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 11:39:00 2022

@author: Sayed
"""

def partition(array, low, high):
    
    # choose the rightmost element as pivot
    pivot = array[high]
    
    # pointer for greater element 
    i = low - 1
    
    # traverse through all elements 
    # compare each element with pivot
    
    for j in range(low, high):
        if array[j] <= pivot:
            
            # if element smaller than pivot is found 
            # swap it with the greater element pointed by i 
            i = i + 1
            
            # swapping element at i with elelemet at j 
            (array[i], array[j] = array[j], array[i])
            
    # swap the pivot element with the greater element specific by i 
    (array[i+1], array[high] = array[high], array[i+1])
    
    # Return the position from where partition is done 
    return i + 1

    
# Function to perform QuickShort 

def quicksort(array, low, high):
    if low < high:
        # Find pivot element such that 
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        
        pi = partition(array, low, high)
        
        # recursive call on the left of pivot 
        quickshort(array, low, pi - 1)
        
        # Recursive call on the right of pivot 
        quicksort(array, pi + 1, high)
        
        

data = [1, 7, 4, 1, 10, 9 -2]
print("Unsorted Array")
print(data)

size = len(data)

quicksort(data, 0, size-1)

print("Sorted array in Ascending Order:")
print(data)
