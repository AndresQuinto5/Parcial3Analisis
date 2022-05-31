import timeit
import sys 

#Programa en Python para encontrar el subarray contiguo maximo
from sys import maxsize
def maxSubArraySum(a,size):
    
    max_so_far = -maxsize - 1
    max_ending_here = 0
    
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0  
    return max_so_far

# Main
a = [0, 7, 10, 13, -2, 23, -98, 71, -66, 41, -15, -99, -70, 55, 21, -30, 88, -22, 36, 20]
inicio = timeit.timeit()
print("Maximum contiguous sum is", maxSubArraySum(a,len(a)))
final = timeit.timeit()
print("\nTiempo total:\n", abs(final - inicio), "\n")