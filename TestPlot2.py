import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# DataAll1D = np.loadtxt("data3d.csv", delimiter=",")

# # create 2d x,y grid (both X and Y will be 2d)
# X, Y = np.meshgrid(DataAll1D[:,0], DataAll1D[:,1])

# # repeat Z to make it a 2d grid
# Z = np.tile(DataAll1D[:,2], (len(DataAll1D[:,2]), 1))

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# ax.plot_surface(X, Y, Z, cmap='ocean')

fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')
ax1.axes.set_xlim3d(left=0, right=1000) 
ax1.axes.set_ylim3d(bottom=0, top=1000) 


xyz = np.genfromtxt('data3dv2.csv',delimiter=',')

x= np.array(xyz[:,0])
y=np.array(xyz[:,1])
z=np.array(xyz[:,2])

#xyz = np.array([],[],[])


ax1.scatter(x,y,z)
plt.show()

plt.show()