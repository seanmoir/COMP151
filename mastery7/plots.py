import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10,0.1)

y = np.sin(x)
plt.plot(x, y)
plt.show()

y = 3 * np.sin(x*x) - 2 * np.cos(x*x*x)
plt.plot(x, y)
plt.show()

y = pow(2, ((-x)*2)/2)
plt.plot(x, y)
plt.show()

t = np.arange(0,2*np.pi,0.01)
x = t * np.cos(t)
y = t * np.sin(t)
plt.plot(x,y)
# the following line makes sure the aspect ratio is 1:1
plt.gca().set_aspect('equal')
plt.show()

t = np.arange(0,2*np.pi,0.01)
x = pow(np.e, 0.3*t) * np.cos(t)
y = pow(np.e, 0.3*t) * np.sin(t)
plt.plot(x,y)
# the following line makes sure the aspect ratio is 1:1
plt.gca().set_aspect('equal')
plt.show()

t = np.arange(0,2*np.pi,0.01)
x = t - np.sin(t)
y = 1 - np.cos(t)
plt.plot(x,y)
# the following line makes sure the aspect ratio is 1:1
plt.gca().set_aspect('equal')
plt.show()

t = np.arange(0,2*np.pi,0.01)
a = 4
b = 1
x = (a - b) * np.cos(t) + b * np.cos(((a - b)/b) * t)
y = (a - b) * np.sin(t) - b * np.sin(((a - b)/b) * t)
plt.plot(x,y)
# the following line makes sure the aspect ratio is 1:1
plt.gca().set_aspect('equal')
plt.show()

t = np.arange(0,2*np.pi,0.01)
x = np.cos(t)
y = np.sin(t)
r = [[np.cos(np.pi/4), -np.sin(np.pi/4)], [np.sin(np.pi/4), np.cos(np.pi/4)]]
pts = np.vstack((x, y))
out =  np.dot(r, np.dot([[1, 0], [0, 3]], pts))
plt.plot(out[0], out[1])
# the following line makes sure the aspect ratio is 1:1
plt.gca().set_aspect('equal')
plt.show()

t = np.arange(0,2*np.pi,0.01)
x = t * np.cos(t)
y = t * np.sin(t)
r = [[np.cos(np.pi/4), -np.sin(np.pi/4)], [np.sin(np.pi/4), np.cos(np.pi/4)]]
pts = np.vstack((x, y))
out =  np.dot(r, np.dot([[1, 0], [0, 3]], pts))
plt.plot(out[0], out[1])
# the following line makes sure the aspect ratio is 1:1
plt.gca().set_aspect('equal')
plt.show()

t = np.arange(0,2*np.pi,0.01)
x = t - np.sin(t)
y = 1 - np.cos(t)
r = [[np.cos(np.pi/4), -np.sin(np.pi/4)], [np.sin(np.pi/4), np.cos(np.pi/4)]]
pts = np.vstack((x, y))
out =  np.dot(r, np.dot([[1, 0], [0, 3]], pts))
plt.plot(out[0], out[1])
# the following line makes sure the aspect ratio is 1:1
plt.gca().set_aspect('equal')
plt.show()

a = [[1, 1], [1, 1]]
b = [[1, 2, 0, 4, 5, 10], [5, 3, 2, 8, 9, 1]]

out = np.dot(a, b)
plt.scatter(out[0], out[1])
plt.show()