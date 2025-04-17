#Exercício 11 -- pintor#
a = float(input('Dígite a altura da parede: '))
l = float(input('Dígite a largura da parede: '))
ca = a*l
v = ca/2
print('O calculo da aréa em metros quadrados é: {} '
      'e serão necessarios: {:.2f} galões para pintar essa aréa.'.format(ca, v))


#Correção do exercício 11 #
print('-- OUTRA FORMA DE FAZER O MESMO CÓDIGO --')
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
tinta = área / 2
print('Sua parede tem a dimenssão de {} x {} e sua área é de {}m.'.format(larg, alt, área))
print('Para pintar essa parede você precisará de {}l de tinta'.format(tinta))