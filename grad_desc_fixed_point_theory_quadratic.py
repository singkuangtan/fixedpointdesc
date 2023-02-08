import matplotlib.pyplot as plt
import numpy as np
import math

'''
def f(x): 
    if x<-10 or x>10:
        return np.inf
    return -1*math.log(1*(x--11))+-1*math.log(1*(-x+11)) +-0.0001*x #x**4 #x**2
    
def g(x): return -1*1/(1*(x--11))+1*1/(1*(-x+11)) -0.0001 #4*x**3 #2*x
'''

def f(x): 
    if x<-100 or x>100:
        return np.inf
    return x**2
    
def g(x): return 2*x

x=np.arange(-100,100,0.1)
y=np.zeros(len(x))
for i in range(0,len(x)):
    print(x[i])
    y[i]=f(x[i])

plt.plot(x,y)
#plt.show()
#exit(1)

y=(x--10)*-10+100
#plt.plot(x,y)
#plt.show()

#y=x^2
#dy/dx=2x

arr=[]

grad_arr=[]

x=-1
y=-1
ini_x=-99.9
for i in range(0,50):
    grad=g(ini_x)
    #print(grad)
    grad_arr.append(grad)
    #exit(1)
    #grad=np.sign(grad)*np.minimum(np.abs(grad),0.03)
    grad=grad/8 #3
    
    if grad==0:
        break
        
    start_x=ini_x
    start_y=f(ini_x)
    
    if i<4:
        #print('a'+str(grad*8))
        #(np.abs(np.arctan(grad*8))/(np.pi/2)*1+0.1)
        
        if grad>=0:
            ini_x=ini_x-1#0.2
        elif grad<0:
            ini_x=ini_x+1#0.2
    if i>=4:
        #print('a'+str(grad*8))
        #exit(1)
        if grad>=0:
            ini_x=ini_x-0.01#0.2
        elif grad<0:
            ini_x=ini_x+0.01#0.2
    
    ini_y=f(ini_x)
    
    
    
    a=[]
    for j in range(0,100):
        print(j)
        if j!=0 and ini_y<(f(ini_x)):
            ini_x=pre_ini_x
            break;
            
        if len(a)>0:
            plt.plot(a,b,color='g')
            
        if j>=3 and ((arr[-1]-arr[-2])>(arr[-2]-arr[-3])):
            ini_x=pre_ini_x
            break;
        
        
        
        ini_y=f(ini_x)
        
        if x!=-1 and y>f(x):#j!=0:
            a=np.array([ini_x,x])
            b=np.array([ini_y,y])
            plt.plot(a,b,color='g')
            #plt.arrow(a[0],b[1],a[1]-a[0],-(b[1]-b[0]),width=0.1,length_includes_head=True,head_length=(0.1*np.sqrt((a[1]-a[0])**2+(b[1]-b[0])**2)),head_width=5)
        
        y=f(ini_x)
        x=start_x+(y-start_y)/grad
        
        a=np.array([ini_x,x])
        b=np.array([y,y])
        #plt.plot(a,b,color='g')
        #plt.arrow(a[0],b[1],a[1]-a[0],-(b[1]-b[0]),width=0.01,length_includes_head=True,head_length=(0.1*np.sqrt((a[1]-a[0])**2+(b[1]-b[0])**2)),head_width=0.1)
        
        if j==0:
            first_x=x
            first_y=y
        last_x=x
        last_y=y
        
        #print(y)
        print(x)
        #plt.scatter(x,y)
        pre_ini_x=ini_x
        ini_x=x
        #print('x='+str(ini_x))
        print('y='+str(ini_y))
        arr.append(y)
        
    plt.plot([first_x,last_x],[first_y,last_y],color='y')
plt.show()

plt.plot(arr)
plt.show()

plt.plot(np.log(arr-np.min(arr)+0.01))
plt.show()

plt.plot(grad_arr)
plt.show()

#np.save('ffgd.npy',arr)