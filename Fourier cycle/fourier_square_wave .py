import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-4,4,0.001)

def square(x,n):
    s=0
    
    for i in np.arange(0,n):
        s=s+(4/np.pi)*np.sin((2*i+1)*x)/(2*i+1)

    return (x**0)*s


N=301

plt.figure('Fourier series sumation of a square wave')

plt.ion()
for j in np.arange(0,N):

    plt.plot(x,square(x,j))
    plt.title(j)
    plt.ylim(-1.5,1.5)
    plt.show()
    if j<=10:
        plt.pause(0.5)
    elif j<=50:
        plt.pause(0.1)
    
    plt.pause(0.001)

    if j!=N-1:
        plt.clf()

plt.pause(2)
plt.clf()
plt.ioff()
plt.ylim(-1.5,1.5)
plt.plot(x,square(x,50000))
plt.title('n=50000')
plt.show()
