import matplotlib.pyplot as plt
import numpy as np
import math

'''
def f(x): 
    if x<-10 or x>10:
        return np.inf
    return -0.5*math.log(1*(x--11))+-0.5*math.log(1*(-x+11)) +-0.1*x #x**4 #x**2
    
def g(x): return -0.5*1/(1*(x--11))+0.5*1/(1*(-x+11)) -0.1 #4*x**3 #2*x

def h(x): return 0.5*1/((1*(x--11))**2)+0.5*1/((1*(-x+11))**2)  #4*x**3 #2*x
'''

def f(x): 
    if x<-100 or x>100:
        return np.inf
    return 1/(x--101)+1/(-x+101) +-0.01*x #x**4 #x**2
    
def g(x): 
    if x<-100: 
        x=-100
    if x>100:
        x=100
    return -1/((x--101)**2)+1/((-x+101)**2) -0.01 #4*x**3 #2*x

def h(x): 
    if x<-100: 
        x=-100
    if x>100:
        x=100
    return 2/((x--101)**3)+2/((-x+101)**3) #4*x**3 #2*x

x=np.arange(-100,100,0.1)
y=np.zeros(len(x))
for i in range(0,len(x)):
    #print(x[i])
    y[i]=g(x[i])

plt.plot(x,y)
plt.show()
#exit(1)

y=(x--10)*-10+100
#plt.plot(x,y)
#plt.show()

#y=x^2
#dy/dx=2x

arr=[]

x=-1
y=-1
ini_x=-99.9

y=f(ini_x)
arr.append(y)
for i in range(0,50):
    
    ini_x=ini_x-g(ini_x)/h(ini_x)
    
    if ini_x<-100: 
        ini_x=-100
    if ini_x>100:
        ini_x=100
        
    y=f(ini_x)
    print(y)
    arr.append(y)

plt.figure()
plt.plot(arr)
plt.show()

#np.save('new.npy',arr)

'''
    grad=g(ini_x)
    grad=grad/3 #3
    
    if grad==0:
        break
        
    start_x=ini_x
    start_y=f(ini_x)
    
    if grad>=0:
        ini_x=ini_x-0.01
    elif grad<0:
        ini_x=ini_x+0.01
    
    ini_y=f(ini_x)
    
    
    
    
    for j in range(0,100):
        print(j)
        if j!=0 and ini_y<(f(ini_x)):
            ini_x=pre_ini_x
            break;
        if j>=3 and ((arr[-1]-arr[-2])>(arr[-2]-arr[-3])):
            ini_x=pre_ini_x
            break;
            
        ini_y=f(ini_x)
        
        if j!=0:
            a=np.array([ini_x,x])
            b=np.array([ini_y,y])
            plt.plot(a,b)
        
        y=f(ini_x)
        x=start_x+(y-start_y)/grad
        
        a=np.array([ini_x,x])
        b=np.array([y,y])
        plt.plot(a,b)
        
        if j==0:
            first_x=x
            first_y=y
        last_x=x
        last_y=y
        
        #print(y)
        print(x)
        plt.scatter(x,y)
        pre_ini_x=ini_x
        ini_x=x
        #print('x='+str(ini_x))
        print('y='+str(ini_y))
        arr.append(y)
        
    plt.plot([first_x,last_x],[first_y,last_y])
plt.show()

plt.plot(arr)
plt.show()

plt.plot(np.log(arr-np.min(arr)+0.01))
plt.show()
'''