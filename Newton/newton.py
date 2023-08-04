# Import math library for the exponential, cos and sin functions
import math

# Define the function e^x - 2cos(x)
def f(x):
    return x**4 - 9*(x**3) + 27*(x**2) - 31*x + 12

# Define the derivative of the function e^x - 2cos(x)
def df(x):
    return 4*(x**3) - 27*(x**2) + 54*x - 31

# Define the Newton's method algorithm
def newton(f, df, a, b, error):
    """
    This function calculates the approximated root of a function f(x) using the Newton's method algorithm.
    f: function
    df: derivative of the function f
    a: lower bound of the interval
    b: upper bound of the interval
    error: error to stop the algorithm
    """

    # # Check if the interval is valid
    # if f(a)*f(b) > 0:
    #     print("Intervalo inválido")
    #     return 1.0, 1.0, 1.0
    
    # Set the number of iterations to zero
    k = 0

    # Start with the guess x0 = a
    xk = a

    # Iterate until the error is smaller than the given error
    while abs(f(xk)) >= error:

        # Check if the derivative is zero
        if df(xk) == 0:
            print("Derivada igual à zero")
            return 1.0
        
        # Calculate the next guess
        xk = xk - (f(xk)/df(xk))

        # Increment the number of iterations
        k += 1
    
    # Return the approximated root, the value of f(x) for the approximated root and the number of iterations
    return xk, f(xk), k

# Test the algorithm

# Set the precision of the algorithm
precision = 8

# Set the interval to search for the root
interval = [6, 2]

# Get the result
result = newton(f, df, *interval, 10**(-precision))

# Print the result
print("The approximated root of the function is:", result[0])
print("The number of iterations is:", result[2])
print("The value of f(x) for the approximated root is:", result[1])