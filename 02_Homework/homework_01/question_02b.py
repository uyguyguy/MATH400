'''
Shixin Wang
MATH 400-01 Homework 1 Question 2a

Description: This is the program of bisection, it will result to an estimate of the root depends on the error given.
'''

'''
PLEASE READ!!!
RUN PORGRAM: run `python -u .\question_02b.py` in the terminal 
             and make sure the current path is where the "question_02b.py" locatted.
'''


import sys
import math
import numpy as np
format_output_decimos = '0.7f'  # all out put will round to 7 decimos

'''
f: function
a: lower bound
b: upper bound
delta: error bound
'''


def bisection(f, a, b, delta, return_x_list=False):

    fa = f(a)  # get value of f(a)
    fb = f(b)  # get vblue of f(b)
    possible_value_max = (abs(b-a))/2

    # check is the function have a root in range [a,b]
    if fa*fb > 0:
        print(
            "Error! function in range [a,b] must have different signs at the endpoints. Aborting")
        sys.exit(1)

    # print all initial values and round to 6 decimos
    print(f"initial interval: a = {format(a, format_output_decimos)}; b = {format(b, format_output_decimos)}; fa = {format(fa, format_output_decimos)};",
          f" fb = {format(fb, format_output_decimos)}; Error_Bound = {format(possible_value_max, format_output_decimos)}")

    iteration_counter = 0  # record the iteration times
    if return_x_list:
        x_list = []

    while(possible_value_max > delta):

        c = float(b+a)/2  # midpoint of the interval
        fc = f(c)  # value of f at c

        if fa*fc < 0:  # if a & c have different sign
            b = c  # set b to midpoint since they have same sign
            fb = fc  # same as the f value of b
        else:  # if a & c have same sign
            a = c  # same as above
            fa = fc

        possible_value_max = (abs(b-a))/2  # reset error bound

        iteration_counter += 1
        if return_x_list:
            x_list.append(c)

        # print all values and round to 6 decimos
        print(f"n{'%02d' % iteration_counter}: a = {format(a, format_output_decimos)}; b = {format(b, format_output_decimos)}; c = {format(c, format_output_decimos)}; fa = ",
              f"{format(fa, format_output_decimos)}; fb = {format(fb, format_output_decimos)}; fc = {format(fc, format_output_decimos)}; max_possible_value = {format(possible_value_max, format_output_decimos)}")

    if return_x_list:
        return x_list, iteration_counter
    else:
        return c, iteration_counter


def f(x):
    return ((5-x)*np.e**x)-5


solution, num_iterations = bisection(f, 4, 5, 1e-6)
print("Number of iterations = ", num_iterations)
print("An estimate of the root is ", solution)
