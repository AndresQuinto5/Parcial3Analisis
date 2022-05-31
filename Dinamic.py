# Programa de python que imprime la sumatoria del array contiguo

from sys import maxsize
import timeit

# Funcion para encontrar el sub array contiguo maximo
# 
# Tambien imprimie su índice inicial y final
def maxSubArraySum(a,size):

	max_so_far = -maxsize - 1
	max_ending_here = 0
	start = 0
	end = 0
	s = 0

	for i in range(0,size):

		max_ending_here += a[i]

		if max_so_far < max_ending_here:
			max_so_far = max_ending_here
			start = s
			end = i

		if max_ending_here < 0:
			max_ending_here = 0
			s = i+1

	print ("Maximum contiguous sum is %d"%(max_so_far))
	print ("Starting Index %d"%(start))
	print ("Ending Index %d"%(end))

# Main
a = [-2, -3, 4, -1, -2, 1, 5, -3]

inicio = timeit.timeit()
maxSubArraySum(a,len(a))
final = timeit.timeit()

print("Tiempo total: ", final - inicio)