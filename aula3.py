## exercicios de plano inclinado ###

import numpy as np

m = int(input('digite massa em kg'))
g = float(input('digite o valor de g em m/s**2'))
theta = math.radians(float(input('digite o angulo em graus')))
ca = float(input('digite o valor do coeficiente de atrito'))

normal = m*g*np.cos(theta)
aceleracao = g*(np.sin(theta))-ca*np.cos(theta)

print('A normal é {0:.2f}'.format(normal))
print('a aceleração é {0:.2f}'.format(aceleracao))