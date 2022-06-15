# IMPORT NECESSARY MODULES------------------------------------------------------------------------->
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Opening  and assigning each file to a variable name
f_earth = open('earth.txt', 'r')
f_mars = open('mars.txt', 'r')
f_jupiter = open('jupiter.txt', 'r')
f_saturn = open('saturn.txt', 'r')
f_uranus = open('uranus.txt', 'r')
f_voyager2 = open('voyager2.txt', 'r')

# DATA EXTRACTION STARTS HERE---------------------------------------------------------------------->

# Bodies' coordinates extraction
def body(s):
    x_axis, y_axis = [], []
    data = s.readlines()
    if s == f_voyager2:
        d = data[50:32721:4]
    else:
        d = data[27:32701:4]
    for n in d:
        xyz = n.split()
        xyz = [xyz[0]+xyz[1]+xyz[2], xyz[3]+xyz[4]+xyz[5]]
        x = xyz[0]
        x = x.strip('X').strip('Y').strip('=')
        y = xyz[1]
        y = y.strip('=').strip('Z').strip('Y').strip('=')
        y = y[0:22] #remove any unwanted characters tagging along with the data
        xy = [x,y]
        x_axis.append(float(xy[0]))
        y_axis.append(float(xy[1]))
    return x_axis, y_axis
# DATA EXTRACTION ENDS HERE------------------------------------------------------------------------>

#--------Calling User-defined function to read and assign the approptiate variable name to each file
x_earth, y_earth = body(f_earth)
x_mars, y_mars = body(f_mars)
x_jupiter, y_jupiter = body(f_jupiter)
x_saturn, y_saturn = body(f_saturn)
x_uranus, y_uranus = body(f_uranus)
x_coordinate, y_coordinate = body(f_voyager2)

# PLOTING OF GRAPH WITH THE EXTRACTED DATA STARTS HERE--------------------------------------------->
# Program for graphing data
fig, ax = plt.subplots()
ax.set_facecolor ('#040406')
plt.title('Voyager 2 Spacecraft trajectory 1977-Aug-20 to 1999-Oct-01')
plt.xlabel('X-component of position vector (au)')
plt.ylabel('Y-component of position vector (au)')
ax.set_xlim(min(x_coordinate)-10, max(x_coordinate)+5)
ax.set_ylim(min(y_coordinate)-10, max(y_coordinate)+10)
line, = ax.plot( 0, 0, ls='--', lw=1.5)
lines, = ax.plot( 0, 0,marker='X', label='Voyager2')
mars_path, = ax.plot(0, 0)
earth_path, = ax.plot(0, 0)
jupiter_path, = ax.plot(0, 0)
saturn_path, = ax.plot(0, 0)
uranus_path, = ax.plot(0, 0)
mars,= ax.plot(0,0,'o', label='Mars')
earth,= ax.plot(0,0,'o', label='Earth')
jupiter, = ax.plot(0,0,'o', label='Jupiter')
saturn,= ax.plot(0,0,'o', label='Saturn')
uranus,= ax.plot(0,0,'o', label='Uranus')
plt.legend()
# PLOTING OF GRAPH WITH THE EXTRACTED DATA ENDS HERE----------------------------------------------->

# ANIMATION OF PLOTED CORDINATES STARTS HERE------------------------------------------------------->
# function for animation is intiated
x, y=[],[]
def animation_frame(i):
    while i < len(x_coordinate)/10:
        x.append(x_coordinate[int(i*10)])#---------------------X-coordinate of Voyager2's trajectory
        y.append(y_coordinate[int(i*10)])#---------------------Y-coordinate of Voyager2's trajectory
        #---------------------------------the planets coordinate at each point of X and Y trajectory
        j, u = x_coordinate[int(i*10)], y_coordinate[int(i*10)]
        c, d = x_earth[int(i*10)], y_earth[int(i*10)]#------------------X and Y trajectory for Earth
        e, f = x_mars[int(i*10)], y_mars[int(i*10)]#--  -----------------X and Y trajectory for Mars
        a, b = x_jupiter[int(i*10)], y_jupiter[int(i*10)]#------------X and Y trajectory for Jupiter
        g, h = x_saturn[int(i*10)], y_saturn[int(i*10)]#---------------X and Y trajectory for Saturn
        k, m = x_uranus[int(i*10)], y_uranus[int(i*10)]#---------------X and Y trajectory for Uranus
        i = len(x_coordinate)
        line.set_xdata(x)
        line.set_ydata(y)
        lines.set_xdata(j)
        lines.set_ydata(u)
        jupiter.set_xdata(a)
        jupiter.set_ydata(b)
        earth.set_xdata(c)
        earth.set_ydata(d)
        mars.set_xdata(e)
        mars.set_ydata(f)
        saturn.set_xdata(g)
        saturn.set_ydata(h)
        uranus.set_xdata(k)
        uranus.set_ydata(m)
    # ---------------------------------------------------Setting the graph trajectory of the planets
        jupiter_path.set_xdata(x_jupiter)
        jupiter_path.set_ydata(y_jupiter)
        earth_path.set_xdata(x_earth)
        earth_path.set_ydata(y_earth)
        mars_path.set_xdata(x_mars)
        mars_path.set_ydata(y_mars)
        saturn_path.set_xdata(x_saturn)
        saturn_path.set_ydata(y_saturn)
        uranus_path.set_xdata(x_uranus)
        uranus_path.set_ydata(y_uranus)
        return  line, lines, jupiter, earth, mars, saturn, uranus, jupiter_path, earth_path, mars_path
# ANIMATION OF PLOTED CORDINATES ENDS HERE------------------------------------------------------->

#Call Animation function to run the Create and the Animation and show the output
animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, len(x_coordinate), 1), interval=100)
plt.show()
