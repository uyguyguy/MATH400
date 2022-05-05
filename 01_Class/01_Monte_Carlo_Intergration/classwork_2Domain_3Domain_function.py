# Q: Use Monte Carlo Integration to Estimate:
# 1. fnInt(fnInt(1,x,-(1-y^2)^(1/2),(1-y^2)^(1/2),y,-1,1)
# 2. fnInt(fnInt(fnInt(fnInt(cos(x*y*e^z)), z, xy, 2), y, x, 1), x, 0, 1)

from curses.ascii import FS
import numpy as np

# n represents how many random points wants to draw in rectangle


def IsInsideRange(x, y):
    return (True if (x**2 + y**2 <= 1) else False)


def MonteCarlo_2Domain(f, range, xlow, xhigh, ylow, yhigh, n):
    # draw n random points in the rectangle
    # in the range of (xlow, xhigh), draw n random x-coordinate
    x = np.random.uniform(xlow, xhigh, n)
    # in the range of (ylow, yhigh), draw n random y-coordinate
    y = np.random.uniform(ylow, yhigh, n)

    # Compute sum of f values inside the integration domain
    # 在积分范围中的总额，也可以说在整个矩形中point值的总和，毕竟介于积分外和矩形之间的区域值为0
    fSum = 0.0
    numInside = 0  # number of points inside domain (g)

    for i in range(n):
        for j in range(n):
            if IsInsideRange(x[i], y[j]):
                numInside += 1
                fSum += f(x[i], y[j])

    areaRectangle = (xhigh - xlow) * (yhigh - ylow)
    functionAverage = fSum/float(n**2)

    return areaRectangle * functionAverage
