import numpy as np

def square(a):
    return a*a

def script():
    x = np.linspace(0,5,20)
    y = square(x)
    return y
