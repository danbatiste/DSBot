from __future__ import print_function
from cmath import *
import sys

ln = log

def nPr(n,r):
    return factorial(n) / (factorial(r) * factorial(n-r))

def nCr(n,r):
    return nPr(n,r) / factorial(r)
    
def re(z):
    return z.real()

def im(z):
    return z.imag()

def sum(f,n,k):
    x = 0
    u = 0
    for u in range(n,k):
        x += eval(f)
        u += 1
    return x

#Main functions

def iterate(y, iterations, x0):
    if type(iterations) in [float, str]:
        iterations = int(iterations)

    f = eval("lambda x: {}".format(y))
    x1 = x0
    x2 = -x0

    try:
        if f(0) == 0:
            return 0
    except:
        ...

    for n in range(iterations):
        x1 = f(x1)
        if str(x1) in ['inf','nan','nanj']:
            for n in range(iterations):
                x2 = f(x2)
            return x2   
    return x1
        


def solve(y):
    i = 2
    while 1:
        try:
            return iterate(y, 10000, i)
        except:
            i += 1
            continue

def main():
    f = get_input("x = ")
    iterations = float(get_input("\niterations = "))
    x0 = float(get_input("\nx0 = "))

    print("\n\nAnswer = {}".format(iterate(f, iterations, x0)))
    input("Press enter to continue...")

if __name__ == "__main__":
    get_input = input

    if sys.version_info[:2] <= (2, 7):
        get_input = raw_input

    main()