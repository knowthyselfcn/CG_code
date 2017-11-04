# -*- coding: utf8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.interpolate

xSize = 10
fig = plt.figure()

def onclick(event):
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, event.xdata, event.ydata))

def onkey(event):
    global xSize
    if(event.key == "up"):
        xSize  = xSize +1
    elif (event.key == "down"):
        xSize = xSize - 1
    testInterpolate1()


fig.canvas.mpl_connect('button_press_event', onclick)
fig.canvas.mpl_connect('key_press_event', onkey)

def func_cubic(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c*x + d

def genData():
    xdata = np.linspace(-4, 4, xSize)
    y = func_cubic(xdata, 1, 1, 1, 1)
    y_noise = 2 * np.random.normal(size=xdata.size)
    ydata = y + y_noise
    return xdata, ydata

def testInterpolate1():
    global xSize
    plt.clf()
    xdata, ydata = genData()
    plt.plot(xdata, ydata, 'b.', label='data,  size=' + str(xSize))

    # 按照三次曲线拟合, popt 是方程 f 的系数， pcov是预估的协方差
    popt_cubic, pcov_cubic = curve_fit(func_cubic, xdata, ydata)
    print(xdata, ydata)
    plt.plot(xdata, func_cubic(xdata, *popt_cubic), 'g-', label='cubic fit')

    lagrangePoly = scipy.interpolate.lagrange(xdata, ydata)
    newXData = np.delete(np.add(-0.1, xdata), xdata.size - 1)
    newYData = np.add(3, lagrangePoly(newXData))
    plt.plot(newXData, newYData, 'r--.', label='lagrangePoly(x)+3')

    f = scipy.interpolate.interp1d(xdata, ydata)
    newXData = np.delete( np.add(0.1, xdata), xdata.size-1)
    newYData = np.add(-3, f(newXData))
    plt.plot(newXData, newYData, 'r:', label='interp1d(x)-3')

    plt.xlabel('x'); plt.ylabel('y'); plt.legend()
    plt.show()

testInterpolate1()


