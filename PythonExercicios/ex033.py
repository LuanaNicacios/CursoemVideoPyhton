v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))

# Verificando o menor valor
menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3< v2:
    menor = v3
maior = v1
# Verificando o maior valor
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))