import numpy as np
import matplotlib.pyplot as plt


plt.figure()
x = np.linspace(0.1, 2 * np.pi, 100)  # range [0.1, 2*pi]
y1 = np.cos(x)
y2 = np.log(x)
plt.plot(x, y1, label=r'$\cos(x)$')
plt.plot(x, y2, label=r'$\log(x)$')
plt.fill_between(x, y1, y2, color='lightgrey', alpha=0.5)  
plt.xlabel('x')
plt.ylabel('y')
plt.title('Filled between Cos(x) and Log(x)')
plt.legend()
plt.show()


n = 1024
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
sizes = (y - min(y)) / (max(y) - min(y)) * 60 
plt.figure()
plt.scatter(x, y, s=sizes, alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Random Points with Normal Distribution')
plt.show()

# Bar plot
n = 12
x = np.arange(1, n + 1)
y = (1 - x / float(n)) * np.random.uniform(0.5, 1.0, n)
plt.figure()
plt.bar(x, y, facecolor='#9999ff', edgecolor='white')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Bar Plot')
plt.show()

# 3D plot
# Initial conditions for projectile
x0, y0, z0 = 1, 2, 0
vx0, vy0, vz0 = 1, -1.5, 5.0
g = -9.81  # gravity
t = np.linspace(0, 1.02, 100)  # time from 0 to 1.02 sec

# Equations of motion
x = x0 + vx0 * t
y = y0 + vy0 * t
z = vz0 * t + 0.5 * g * t**2


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='Projectile path')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Projectile Motion')
plt.legend()
plt.show()


plt.xlim([x[0], x[-1]])
plt.ylim([y[0], y[-1]])
print("Launch Location: ", (x[0], y[0]))
print("Falling Location: ", (x[-1], y[-1]))
