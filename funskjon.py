from pylab import *
import matplotlib.style as style
style.use('dark_background')
title('En graf over Temperaturen')
xlabel('Tid')
ylabel('Temp')
temperatur = [9,29.9,30.4,30.5,30.4,32.1,32.3,32.1,30.9,31.6,31.7,30.5,32.3,31.9,31.6,31.1,31.6,32.4,32.1,30.2,29.2,29.1,29.3,28,28.1,27.3,27.2,25.6,25.1,25.2]
tid = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150]

interval1 = [9,29.9]
tid1 = [5,10]

interval2 = [29.9,32.4]
#fra 10 te 90 pa x-aksen
tid2 = [10,90]

interval3 = [32.4,25]
tid3 = [90,146]

plot(tid,temperatur, 'o', label="data")
plot(tid1,interval1,label="graf1")
plot(tid2,interval2,label="graf2")
plot(tid3,interval3,label="graf3")
legend() # denna displaye bare labelene
show()
