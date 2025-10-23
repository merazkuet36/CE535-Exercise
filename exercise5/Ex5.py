import math

# Define a variable with name 'angle' and a positive floating number
angle = 45.0  # Example: 45 degrees

# Define a variable with name 'Angle' and a negative floating number
Angle = -30.0  # Example: -30 degrees

# Define a variable with name 'index' and an integer number
index = 5  # Example: index = 5

# Define a variable with name 'msg' and a string value
msg = "This is a sample string!"  # Example message

# Math operations and the math library
# Volume of a cylinder with height of 12.5 meters and radius of 0.32 meters
radius = 0.32  # in meters
height = 12.5  # in meters
V = math.pi * radius**2 * height  # Volume of cylinder: πr²h

# Area of a circle with radius 2.5 inches
radius_circle = 2.5  # in inches
A = math.pi * radius_circle**2  # Area of circle: πr²

# Convert 37 degree Celsius to Fahrenheit
C = 37  # Celsius temperature
F = 1.8 * C + 32  # Fahrenheit formula

# the difference between two powers of 10
y = 10**(2/3) - 10**0.5   # As required by test_y()

# Display the results
print(f"Angle: {angle} degrees")
print(f"Angle: {Angle} degrees (negative)")
print(f"Index: {index}")
print(f"Message: {msg}")
print(f"Volume of the cylinder (V): {V:.2f} cubic meters")
print(f"Area of the circle (A): {A:.2f} square inches")
print(f"y = {y:.4f}")
print(f"Temperature in Fahrenheit (F): {F:.2f}°F")
print("DEBUG Angle repr:", repr(Angle))
