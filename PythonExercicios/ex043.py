peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura: '))
imc = peso /(altura * altura)
#cores = {'verde':'\033[1;32m','vermelho':'\033[1;31m',
         #'amarelo':'\033[1;33m', 'azul':'\033[1;34m'}
print('O seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('IMC abaixo de 18,5: \033[1;31m ABAIXO DO PESO!\033[m ')
elif 18.5 <= imc < 25:
    print('IMC entre 18.5 e 25: \033[1;32m NORMAL!\033[m ')
elif 25 <= imc < 30:
    print('IMC entre 25 e 30: \033[1;33m SOBREPESO!\033[m ')
elif 30 <= imc < 40:
    print('IMC entre 30 e 40: \033[1;31m OBESIDADE!\033[m ')
else:
    print('IMC entre 40 e 40: \033[1;31m OBESIDADE MORBIDA!!!\033[m ')