soma = 0
cont = 0
for c in range (1, 7):
    n = float(input('Digite um valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))


