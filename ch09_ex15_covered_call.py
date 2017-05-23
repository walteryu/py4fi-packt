"""
  Name     : 4375OS_09_15_covered_call.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd.
  Author   : Yuxing Yan
  Date     : 12/26/2013
  Email    : yany@canisius.edu
             paulyxy@hotmail.com
  Update   : Walter Yu on 5/23/17
"""

import numpy as np
from scipy import exp,sqrt,stats
from matplotlib import pyplot as plt

sT = np.arange(0,40,5)
k=15
s0=10
c=2
y0= np.zeros(len(sT))
y1=sT-s0                   # stock only
y2=(abs(sT-k)+sT-k)/2-c    # long a call
y3=y1-y2                   # covered-call

plt.ylim(-10,30)
plt.plot(sT,y1)
plt.plot(sT,y2)
plt.plot(sT,y3,'red')
plt.plot(sT,y0,'b-.')
plt.plot([k,k],[-10,10],'black')

plt.title('Covered call (long one share and short one call)')
plt.xlabel('Stock price')
plt.ylabel('Profit (loss)')
plt.annotate('Stock only (long one share)', xy=(24,15),xytext=(15,20),
             arrowprops=dict(facecolor='blue',shrink=0.01),)
plt.annotate('Long one share, short a call', xy=(10,4), xytext=(9,25),
             arrowprops=dict(facecolor='red',shrink=0.01),)
plt.annotate('Exercise price= '+str(k), xy=(k+0.2,-10+0.5))

plt.show()
