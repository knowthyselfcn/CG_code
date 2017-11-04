import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import numpy as np


x = np.linspace(-3, 3, 50)
#y = np.exp(-x**2) + 0.1 * np.random.randn(50)
y = np.sin(x) + np.random.randn(1)
plt.plot(x, y, 'ro', ms=5)

spl = UnivariateSpline(x, y)
xs = np.linspace(-3, 3, 1000)

plt.plot(xs, spl(xs), 'g-', lw=3, label='no-smooth')

spl.set_smoothing_factor(0.1)
plt.plot(xs, spl(xs), 'b-', lw=3, label='smooth_factor=0.1')

plt.xlabel('x'); plt.ylabel('y'); plt.legend()
plt.show()


