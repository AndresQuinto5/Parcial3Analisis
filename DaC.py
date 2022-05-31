# Programa de Divide and Conquer 
# para el prblema de Maximum Subarray Sum

# Encontrar la suma maxima posible en
# arr[] tal que arr[m] es parte de este. 

import timeit


def maxCrossingSum(arr, l, m, h):

	# Incluir elementos de la izqIierda de la mitad 
	sm = 0
	left_sum = -10000

	for i in range(m, l-1, -1):
		sm = sm + arr[i]

		if (sm > left_sum):
			left_sum = sm

	# Incluir elementos de la derecha de la mitad 	
	sm = 0
	right_sum = -1000
	for i in range(m + 1, h + 1):
		sm = sm + arr[i]

		if (sm > right_sum):
			right_sum = sm

	# Regresar la suma de elementos en la izquierda y derecha de la mitad
	# Retorna solo left_sum + right_sum que fallara [-2, 1]

	return max(left_sum + right_sum, left_sum, right_sum)


# Devuelve la suma del subarreglo de suma máxima en aa[l..h]
def maxSubArraySum(arr, l, h):

	# Caso base: solo un elemento
	if (l == h):
		return arr[l]

	# Encuentra el punto medio
	m = (l + h) // 2

	# Devolver máximo de los siguientes tres casos posibles
	# a) Suma máxima de subarreglo en la mitad izquierda
	# b) Suma máxima de subarreglo en la mitad derecha
	# c) Suma máxima de subarreglo tal que el
	#	subarreglo cruza el punto medio
	
	return max(maxSubArraySum(arr, l, m),
			maxSubArraySum(arr, m+1, h),
			maxCrossingSum(arr, l, m, h))


# Main
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
n = len(arr)

inicio = timeit.timeit()
max_sum = maxSubArraySum(arr, 0, n-1)
print("Maximum contiguous sum is ", max_sum)
final = timeit.timeit()
print("\nTiempo total:\n", abs(final - inicio), "\n")

