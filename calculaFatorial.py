def fatorial(num):
	if num == 0:
		return 1
	else:
		return num * fatorial(num - 1)

x = 4
print(fatorial(x))