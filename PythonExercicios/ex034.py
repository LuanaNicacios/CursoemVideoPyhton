salario = int(input('Digite o salario do funcionario: '))
salarionovo1 = salario + (salario * 0.10)
salarionovo2 = salario + (salario * 0.15)

if salario <= 1250:
    print('Quem ganhava {:.2f} com 15% de aumento ira ganhar: {:.2f} R$'.format(salario, salarionovo2))
else:
    print('Quem ganhava {:.2f} com 10% de aumento ira ganhar {:.2f} R$'.format(salario, salarionovo1))


