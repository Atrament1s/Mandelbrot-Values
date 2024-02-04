import cmath

z_val = complex(input("Initial value for z?\n").replace(" ", "").replace("i", "j"))
c_val = complex(input("Initial value for c?\n").replace(" ", "").replace("i", "j"))
i_val = int(input("How many iterations?\n").replace(" ", ""))

def f(z, c):
    f_val = z**2+c
    return f_val

temp = f(z_val, c_val)
print("\n\n")
print("Iteration:", 1, "\n", "Real Part:", temp.real, "\n", "Imaginary Part:", temp.imag, "\n")
for n in range(i_val - 1):
    temp = f(temp, c_val)
    print("Iteration:", n + 2, "\n", "Real Part:", temp.real, "\n", "Imaginary Part:", temp.imag, "\n")
