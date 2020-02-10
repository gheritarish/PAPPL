import os

def square(a):
    return a*a

def mv_dir(name):
    # Faire des tests sur l'entrée, attention aux guillemets, | et ;
    os.system("cd " + name + "; ls")
    return str(os.system("ls"))

def script():
    x = 5
    y = square(x)
    return y
