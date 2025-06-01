print('-='*20)
print('ANALISANDO UM TRIÂNGULO')
print('-='*20)
c1 = float(input('Primeiro Segmento: '))
c2 = float(input('Segundo Segmento: '))
c3 = float(input('Terceiro Segmento: '))

if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('Os Segmentos acima PODEM FORMAR UM triângulo')
else:
    print('Os Segmento acima NÃO PODEM FORMAR UM triângulo')