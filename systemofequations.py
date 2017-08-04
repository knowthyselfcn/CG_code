# -*- coding: utf8 -*-

from __future__ import division

import numpy as np
import numpy.linalg

import scipy
import scipy.linalg



# square matrix
def randomGenHugeFullRankMatrix(dim):
    return np.random.rand(dim, dim)

d = 5

vb = range(1, d+1)
vx = list( reversed(vb) )

m =  randomGenHugeFullRankMatrix(d)


for i,v in enumerate(vx):
    x = vx[i]
    b = vb[i]
    mn = b / x
    #print(mn)
    m[i][i] = mn

#r = numpy.linalg.matrix_rank(m)
#print(r)

P, L, U = scipy.linalg.lu(m)
#print(P, L, U)

c = scipy.linalg.cholesky(m)
print(c)