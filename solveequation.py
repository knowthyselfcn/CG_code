# -*- coding: utf8 -*-


import scipy
import scipy.optimize


def f_d5(x):
    return x ** 5 + 2 * x ** 4 + 3 * x ** 3 + 4 * x ** 2 + 5 * x + 6


def f_d6(x):
    return x**6 + x ** 5 + 2 * x ** 4 + 3 * x ** 3 + 4 * x ** 2 + 5 * x + 6


def f_d7(x):
    return x**7 + x**6 + x ** 5 + 2 * x ** 4 + 3 * x ** 3 + 4 * x ** 2 + 5 * x + 6

root, ro = scipy.optimize.bisect(f_d5, -10, 10, xtol=2e-30, rtol=2e-15, maxiter=1000, full_output=True)
print(root, ro)

root,ro = scipy.optimize.ridder(f_d5, -10, 10, xtol=2e-30, rtol=2e-15, maxiter=1000, full_output=True)
print(root, ro)


def f_d5_prime(x):
    return 5 * x ** 4 + 8 *x ** 3 + 9 * x ** 2 + 8 * x + 5

root = scipy.optimize.newton(f_d5, 111112222221110, f_d5_prime, maxiter=300)
print(root)

