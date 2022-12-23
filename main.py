
import numpy as np
import matplotlib.pyplot as plt

#te1 represents the loaded users on the server, and te2 represents the leaves from the server,
#in the form of 2 element lists, the first element representing the time it passed since
#the start of the game until the leave/load, and the second element is the flag for leave/load, 1 for load, 0 for leave.
te1=[[0.4,1],[1.6,1],[2.1,1], [2.8,1], [3,1], [3.6,1], [3.8,1],[5.2,1]]
te2=[[2.4,0],[3.1,0],[3.3,0],[4.4,0],[8.1,0],[8.7,0],[8.9,0],[9.4,0]]

for i in te2:
    te1.append(i)

n=8
for i in range(2*n-1):
    x=range(i+1,2*n)
    for j in x:
        if te1[i][0]>te1[j][0]:

            aux=te1[i][0]
            te1[i][0]=te1[j][0]
            te1[j][0]=aux

            aux=te1[i][1]
            te1[i][1]=te1[j][1]
            te1[j][1]=aux

y=-1
graphx=[]
graphy=[]

range1=range(0,2*n-1)
for i in range1:
    if te1[i][1]==0:
        y=y-1
    else:
        y=y+1

    x=np.arange(te1[i][0],te1[i+1][0],0.01)
    for j in x:
        graphy.append(y)
    for j in x:
        graphx.append(j)


plt.plot(graphx, graphy)
plt.show()







