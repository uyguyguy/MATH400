'''
Shixin Wang
MATH 400-01 Homework 1 Question 1
'''

'''
PLEASE READ!!!
RUN PORGRAM: run `python -u .\question_01.py` in the terminal 
             and make sure the current path is where the "question_01.py" locatted.
'''


# Question 1:
# Function: e^(-( (x^2 + y^2 + z^2 + t^2) / 2) )
# N = 10^6; 0<=x<=10; 0<=y<=x; 0<=z<=y; 0<=t<=z
# 4D Monte Carlo Integration




import numpy as np
def monte_carlo_4D(function, domain, x_range, y_range, z_range, t_range, n):
    # area of rectangle
    area_rectangle = (x_range[1] - x_range[0]) * (y_range[1] - y_range[0]) * \
        (z_range[1] - z_range[0]) * (t_range[1] - t_range[0])
    num_inside = 0  # number of points inside the integration domain
    sum_f = 0  # sum of f values inside the integration domain

    # give n random values to all axis
    # index 0 is the min, index 1 is the max
    x = np.random.uniform(x_range[0], x_range[1], n)
    y = np.random.uniform(y_range[0], y_range[1], n)
    z = np.random.uniform(z_range[0], z_range[1], n)
    t = np.random.uniform(t_range[0], t_range[1], n)

    # check n random points and pick up points in integration domain
    for i in range(n):
        if domain(x[i], y[i], z[i], t[i]):
            num_inside += 1
            sum_f += function(x[i], y[i], z[i], t[i])

    average_function = sum_f / float(n)  # average of function

    return area_rectangle * average_function, average_function, area_rectangle


# check is random point is inside the integration domain (not equal 0)
# N = 10^6; 0<=x<=10; 0<=y<=x; 0<=z<=y; 0<=t<=z
def isInsideFunction(x, y, z, t):
    if 0 <= x <= 10 and 0 <= y <= x and 0 <= z <= y and 0 <= t <= z:
        return True
    else:
        return False


# domain of rectangle in 4 axis
range_rectangle = [
    [0, 10],
    [0, 10],
    [0, 10],
    [0, 10]
]

# number of random points to estimate the integral
n = 10**6


def f(x, y, z, t):
    return np.e**(-((x**2 + y**2 + z**2 + t**2)/2))


I, average_function, x = monte_carlo_4D(f, isInsideFunction,
                                        range_rectangle[0], range_rectangle[1], range_rectangle[2], range_rectangle[3], n)

print(f"""
========== Question 1 ==========

The value of the integral: {I}
The average of function: {average_function}
Total random points created: {n}

================================
""")
