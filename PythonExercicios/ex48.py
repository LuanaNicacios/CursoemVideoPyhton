soma = 0
cont = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        soma = soma + num
        cont = cont + 1
print(' A soma de todos os {} valores de números ímpares divisivíel por 3 é: \033[1;32m{}\033[m'.format(cont, soma))


