# -*- coding: utf8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.interpolate

xSize = 10
xdata = np.array( [0.1, 5] )
ydata = np.array( [0.1, 1.0] )

fig = plt.figure()

def onclick(event):
    global xSize, xdata, ydata
    xdata = np.sort(np.append(xdata, event.xdata))
    index = np.where(xdata == event.xdata)[0][0]
    ydata = np.insert(ydata, index, event.ydata)
    show()

def onkey(event):
    global xSize, xdata, ydata
    if(event.key == "up"):
        xSize  = xSize +1
    elif (event.key == "down"):
        xSize = xSize - 1
    show()


fig.canvas.mpl_connect('button_press_event', onclick)
fig.canvas.mpl_connect('key_press_event', onkey)

def func_quat(x, a, b, c):
    return a * x ** 2 + b * x + c

def show():
    global xSize, xdata, ydata
    plt.clf()
    A = np.vstack([xdata, np.ones(len(xdata))]).T
    m, c = np.linalg.lstsq(A, ydata)[0]
    plt.plot(xdata, ydata, 'b.', label='data')
    plt.plot(xdata, np.add(np.multiply(xdata, m), c), 'r', label='Fitted line')

    if( xdata.size > 3):
        popt, pcov = curve_fit(func_quat, xdata, ydata)
        plt.plot(xdata, func_quat(xdata, *popt), 'g-', label='quad fit')

    plt.xlabel('x'); plt.ylabel('y'); plt.legend()
    plt.show()

show()


