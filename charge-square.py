import numpy as np
import matplotlib.pyplot as plt

# Physical constants
epsilon0 = 8.854187817e-12  # Vacuum permittivity (F/m)

# Charge sheet parameters
L = 1.0                     # Length of the square sheet (m)
sigma = 1e-6                # Surface charge density (C/m^2)

# Discretize the sheet into small charge elements
N = 100                     # Number of divisions per side (increase for higher accuracy)
xq = np.linspace(-L/2, L/2, N)
yq = np.linspace(-L/2, L/2, N)
dx = xq[1] - xq[0]
dy = yq[1] - yq[0]
Xq, Yq = np.meshgrid(xq, yq)

# Evaluation grid in the XY plane
M = 100                     # Grid resolution for plotting
extent = 2 * L              # Plot region extends from -L to +L in both x and y
x = np.linspace(-extent/2, extent/2, M)
y = np.linspace(-extent/2, extent/2, M)
X, Y = np.meshgrid(x, y)
V = np.zeros_like(X)

# Pre-factor for potential calculation
prefactor = sigma * dx * dy / (4 * np.pi * epsilon0)

# Numerically compute the potential at each grid point
for i in range(M):
    for j in range(M):
        Rx = X[i, j] - Xq
        Ry = Y[i, j] - Yq
        R = np.sqrt(Rx**2 + Ry**2)
        # Avoid singularity at R=0
        R[R == 0] = np.finfo(float).eps
        V[i, j] = prefactor * np.sum(1.0 / R)

# Plot equipotential lines
levels = np.linspace(np.min(V), np.max(V), 25)
plt.figure(figsize=(6, 5))
cp = plt.contour(X, Y, V, levels=levels)
plt.clabel(cp, inline=True, fontsize=8)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Equipotential Lines of a Finite Square Charged Sheet')
plt.axis('equal')
plt.tight_layout()
plt.show()
