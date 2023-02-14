# Функція для н-ного числа фібоначі
def Fibonacci(n):

	# перевірка що вводять не відємне ч-ло
	if n < 0:
		print("Incorrect input")

	# якщо 0, то вивід 0
	elif n == 0:
		return 0

	# якщо 1 або 2, то вивід 1
	elif n == 1 or n == 2:
		return 1

	else:
		return Fibonacci(n-1) + Fibonacci(n-2)


print(Fibonacci(11))
