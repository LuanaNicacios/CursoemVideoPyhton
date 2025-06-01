from datetime import date
ano = int(input('Digite que ano você quer analisar? coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))
