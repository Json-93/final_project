from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(9,9))


j=sqrt(-1)
pi=np.pi
exp=np.exp


dt=0.0001 # lowering the dt will gives more precise shape of the contour

ts1=np.arange(0,pi/2,dt)
ts2=np.arange(pi/2,pi,dt)
ts3=np.arange(pi,1.5*pi,dt)          
ts4=np.arange(1.5*pi,2*pi,dt)

#different shape of contour on complex plane

'''fs1=(-j/2+1*ts1+j*ts1+j/pi*ts1).tolist()
fs2=((pi+pi*j)/2+pi/4*(exp(2*j*ts1)-1)).tolist()             #define the heart contour on the complex plane
fs3=(j*pi/2+pi/4*(exp(2*j*ts1)-1)).tolist()
fs4=((-1*pi+j*pi)/2+(1-j-j/pi)*ts1).tolist()'''

fs1=((2+j)*ts1).tolist()
fs2=((2+j)*pi/2+(-1-j)*ts1).tolist()               #define the arrow contour on the complex plane
fs3=((pi/2)+(1-j)*ts1).tolist()
fs4=((2-j)*pi/2+(-2+j)*ts1).tolist()

ts=np.array(ts1.tolist()+ts2.tolist()+ts3.tolist()+ts4.tolist())   
fs=np.array(fs1+fs2+fs3+fs4) 

def cn(n):     #definition of Fourier trick
    F=fs*exp(-j*n*ts)
    s=0
    for i in np.arange(0,len(F)):
        s=s+F[i]*dt
    return s                          

NMAX=200 #maximum number of frequencies combination

cnplus=[]
cnmin=[]
for m in range(0,NMAX):
    cnplus.append(cn(m))
    cnmin.append(cn(-m))

cnmin=cnmin[1:]
cnmin.reverse()
cns=cnplus+cnmin     #use a list cns[n] to store the  cn(n) , calculate the coefficients before the animation
 


def fn(t,n):
    
    return cns[n]*np.exp(j*n*t)*2/pi**2/2    # number n term in the fourier series


#Animation start 

X=[]
Y=[]


plt.ion()
for t in np.arange(0,90,0.03):
    N=5*int(t//(2*np.pi)+1)     #number of frequencies combination
    N=99
                
    if N>6 :    #number of circles
        M=7     #the loop is needed because the number of circles must less then that of the series
    else:
        M=N
         
    
    if t%(2*np.pi)<0.04:    #clear the contour when each periods finish 
        X=[]
        Y=[]



    xs=[0]
    ys=[0]
    for i in range(1,N+1):
        
        x1n=fn(t,i).real
        x2n=fn(t,-i).real
        y1n=fn(t,i).imag
        y2n=fn(t,-i).imag
        xs.append(xs[-1]+x1n)
        xs.append(xs[-1]+x2n)
        ys.append(ys[-1]+y1n)
        ys.append(ys[-1]+y2n)
    
    

   
    for i in np.arange(0,2*M):
        rn=((xs[i+1]-xs[i])**2+(ys[i+1]-ys[i])**2)**(1/2)
        x = np.arange(0,2*np.pi+0.1,0.1)
        
        plt.plot(xs[i]+rn*np.cos(x),ys[i]+rn*np.sin(x),color='purple',linewidth=0.1)

    
    X.append(xs[-1])
    Y.append(ys[-1])
    
    
    
    #plotting the setting contour on the complex plane
    
    plt.plot(X,Y,color='brown',linewidth=0.9,label='square(t)')
    plt.plot(xs,ys,color='gray',linewidth=0.2)
    plt.scatter(xs,ys,color='black',s=0.5)
    
    plt.ylabel('Imaginary')
    plt.xlabel('Real')
    plt.xlim(-1.5,1.5)
    plt.ylim(-1.5,1.5)
    

    plt.title('First '+str(N)+' orders of Fourier series')
    plt.grid(linewidth='0.2')
    plt.legend()
    
    plt.show()
    
    plt.pause(0.005)
    plt.clf()


    
