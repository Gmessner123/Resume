# Import Python packages necessary for this script
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate a beautiful sinusoidal curve
x = np.linspace(0, 2*np.pi, 500)
y = np.sin(2 * np.sin(2 * np.sin(2 * x)))
plt.plot(x, y)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()
