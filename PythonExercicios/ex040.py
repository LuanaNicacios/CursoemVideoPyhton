nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Sua media foi \033[1;31m {}\033[m abaixo de \033[1;31m 5\033[m, você está: '
          '\033[1;31m REPROVADO!\033[m'.format(media))
elif media >= 5 and media < 6.9:
    print('Sua média foi, \033[1;33m {:.2f}\033[m e está em entre \033[1;33m 5 e 6.9\033[m você está em: '
          '\033[1;33m RECUPERAÇÃO!\033[m'.format(media))
else:
    print('Sua média foi \033[1;32m {}\033[m, você está \033[1;32m APROVADO!\033[m'.format(media))

#CODIGO GUANABARA#
"""
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media)) ')
if 7 > média >= 5:
    print('O aluno está em RECUPERAÇÃO!!!')
elif média < 5: 
    print('O aluno está em REPROVADO!!!') 
elif média >= 7:
    print('O aluno está APROVADO!!!')
"""