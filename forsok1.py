from pylab import *
import matplotlib.style as style
style.use('dark_background')
title('Forsøk 1')
xlabel('Tid')
ylabel('Temp')
temperatur = [9,29.9,30,30.4,30.5,30.4,32.1,32.3,32.1,30.9,31.6,31.7,30.5,32.3,31.9,31.6,31.1,31.6,32.4,32.1,31,30.2,29.2,29.1,29.3,28,28.1,27.3,27.2,25.6,25.1]
tid = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155]
plot(tid,temperatur)
show()
