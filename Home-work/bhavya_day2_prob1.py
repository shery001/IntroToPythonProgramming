import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
f = open('/home/bhavya/Documents/AA/PythonProgramming/Day_2/data/autofahrt.txt','r') 
time = []
a_x = []
a_y = []
for line in f:
    columns = line.split(' ')
    if len(columns) >= 2:
        time.append(columns[0])
        a_x.append(columns[1])
        a_y.append(columns[2])
        

time.remove('Time')
time.remove('s')
#print time
a_x.remove('Gx')
a_x.remove('m/s^2')
#print a_x
a_y.remove('Gy')
a_y.remove('m/s^2')
#print a_y
print len(a_x)

a = []
for i in range(len(a_x)):
    #print i
    fl_ax = float(a_x[i])
    fl_ay = float(a_y[i])
    #print np.square(fl_ax)
    #print np.square(fl_ay)
    a.append(np.sqrt(np.square(fl_ax)+ np.square(fl_ay)))
    
#print a  

plt.plot(time, a)


#accelatation is the second derivative, with respect to time, of accelartion. 
#Here i would explain the total projected  forward distance as the equal to the total forwrd distance in every timestep
#which can be calculated by the accelaration in everytime step.

dist_t = []
for i in range(len(time)-1):
    t1 = float(time[i])
    t2 = float(time[i+1])
    delta_t = t2-t1
    #print delta_t
    #print a[i]
    dist_t.append(a[i]*(0.5)*(delta_t**2))       #distance travel in every time step
    
    
#print dist_t

#Total distance traveled.

total_dist = 0

for i in range(len(dist_t)):
    total_dist += dist_t[i] 
    
    
print total_dist
    

