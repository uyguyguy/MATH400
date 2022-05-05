def secant(f, x0, x1, delta, Nmax):
    """


    Parameters
    ----------
    f     : function whose root we want to find

    x0,x1 : Left and right endpoints, respectively, of initial interval
    delta : The tolerance/accuracy we desire
    Nmax  : Maximum number of iterations to be performed

    Raises
    ------
    Exception
        DESCRIPTION.

    Returns
    -------
    x : The approximation to the root
        DESCRIPTION.
    iter_counter : Number of iterations it takes to satisfy tolerance

    """
    iter_counter = 0  # set iteration counter to zero

    fx0 = f(x0)
    fx1 = f(x1)
    while abs(fx1) > delta and iter_counter < Nmax:
        try:
            dx = (fx1 - fx0)/(x1-x0)
            x = x1 - fx1/dx  # Secant method
        except:
            raise Exception("Division by zero. f'(x) = 0")

        x0 = x1
        x1 = x
        fx0 = fx1
        fx1 = f(x1)

        iter_counter += 1

    return x, iter_counter


def f(x):
    return x**4-5  # x**2-3 #(5.0-x)*math.exp(x)-5


solution, no_iterations = secant(f, 1, 2, 1e-6, 100)
print("Number of iterations = ", no_iterations)
print("An estimate of the root is ", solution)
