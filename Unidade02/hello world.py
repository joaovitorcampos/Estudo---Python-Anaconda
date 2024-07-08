print('Hello World')
numeros = list(range(1,101))
print(type(numeros))
for n in numeros:
	if n % 2 == 0 and n % 4 == 0:
		print(n)
pares_div4 = [numero for numero in numeros if numero % 2 == 0 and numero % 4 == 0]
print(pares_div4)