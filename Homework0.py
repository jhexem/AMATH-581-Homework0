import numpy as np
import matplotlib.pyplot as plt

A1 = np.array([[12, 37], [-9, 0]])

def f(x):
   return -x - np.cos(x)   #defines function f

def fprime(x):
   return -1 + np.sin(x)   #defines derivative of f

def newtons_method(x0):   #takes initial guess as input and returns 
   x = np.empty(1)   #initialize array
   x[0] = x0
   for i in range(1000):
      x = np.append(x, [x[i] - f(x[i])/fprime(x[i])])   #calculate next guess
      fc = f(x[i + 1])    #calculate function value at the next guess
      if np.abs(fc) < 10**(-6):   #checks to see if function is within the required error and quits loop if this value is within the error
         break
   return (np.transpose([x]), i + 2)

def bisection_method(xl, xr):
   a = np.empty(1)
   for i in range(1000):
      midpoint = (xl + xr) / 2   #calculate midpoint
      fc = f(midpoint)   #calculate function
      a = np.append(a, [midpoint])   #adds midpoint to array of midpoints
      if np.abs(fc) < 10**(-6):   #checks if function is within the required error and breaks if it is
         break
      if f(xl) * fc < 0:      #sets the right endpoint equal to the midpoint if the root is in the left half
         xr = midpoint
      else:   #sets the left endpoint equal to the midpoint if the root is in the right half
         xl = midpoint
   return (a[1:], i + 2)
      
solA2 = newtons_method(-3)   #calls the newtons_method function with desired input
solA3 = bisection_method(-3, 1)   #calls the bisection_method function with desired input

A2 = solA2[0]
A3 = solA3[0]
A4 = np.array([solA2[1], solA3[1]])

x = np.array([1, 3, 4, 8, 9])   #defines data points
y = np.array([3, 4, 5, 7, 12])
solA5 = np.polyfit(x, y, 1)   #finds line of best fit

A5 = solA5[0]

'''linex = np.array([0, 15])   #plots points and line of best fit
liney = np.array([solA5[1], (solA5[0] * 15) + solA5[1]])
plt.plot(x, y, 'ro', linex, liney)
plt.axis([0, 10, 0, 15])
plt.show()'''

A = np.array([[-0.1, 3], [3, -0.1]])   #defines the matrix and vector
b = np.array([[-0.2], [0.2]])

A6 = np.linalg.solve(A, b)

print(A1)