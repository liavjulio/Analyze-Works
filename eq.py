import math

def eq1(x):
    return 4.86 + 0.018 * x

def eq2(x):
    return x / 3000

def eq3(x):
    a0 = 0.0047
    a1 = 0.0023
    a2 = 0.000043
    return x * (a0 + a1 * math.log(x) + a2 * math.log(x)**2)

def eq4(x):
    return 4.2 + 0.0015 * (x ** (4 / 3))

def eq5(x):
    return 0.069 + 0.00156 * x + 0.00000047 * (x ** 2)
x = 658
print(eq1(x))
print(eq2(x))
print(eq3(x))
print(eq4(x))
print(eq5(x))
