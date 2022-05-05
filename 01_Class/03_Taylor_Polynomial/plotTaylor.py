
"""
Created on Thu Feb  3 11:00:11 2022

@author: hboateng
"""
# Plot the first four Taylor polynomials for exp(x)
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 2, 500)  # set x values

fx = np.e**(1-x**2)  # exact function

p0 = np.ones(len(x))
p1 = p0 + (-2) * (x - 1)
p2 = p1 + (x - 1)**2
p3 = p2 + (2/3) * (x - 1)**3
p4 = p3 + (x - 1)**4


plt.subplot(3, 2, 1)
plt.plot(x, fx, 'b--', label='fx')
plt.plot(x, p0, 'k-', label='P_0(x)')
#plt.title(f'plot of P_0(x) and f(x)')
plt.legend()

plt.subplot(3, 2, 2)
plt.plot(x, fx, 'b--', label='fx')
plt.plot(x, p1, 'k-', label='P_1(x)')
#plt.title(f'plot of P_1(x) and f(x)')
plt.legend()

plt.subplot(3, 2, 3)
plt.plot(x, fx, 'b--', label='fx')
plt.plot(x, p2, 'k-', label='P_2(x)')
#plt.title(f'plot of P_2(x) and f(x)')
plt.legend()

plt.subplot(3, 2, 4)
plt.plot(x, fx, 'b--', label='fx')
plt.plot(x, p3, 'k-', label='P_3(x)')
#plt.title(f'plot of P_3(x) and f(x)')
plt.legend()

# plt.subplot(3, 2, 5)
# plt.plot(x, fx, 'b--', label='fx')
# plt.plot(x, p4, 'k-', label='P_4(x)')
# #plt.title('plot of P_4(x) and f(x)')
# plt.legend()

# plt.subplot(3, 2, 6)
# plt.plot(x, fx, 'b--', label='fx')
# plt.plot(x, p5, 'k-', label='P_5(x)')
# #plt.title('plot of P_5(x) and f(x)')
# plt.legend()

plt.show()
