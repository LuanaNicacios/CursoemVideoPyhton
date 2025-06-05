num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('O número: \033[1;32m {},\033[m é maior que o número: \033[1;32m {}.\033[m '.format(num1, num2))
elif num1 < num2:
    print('O número: \033[1;32m {},\033[m é maior que o número: \033[1;32m {}.\033[m '.format(num2, num1))
elif num1 == num2:
    print('\033[1;31m Os números são equivalentes \033[m')
else:
    print('\033[1;31m Você deve digitar apenas números !!!')