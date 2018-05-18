def fatorial(num):
	if num == 0:
		return 1
	else:
		return num * fatorial(num - 1)

def combinacao(sub,num):
	return fatorial(num)/(fatorial(p)*fatorial(num - sub))

