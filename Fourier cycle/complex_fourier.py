from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6.75,9))


j=sqrt(-1)



def fn(t,n):
    m=2*n+1
    return (2/np.pi)*np.exp(j*m*t)/(m*j)



ts=[]
zs=[]


plt.ion()

for t in np.arange(0,30,0.025):
    N=int(t//(2*np.pi)+1)
    N=150
    
    
    xs=[0]
    ys=[0]
    for n in np.arange(0,N):
        
        x1n=fn(t,n).real
        x2n=fn(t,-n-1).real
        y1n=fn(t,n).imag
        y2n=fn(t,-n-1).imag
        xs.append(xs[2*n]+x1n)
        xs.append(xs[2*n+1]+x2n)
        ys.append(ys[2*n]+y1n)
        ys.append(ys[2*n+1]+y2n)

   
    for i in np.arange(0,20):
        rn=((xs[i+1]-xs[i])**2+(ys[i+1]-ys[i])**2)**(1/2)
        x = np.arange(0,2*np.pi+0.1,0.1)
        
        plt.plot(xs[i]+rn*np.cos(x),ys[i]+rn*np.sin(x),color='purple',linewidth=0.1)

    zs.reverse()
    zs.append(xs[-1])
    zs.reverse()
    ts.append(0.4*t)
    
    
    
    plt.plot(zs,ts,color='red',linewidth=0.9,label='square(t)')
    plt.plot(xs,ys,color='gray',linewidth=0.2)
    plt.scatter(xs,ys,color='black',s=0.5)
    
    plt.ylabel('Imaginary')
    plt.xlabel('Real')
    plt.xlim(-1.5,1.5)
    plt.ylim(-1.5,2.5)
    

    plt.title('combination of 300 rotations')
    plt.grid(linewidth='0.2')
    plt.legend()
    
    plt.show()
    
    plt.pause(0.01)
    plt.clf()
    
    

