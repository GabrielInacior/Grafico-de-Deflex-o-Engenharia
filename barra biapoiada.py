import matplotlib
import  numpy
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import BSpline,make_interp_spline

#Gabriel e Camile 

import matplotlib.pyplot as plt
I= 106.7
E= 200000
F= 20
l=650
a=l/2
Va = ((F*l - F*a)/(l))
Vb = F - Va
A2=0
A1 = (-(Va/6)*l**3 + (F/6)*(l-a)**3)/l
u1=[]
x1=[]
dx=0
cont=0
k=0.0001


#para u1
while dx<l:
    if dx<a:
        u1.append( (((Va/6)*(dx**3) + A1*dx )/( E*I )) )
        x1.append(dx)
        dx=dx+k
        cont=cont+1
    elif dx<l:
        u1.append( (((Va/6)*(dx**3) - (F/6)*((dx - a)**3) +
        A1*dx )/( E*I)) )
        x1.append(dx)
        dx=dx+k
        cont=cont+1
    else:
        u1.append(0)
        x1.append(dx)
        dx=dx+k
        cont=cont+1
#para u2
I= 106.7
E= 200000
F= 5
l=650
a=l/2
Va = ((F*l - F*a)/(l))
Vb = F - Va
A2=0
A1 = (-(Va/6)*l**3 + (F/6)*(l-a)**3)/l
Ma=(Va*l - F*(l-a))
u2=[]
x2=[]
dx=0
cont=0
k=0.0001

while dx<l:
    if dx<a:
        u2.append( (((Va/6)*(dx**3) + A1*dx )/( E*I )) )
        x2.append(dx)
        dx=dx+k
        cont=cont+1
    elif dx<l:
        u2.append( (((Va/6)*(dx**3) - (F/6)*((dx - a)**3) +
        A1*dx )/( E*I)) )
        x2.append(dx)
        dx=dx+k
        cont=cont+1
    else:
        u2.append(0)
        x2.append(dx)
        dx=dx+k
        cont=cont+1
#para u3

I= 106.7
E= 200000
F= 10
l=650
a=l/2
Va = ((F*l - F*a)/(l))
Vb = F - Va
A2=0
A1 = (-(Va/6)*l**3 + (F/6)*(l-a)**3)/l
u3=[]
x3=[]
dx=0
cont=0
k=0.0001

while dx<l:
    if(dx<a):
        u3.append( (((Va/6)*(dx**3)-((Ma/2))*(dx-0)**2 + A1*dx )/( E*I)))
        x3.append(dx)
        dx=dx+k
        cont=cont+1
    elif(dx<l):
        u3.append( (((Va/6)*(dx**3)-((Ma/2))*(dx-0)**2 - (F/6)*((dx -a)**3) + A1*dx )/( E*I)))
        x3.append(dx)
        dx=dx+k
        cont=cont+1
    else:
        u3.append(0)
        x3.append(dx)
        dx=dx+k
        cont=cont+1
#para u4
I= 106.7
E= 200000
F= 15
l=650
a=l/2
Va = ((F*l - F*a)/(l))
Vb = F - Va
A2=0
A1 = (-(Va/6)*l**3 + (F/6)*(l-a)**3)/l
u4=[]
x4=[]
dx=0
cont=0
k=0.0001
while dx<l:
    if dx<a:
        u4.append( (((Va/6)*(dx**3) + A1*dx )/( E*I )) )
        x4.append(dx)
        dx=dx+k
        cont=cont+1
    elif dx<l:
        u4.append( (((Va/6)*(dx**3) - (F/6)*((dx - a)**3) +
        A1*dx )/( E*I)) )
        x4.append(dx)
        dx=dx+k
        cont=cont+1
    else:
        u4.append(0)
        x4.append(dx)
        dx=dx+k
        cont=cont+1

fig,ax = plt.subplots(figsize=(15, 8))
ax.plot(x2, u2,label='U teorica,(5 N)',color='red')
ax.plot(100,-0.62,'o',label='U experimental,(5N)',color='red')
ax.plot(325,-1.19,'o',color='red')
ax.plot(380,-1,'o',color='red')
ax.plot(535,-0.65,'o',color='red')
ax.plot(x3, u3,label='U teorica,(10 N)',color='blue')
ax.plot(100,-1,'o',label='U experimental,(10N)',color='blue')
ax.plot(325,-2.05,'o',color='blue')
ax.plot(380,-1.80 ,'o',color='blue')
ax.plot(535,-1.17,'o',color='blue')
ax.plot(x4, u4,label='U teorica,(15 N)',color='orange')
ax.plot(100,-1.40,'o',label='U experimental,(15N)',color='orange')
ax.plot(325,-2.90,'o',color='orange')
ax.plot(380,-2.50 ,'o',color='orange')
ax.plot(535,-1.66,'o',color='orange')
ax.plot(x1, u1,label='U teorica,(20 N)',color='green')
ax.plot(100,-1.90,'o',label='U experimental,(20N)',color='green')
ax.plot(325,-3.95,'o',color='green')
ax.plot(380,-3.60,'o',color='green')
ax.plot(535,-2.30,'o',color='green')
plt.title('Viga biapoiada')
plt.xlabel('L(mm)')
plt.ylabel('U(mm)')
plt.grid()
ax.legend()
plt.show()

