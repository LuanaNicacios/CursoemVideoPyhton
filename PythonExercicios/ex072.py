#Meu Código
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um Número entre 0 e 20: '))
    if num <= 20:
        print(f'0 Número digitado foi, {extenso[num]}.')
    else:
        print('O número Digitado não está entre 0 e 20.')


#GUANABARA CÓDIGO
'''
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20
        break
    print('Tente Novamente.', end='')
print(f'Você digitou o número {cont[núm]}')
'''

