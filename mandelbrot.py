import cmath
import sys

function_input = input("What function should be iterated? (only use built-in and cmath functions, on z and c. ").replace(" ", "").replace("^", "**").replace("i", "j").replace("I", "J")
z_input = complex(input("Initial value for z?\n").replace(" ", "").replace("i", "j").replace("I", "J"))
c_input = complex(input("Initial value for c?\n").replace(" ", "").replace("i", "j").replace("I", "J"))
iterations = int(input("How many iterations?\n").replace(" ", ""))

def f(z, c):
    return eval(function_input)
try:
    temp = f(z_input, c_input)
    print("\n\n")
    print("Iteration:", 1, "\n", "Real Part:", temp.real, "\n", "Imaginary Part:", temp.imag, "\n")
    for n in range(iterations - 1):
        temp = f(temp, c_input)
        print("Iteration:", n + 2, "\n", "Real Part:", temp.real, "\n", "Imaginary Part:", temp.imag, "\n")
except:
    sys.exit("Overflow Error: Your complex number has become too large!\n")

