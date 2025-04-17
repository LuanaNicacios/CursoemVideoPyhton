nome = input('Qual o seu nome? ')
print('prazer em te conhecer {:20}!!'.format(nome))
print('Prazer em te conhecer {:>20}!!'.format(nome))
print('Prazer em te conhecer {:<20}!!'.format(nome))
print('Prazer em te conhecer {:^20}!!'.format(nome))

num1 = int(input('Um valor: '))
num2 = int(input('Outro valor: '))
s = num1 + num2
m = num1 * num2
d = num1 / num2
e = num1 ** num2
di = num1 // num2
rd = num1 % num2
print('A soma é: {}, \n a multiplicação é: {} \n e a divisão é: {:.3}'.format(s, m, d), end=' ')
print('Divisão inteira é: {} e potência é: {}'.format(di, e))


