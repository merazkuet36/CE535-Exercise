# Exercise 7

# input number
input_number = -3.5  

# output variable
category = 'not assigned'  

# statements
if input_number > 0:
    category = 'positive'
elif input_number < 0:
    category = 'negative'
else:
    category = 'zero'

# Print result
print(f"Input number = {input_number}, Category = {category}")


# Cemented soil model computation


# constants 
Kpyz = 2.0
C = 0.171
n = 3.0
b = 1.0
yk = 0.005
yM = b / 60.0
yU = 3 * b / 80.0
Kpm = -1.5

# Derived constants
pM = C * (yM ** (1 / n))
pU = pM + Kpm * (yU - yM)

# deflection y in mm
y = 0.02

# output variable p
p = 0.0

# Conditional flow 
if y < yk:
    p = Kpyz * y
elif y < yM:
    p = C * (y ** (1 / n))
elif y < yU:
    p = pM + Kpm * (y - yM)
else:
    p = pU

# Print result
print(f"For y = {y:.4f} mm, soil resistance p = {p:.5f} kN/m")


# Heaviside function 


import math

# Define variable x
x = 10.0
flag = 0

# Incomplete if condition fixed with 'pass'
if x < 0:
    pass  # No operation when x < 0
else:
    flag = 1

print(f"Heaviside flag (using pass): {flag}")

# Using ternary operator
ternary_flag = 0 if x < 0 else 1
print(f"Ternary flag: {ternary_flag}")

# Define g 
g = 0.0

match ternary_flag:
    case 0:
        g = math.sin(x)
    case 1:
        g = math.cos(x)
    case _:
        g = 0.0  # default case

print(f"For x = {x}, g(x) = {g:.5f}")
