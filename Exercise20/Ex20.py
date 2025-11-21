import numpy as np
import matplotlib.pyplot as plt

# e^(sqrt(x)) over [0, 6]
x1 = np.linspace(0, 6, 400)
y1 = np.exp(np.sqrt(x1))

# log(|sin(x)|) over [0.1, 6]
x2 = np.linspace(0.1, 6, 400)
y2 = np.log(np.abs(np.sin(x2)))

# arctan(x^3) over [-6, 6]
x3 = np.linspace(-6, 6, 400)
y3 = np.arctan(x3**3)

# Modified Bessel function
x4 = np.linspace(0, 6, 400)
y4 = np.i0(x4)


plt.figure(figsize=(10, 8))

# e^(sqrt(x)) over [0, 6]
plt.subplot(2, 2, 1)
plt.plot(x1, y1, 'r')  # Red color
plt.title(r'$e^{\sqrt{x}}$ over [0, 6]')
plt.xlabel('x')
plt.ylabel(r'$e^{\sqrt{x}}$')
plt.grid(True)

# log(|sin(x)|) over [0.1, 6]
plt.subplot(2, 2, 2)
plt.plot(x2, y2, 'g')  # Green color
plt.title(r'$\log(|\sin(x)|)$ over [0.1, 6]')
plt.xlabel('x')
plt.ylabel(r'$\log(|\sin(x)|)$')
plt.grid(True)

# arctan(x^3) over [-6, 6]
plt.subplot(2, 2, 3)
plt.plot(x3, y3, 'b')  # Blue color
plt.title(r'$\arctan(x^3)$ over [-6, 6]')
plt.xlabel('x')
plt.ylabel(r'$\arctan(x^3)$')
plt.grid(True)

# Modified Bessel function 
plt.subplot(2, 2, 4)
plt.plot(x4, y4, 'm')  # Magenta color
plt.title(r'Modified Bessel function of the first kind, $J_0(x)$')
plt.xlabel('x')
plt.ylabel(r'$J_0(x)$')
plt.grid(True)


plt.tight_layout()
plt.show()
