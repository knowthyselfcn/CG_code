import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import numpy as np


x = np.linspace(-3, 3, 50)
y = np.exp(-x**2) + 0.1 * np.random.randn(50)
plt.plot(x, y, 'ro', ms=5)

spl = UnivariateSpline(x, y)
xs = np.linspace(-3, 3, 1000)
plt.plot(xs, spl(xs), 'g', lw=3)

spl.set_smoothing_factor(0.3)
plt.plot(xs, spl(xs), 'b', lw=3)
plt.show()


"""
https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.UnivariateSpline.html

"""
