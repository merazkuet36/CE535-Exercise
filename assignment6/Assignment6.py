import numpy as np
import matplotlib.pyplot as plt

u0 = 2.0
udot0 = 1.5
m = 3.0
k = 15.0

# TODO: generate a vector for time t
t = np.linspace(0, 3*np.pi, 500)

# TODO: compute natural circular frequency
wn = np.sqrt(k/m)

# TODO: compute displacement vector
u = u0 * np.cos(wn * t) + (udot0 / wn) * np.sin(wn * t)

# TODO: plot u vs. t
plt.plot(t, u)

# TODO: set x limits to [0, 3pi]
plt.xlim(0, 3*np.pi)

# TODO: set x label and y label with units
plt.xlabel("t [s]")
plt.ylabel("u(t) [m]")

u0 = 2.0
udot0 = 1.5
m = 3.0
k = 15.0
zeta = 0.02

# TODO: generate a vector for time t
t = np.linspace(0, 3*np.pi, 500)

# TODO: compute natural and damped circular frequency
wn = np.sqrt(k/m)
wD = wn * np.sqrt(1 - zeta**2)

# TODO: compute displacement vector
u = np.exp(-zeta * wn * t) * (
    u0 * np.cos(wD * t) +
    (udot0 + zeta * wn * u0) / wD * np.sin(wD * t)
)

# TODO: compute rho
rho = np.sqrt(
    u0**2 + ((udot0 + zeta * wn * u0) / wD)**2
)

# TODO: compute envelope function f1 and f2
f1 = rho * np.exp(-zeta * wn * t)
f2 = -rho * np.exp(-zeta * wn * t)

# TODO: plot u, f1, f2 vs. t with specified styles
plt.plot(t, u, '-', label="u(t)")
plt.plot(t, f1, '--', label="envelope +")
plt.plot(t, f2, '--', label="envelope -")

# TODO: set legends for three lines
plt.legend()

# TODO: set x label and y label with units
plt.xlabel("t [s]")
plt.ylabel("u [m]")



u0 = 2.0
udot0 = 1.5
m = 3.0
k = 15.0

wn = np.sqrt(k/m)
t = np.linspace(0, 3*np.pi, 500)

zetas = [0.02, 0.05, 0.1, 0.2]

plt.figure(figsize=(10, 8))

for i, zeta in enumerate(zetas, start=1):
    wD = wn * np.sqrt(1 - zeta**2)
    u = np.exp(-zeta * wn * t) * (
        u0 * np.cos(wD * t) +
        (udot0 + zeta * wn * u0) / wD * np.sin(wD * t)
    )

    plt.subplot(2, 2, i)
    plt.plot(t, u)
    plt.title(r"$\zeta = {:.2f}$".format(zeta))
    plt.xlabel("t [s]")
    plt.ylabel("u(t) [m]")
    plt.grid(True)

plt.tight_layout()
plt.show()
