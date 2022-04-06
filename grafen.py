from matplotlib import pyplot
import math
import numpy as np
from pylab import *
temperatur = [9,29.9,30.4,30.5,30.4,32.1,32.3,32.1,30.9,31.6,31.7,30.5,32.3,31.9,31.6,31.1,31.6,32.4,32.1,30.2,29.2,29.1,29.3,28,28.1,27.3,27.2,25.6,25.1,25.2]
tid = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]


def f(x):
    #if 0 <= x <= 5
    return 20.9*x + 9

x = np.linspace(0,10)
pyplot.plot(x,f(x),tid,temperatur,'o')
pyplot.ylim(35)
fig = pyplot.figure()
a1 = fig.add_axes([0,0,1,1])
#a1.set_ylim(20)
a1.plot(x,f(x))
a1.set_title('Temperatur')
pyplot.show()
