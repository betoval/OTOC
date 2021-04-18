import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(10,9))
x = np.linspace(0, 3, 500)
y = np.exp(5*x)
otoc = 1/((1+(1/1000)*y))**2
c = 2-2*otoc
plt.plot(x, otoc, label='$OTOC(t)$', color='red')
plt.plot(x, c, label='$C(t)$', color='blue')

plt.xlabel('$t$', fontsize=16)
plt.legend(bbox_to_anchor=(1,1), loc='upper left', fontsize=16)
fig.savefig('plot.png')
plt.show()
