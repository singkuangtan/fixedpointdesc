import matplotlib.pyplot as plt
import numpy as np

arr1=np.load('ffgd.npy')
arr2=np.load('new.npy')

plt.plot(arr1,label='Gradient descent using fixed point theorem')
plt.plot(arr2,label='Newton method')
plt.legend()
plt.show()