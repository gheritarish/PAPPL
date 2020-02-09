import os

def square(a):
    return a*a

def mv_dir(name):
    os.system("cd " + name)
    return str(os.system("pwd"))

def script():
    x = 5
    y = square(x)
    return y
