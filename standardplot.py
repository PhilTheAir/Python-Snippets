import matplotlib.pyplot as plt
import numpy as np

def graphtt(xx):
  y = []
  #print(xx)
  for x in xx:
    if x <= 1000:
      y.append(10 / x)
    elif x <= 10000:
      y.append(19.95 / x)
    elif x <= 25000:
      y.append(29.95 / x)
    else:
      y.append(0.0012)
  return y

x = np.linspace(500, 30000, 25000)
y = graphtt(x)
plt.plot(x, y)
plt.show()