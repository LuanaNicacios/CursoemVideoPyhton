casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos = float(input('Digite em quantos anos você quer financiar a casa ? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para ppagar uma casa de R$ em {:.2f} em {} anos'.format(casa, anos, end=''))
print('A prestação sera de R$ {:.2f}'.format(prestacao))
if prestacao <= minimo:
        print('Empréstimo APROVADO!')
else:
        print('Empréstimo NEGADO!')
