from math import radians, sin, cos, tan
ag = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ag))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ag, seno))
coss = cos(radians(ag))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ag, coss))
tag = tan(radians(ag))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ag, tag))
