# -*- coding: utf8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
from scipy.optimize import curve_fit


fig = plt.figure()


def onclick(event):
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, event.xdata, event.ydata))
 
fig.canvas.mpl_connect('button_press_event', onclick)
 

def func(x, a, b, c):
    return a * np.exp(-b * x) + c


def func_quat(x, a, b, c):
    return a * np.power(x, 2) - b * x + c


def func_cubic(x, a, b, c):
    return a * np.power(x, 3) - b * x ** 2 + c*x + 1

xdata = np.linspace(-0, 4, 50)
y = func_quat(xdata, 2.5, 1.3, 0.5)
y_noise = 2 * np.random.normal(size=xdata.size)
ydata = y + y_noise
plt.plot(xdata, ydata, 'b-', label='data')

# 按照二次曲线拟合, popt 是方程 f 的系数， pcov是预估的协方差
popt, pcov = curve_fit(func_quat, xdata, ydata)
plt.plot(xdata, func_quat(xdata, *popt), 'r-', label='fit')

# 
popt, pcov = curve_fit(func, xdata, ydata, bounds=(0, [3., 2., 1.]))
#plt.plot(xdata, func(xdata, *popt), 'g--', label='fit-with-bounds')


plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


"""
https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html



"""
