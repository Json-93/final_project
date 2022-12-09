from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt

j=sqrt(-1)
  
ts=[]
zs=[]
plt.ion()
# create data of complex numbers
for t in np.linspace(0,30,600):
    

    d1 = np.exp(t*j)
    d2 = np.exp(-1*t*j)
    d3=d1+d2

   
    # extract real part using numpy array
    (x1,x2,x3) = (d1.real,d2.real,d3.real)
    (y1,y2,y3) = (d1.imag,d2.imag,d3.imag)

    zs.reverse()
    zs.append(d3)
    zs.reverse()
    ts.append(0.3*t)
    

    # plot the complex numbers
    
    plt.arrow(0,0,x1,y1,head_width=0.05,color='black')
   
    plt.arrow(x1,y1,x2,y2,head_width=0.05,color='black')
    plt.plot(zs,ts,color='orange',linewidth=1.5)
    
    plt.ylabel('Im')
    plt.xlabel('Re')
    plt.xlim(-3.1,3.1)
    plt.ylim(-2.0,3.0)

    plt.title('2cos(t)=exp(iwt)+exp(-iwt)')
    plt.grid(linewidth='0.2')
    plt.show()
  
    plt.pause(0.001)
    plt.clf()
