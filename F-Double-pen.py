# **Ejercicio Péndulo Doble** 


from numpy import array, linspace
from math import sin, cos, pi
from pylab import plot, xlabel, ylabel, show
from scipy.integrate import odeint
from vpython import sphere, scene, vector, color, arrow, text, sleep, cylinder

arrow_size = 0.3  #Tamaño de la flecha

arrow_x = arrow(pos=vector(0,0,0), axis=vector(arrow_size,0,0), color=color.red)
arrow_y = arrow(pos=vector(0,0,0), axis=vector(0,arrow_size,0), color=color.green)
arrow_z = arrow(pos=vector(0,0,0), axis=vector(0,0,arrow_size))

R = 0.03 #Radio de la esfera


###### Función Principal ###### 

def func (r, t, g, l): 
    the1 = r[0]
    ome1 = r[1]
    the2 = r[2]
    ome2 = r[3]
    
    f_ome1 = - (ome1 ** 2 * sin(2 * the1 - 2 * the2) + 2 * ome2 ** 2 * sin(the1 - the2) + \
                  g / l * (sin(the1 - 2 * the2) + 3 * sin(the1))) / (3 - cos(2 * the1 - 2 * the2))
    f_ome2 = (4 * ome1 ** 2 * sin(the1 - the2) + ome2 ** 2 * sin(2 * the1 - 2 * the2) + \
                 2 * g / l * (sin(2 * the1 - the2) - sin(the2))) / (3 - cos(2 * the1 - 2 * the2))
    
    return array([ome1,f_ome1,ome2,f_ome2], float)

#####################################################################

###### Condiciones Iniciales ######

g = 9.81  # m/s^2
m = 1. # kg
l = 0.2  # longitud del péndulo
the1_1 = pi/2. 
the2_1 = pi/2.
ome1_1 = 0.
ome2_1 = 0.

#####################################################################


###### Tiempo Del Problema ######

n_steps = 100000 #Número de pasos
t_start = 0.   #Tiempo inicial
t_final = 100.  #Tiempo final
t_delta = (t_final - t_start) / n_steps #Diferencial de tiempo (Paso temporal)
t = linspace(t_start, t_final, n_steps) #Arreglo de diferencial de tiempo

#####################################################################


###### Solución Del Problema Con Odeint ######

r = array([the1_1, ome1_1, the2_1, ome2_1], float)

solu, outodeint = odeint( func,r, t, args = (g, l), full_output=True) 
#solener=odeint(energia,r,t,arg=(g,m,l),full_output=True)
#plot(t, solener)
#xlabel('t (s)')
#ylabel('energia (J)')
#show()

the_10, ome_10, the_20, ome_20 = solu.T 

#####################################################################


###### Datos Para La Animación ######


scene.range = 0.6 #Tamaño de la escena


###### Posiciones en coord. Polares ######

xp = l*sin(the1_1) 
yp = -l*cos(the1_1)
zp = 0.

xs=l*(sin(the1_1)+sin(the2_1))
ys=-l*(cos(the1_1)+cos(the2_1))
zs=0.

####################################################################


sleeptime = 0.0001 #Tiempo de actualización

###### Figuras para la animación ######

prtcl1 = sphere(pos=vector(xp,yp,zp), radius=R, color=color.white) 
prtcls1= sphere(pos=vector(xs,ys,zs), radius=R, color=color.blue)
cyl1= cylinder(pos=vector(0,0,0), radius=l/50, color=color.magenta)
cyl2= cylinder(pos=vector(xp,yp,0), radius=l/50, color=color.magenta)

######################################################################


###### Animación ######

time_i = 0 
t_run = 0

while t_run < t_final: 
    vector1 = vector( l*sin(the_10[time_i]), -l*cos(the_10[time_i]), zp )
    vector2 = vector( l*(sin(the_10[time_i])+sin(the_20[time_i])), -l*(cos(the_10[time_i])+cos(the_20[time_i])), zs )
    
    
    cyl1.axis = vector1
    prtcl1.pos = vector1
    
    cyl2.pos = vector1
    cyl2.axis = vector2
    prtcls1.pos = vector1 + vector2
    
    t_run += t_delta
    sleep(sleeptime)
    time_i += 1

