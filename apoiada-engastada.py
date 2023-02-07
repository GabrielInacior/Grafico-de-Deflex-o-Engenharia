import matplotlib.pyplot as plt
#Viga Engastada-Apoiada
#Camile e Gabriel


I= 106.7
E= 200000
F= 20
l=650
a=l/2
Va = ((3*F*(l-a))/(2*l))-((F*((l-a)**3))/(2*(l**3)))
Vb = F-Va
Ma=(Va*l - F*(l-a))
A2=0
A1 = 0
u1=[]
x1=[]
dx=0
cont=0
k=0.0001
while dx<l:
    if dx<a:
        u1.append((((Va / 6) * (dx ** 3) - ((Ma / 2)) * (dx - 0) ** 2 +A1 * dx) / (E * I)))
        x1.append(dx)
        dx = dx + k
        cont = cont+1

    elif dx<l:
         u1.append((((Va / 6) * (dx ** 3) - ((Ma / 2)) * (dx - 0) ** 2 - (F / 6) * ((dx - a) ** 3) + A1 * dx) / (E * I)))
         x1.append(dx)
         dx = dx + k
         cont = cont + 1
    else:
         u1.append(0)
         x1.append(dx)
         dx = dx + k
         cont = cont + 1

#Para u2
I = 106.7
E = 200000
F = 5
l = 650
a = l / 2
Va = ((3 * F * (l - a)) / (2 * l)) - ((F * ((l - a) ** 3)) / (2 * (l ** 3)))
Vb = F - Va
Ma = (Va * l - F * (l - a))
A2 = 0
A1 = 0
u2 = []
x2 = []
dx = 0
cont = 0
k = 0.0001

while dx < l:
     if dx<a:
         u2.append((((Va / 6) * (dx ** 3) - ((Ma / 2)) * (dx - 0) ** 2 + A1 * dx) / (E * I)))
         x2.append(dx)
         dx = dx + k
         cont = cont + 1
     elif dx<l:
        u2.append((((Va / 6) * (dx ** 3) - ((Ma / 2)) * (dx - 0) ** 2 - (F / 6) * ((dx -a) ** 3) + A1 * dx) / (E * I)))
        x2.append(dx)
        dx = dx + k
        cont = cont + 1
     else:
        u2.append(0)
        x2.append(dx)
        dx = dx + k
        cont=cont+1

 #Para u3

I= 106.7
E= 200000
F= 10
l=650
a=l/2
Va = ((3*F*(l-a))/(2*l))-((F*((l-a)**3))/(2*(l**3)))
Vb = F-Va
Ma=(Va*l - F*(l-a))
A2=0
A1 = 0
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
    elif dx<l:
     u3.append( (((Va/6)*(dx**3)-((Ma/2))*(dx-0)**2 - (F/6)*((dx -a)**3) + A1*dx )/( E*I)) )
     x3.append(dx)
     dx=dx+k
     cont=cont+1
    else:
     u3.append(0)
     x3.append(dx)
     dx=dx+k
     cont=cont+1

#Para u4
I= 106.7
E= 200000
F= 15
l=650
a=l/2
Va = ((3*F*(l-a))/(2*l))-((F*((l-a)**3))/(2*(l**3)))
Vb = F-Va
Ma=(Va*l - F*(l-a))
A2=0
A1 = 0
u4=[]
x4=[]
dx=0
cont=0
k=0.0001
while dx<l:
    if(dx<a):
     u4.append( (((Va/6)*(dx**3)-((Ma/2))*(dx-0)**2 + A1*dx )/( E*I)))
     x4.append(dx)
     dx=dx+k
     cont=cont+1
    elif(dx<l):
     u4.append( (((Va/6)*(dx**3) - (F/6)*((dx - a)**3)-((Ma/2))*(dx-0)**2 + A1*dx )/( E*I)) )
     x4.append(dx)
     dx=dx+k
     cont=cont+1
    else:
     u4.append(0)
     x4.append(dx)
     dx=dx+k
     cont=cont+1

#Plotando os Gráficos

fig,ax = plt.subplots(figsize=(15, 8))
ax.plot(x2, u2,label='U teorica,(5 N)',color='orange')
ax.plot(100,-0.19,'o',label='U experimental,(5)',color='orange')
ax.plot(325,-0.49,'o',color='orange')
ax.plot(380,-0.55,'o',color='orange')
ax.plot(535,-0.29,'o',color='orange')
ax.plot(x3, u3,label='U teorica,(10 N)',color='green')
ax.plot(100,-0.38,'o',label='U experimental,(10N)',color='green')
ax.plot(325,-1.04,'o',color='green')
ax.plot(380,-1.05 ,'o',color='green')
ax.plot(535,-0.6,'o',color='green')
ax.plot(x4, u4,label='U teorica,(15 N)',color='red')
ax.plot(100,-0.61,'o',label='U experimental,(15N)',color='red')
ax.plot(325,-1.6,'o',color='red')
ax.plot(380,-1.6 ,'o',color='red')
ax.plot(535,-0.85,'o',color='red')
ax.plot(x1, u1,label='U teorica,(20 N)',color='blue')
ax.plot(100,-0.78,'o',label='U experimental,(20N)',color='blue')
ax.plot(325,-2.1,'o',color='blue')
ax.plot(380,-2.1,'o',color='blue')
ax.plot(535,-1.2,'o',color='blue')
plt.title('Viga Apoiada-Engastada')
plt.xlabel('L (mm)')
plt.ylabel('U (mm)')
ax.legend()
plt.show()
