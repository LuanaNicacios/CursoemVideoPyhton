from time import sleep
for num in range (1, 51):
    if num % 2 == 0:
        print('Os Números pares de \033[1;33m 1\033[m até \033[1;33m 50\033[m são: \033[1;32m{}\033[m'.format(num))
        sleep(0.5)
print('-FIM-')

#MEU CODÍGO CORRIGIDO GUANABARA
"""
from time import sleep
for num in range (2, 51, 2): #Vai fazer a mesma função com, menos iteração e memoria. 
        print('Os Números pares de \033[1;33m 1\033[m até \033[1;33m 50\033[m são: \033[1;32m{}\033[m'.format(num))
        sleep(1)
print('-FIM-')
"""
#GUADNABARA CODE#
"""
#O codigo escrito dessa forma faz o laço/for duas vezes
for n in range (1, 51):
    print('.', end='')
    if n % 2 == 0:
        print('n, end=' ')
print('ACABOU!')

#GUANABARA SEGUNDO CODÍGO
#MESMA SOLUÇÃO COM METADE DAS ITERAÇÕES / MAIS LEVE. 
for n in range (2, 51, 2):
    print('.', end='')
    print(n, end=' ')
print('ACABOU!')
    
"""