import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from tensorflow_core import sigmoid

mpl.rcParams['axes.unicode_minus'] = False
fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(111)
x = np.linspace(-6,6)
y = sigmoid(x)

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.set_xticks([-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6])
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.set_yticks([-1,-0.5,0.5,1])

plt.plot(x,y,label = 'Sigmoid',linestyle='-',color='blue')
plt.legend(['Sigmoid'])
plt.show()
# plt.savefig('softmax.png')