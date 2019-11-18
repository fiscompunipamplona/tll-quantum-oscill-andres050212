# **Ejercicio Péndulo Doble** 


from numpy import array, linspace
from math import sin, cos, pi
from pylab import plot, xlabel, ylabel, show
from scipy.integrate import odeint
from vpython import sphere, scene, vector, color, arrow, text, sleep, cylinder

arrow_size = 0.1  #Tamaño de la flecha

arrow_x = arrow(pos=vector(0,0,0), axis=vector(arrow_size,0,0), color=color.red)
arrow_y = arrow(pos=vector(0,0,0), axis=vector(0,arrow_size,0), color=color.green)
arrow_z = arrow(pos=vector(0,0,0), axis=vector(0,0,arrow_size))

R = 0.03 #Radio de la esfera


###### Función Principal ###### 

def func (conds, t, g, l): 
    dc1=conds[4]
    dd1=conds[5]
    dthe1=conds[1]
    dc=(1/2)*(-(conds[5])*cos(conds[0]-conds[2])-((conds[2])**2)*sin(conds[0]-conds[2]))-(g/l)*sin(conds[0])
    dthe2=conds[3]
    dd=-(conds[4])*cos(conds[0]-conds[2])+((conds[1])**2)*sin(conds[0]-conds[2])-(g/l)*sin(conds[2])
    return array([dthe1,dc,dthe2,dd,dc1,dd1], float)

#####################################################################

###### Condiciones Iniciales ######
g = 9.8
l = 0.2

the1=pi/2.
c=0.
the2=pi/2
d=1.
dc=0.
dd=0.

initcond = array([the1,c,the2,d,dc,dd])

#####################################################################


###### Tiempo Del Problema ######

n_steps = 5000 #Número de pasos
t_start = 0.   #Tiempo inicial
t_final = 12.  #Tiempo final
t_delta = (t_final - t_start) / n_steps #Diferencial de tiempo (Paso temporal)
t = linspace(t_start, t_final, n_steps) #Arreglo de diferencial de tiempo

#####################################################################


###### Solución Del Problema Con Odeint ######

solu, outodeint = odeint( func, initcond, t, args = (g, l), full_output=True) 

the_1,cc,the_2,dd,c2,d2 = solu.T 

#####################################################################


###### Datos Para La Animación ######


scene.range = 0.5 #Tamaño de la escena


###### Posiciones en coord. Polares ######

xp = l*sin(the1) 
yp = -l*cos(the1)
zp = 0.

xs=l*(sin(the1)+sin(the2))
ys=-l*(cos(the1)+cos(the2))
zs=0.

####################################################################


sleeptime = 0.0001 #Tiempo de actualización

###### Figuras para la animación ######

prtcl1 = sphere(pos=vector(xp,yp,zp), radius=R, color=color.red) 
prtcls1= sphere(pos=vector(xs,ys,zs), radius=R, color=color.blue)
cyl1= cylinder(pos=vector(0,0,0), radius=l/40, color=color.yellow)
cyl2= cylinder(pos=vector(xp,yp,0), radius=l/40, color=color.yellow)

######################################################################


###### Animación ######

time_i = 0 
t_run = 0  

while t_run < t_final: 
    vector1 = vector( l*sin(the_1[time_i]), -l*cos(the_1[time_i]), zp )
    vector2 = vector( l*(sin(the_1[time_i])+sin(the_2[time_i])), -l*(cos(the_1[time_i])+cos(the_2[time_i])), zs )
    
    
    cyl1.axis = vector1
    prtcl1.pos = vector1
    
    cyl2.pos = vector1
    cyl2.axis = vector2
    prtcls1.pos = vector1 + vector2
    
    t_run += t_delta
    sleep(sleeptime)
    time_i += 1

