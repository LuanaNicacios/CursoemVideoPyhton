numero = int(input('Digite um número inteiro qualquer: '))
binario = bin(numero)[2:]
octal = oct(numero)[2:]
hexadecimal = hex(numero)[2:]

print('-='*20)
print('Escolha uma das bases para conversão: ')
print('\033[1;32m [ 1 ]\033[m Converter para: \033[1;35m BINÁRIO \033[m')
print('\033[1;32m [ 2 ]\033[m Converter para: \033[1;34m OCTAL \033[m')
print('\033[1;32m [ 3 ]\033[m Converter para: \033[1;33m HEXADECIMAL \033[m')
print('-='*20)
opcao = int(input('Digite a opção para qual você quer converter: '))
print('-='*20)

if opcao == 1:
    print('\033[1;32m [ 1 ]\033[m Convertendo para \033[1;35m BINÁRIO\033[m...')
    print('O número: \033[1;31m{}\033[m Convertido para \033[1;35m BINÁRIO\033[m é igual a: \033[1;32m {}\033[m'.format(numero, binario))
elif opcao == 2:
    print('\033[1;32m [ 2 ]\033[m Convertendo para \033[1;34m OCTAL\033[m...')
    print('O número: \033[1;31m{}\033[m Convertido para \033[1;34m OCTAL\033[m é igual a: \033[1;32m {}\033[m'.format(numero, octal))
elif opcao == 3:
    print('\033[1;31m [ 3 ]\033[m Convertendo para \033[1;33m HEXADECIMAL\033[m...')
    print('O número: \033[1;32m {}\033[m Convertido para \033[1;33m HEXADECIMAL\033[m é igual a: \033[1;32m {}\033[m'.format(numero, hexadecimal))
else:
    print('Opção \033[1;32m INVALIDA! \033[m')

# GUNABARA CÓDIGO #
"""
num = int(input('Digite um número inteiro: '))
print(
'[1] Converter para BINÁRIO
 [2] Converter para OCTAL
 [3] Converter para HEXADECIMAL')
 opcao = int(input('Sua opção: ')
 if opção == 1:
    print('{} converdido para BINÁRIO é igual a {}'.format(num, bin(num)[2:])
 elif opcao == 2:
    print('{} converdido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
 elif opcao == 3:
    print('{} converdido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
 else:
    print('Opção INVALIDA! Tente novamente')
 
"""


