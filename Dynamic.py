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


flag = 0
while flag <= 1:
# Main
	a = [-53,-58,-54,-19,73,-21,28,-77,-32,90,35,-98,-78,69,32,70,-42,-36,75,-85,-1,76,-43,-58,62,9,54,92,-16,40,-95,86,-55,-81,-46,-63,68,-66,-53,-29,90,18,27,-87,-64,63,-5,-19,-61,82]
	inicio = timeit.timeit()
	print("Maximum contiguous sum is", maxSubArraySum(a,len(a)))
	final = timeit.timeit()
	print(abs(final - inicio))
	flag += 1