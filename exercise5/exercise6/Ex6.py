# Value of a house in dollars (float)
value = 350000.0  

# Down payment in dollars (float)
downpay = 70000.0  

# Yearly fixed interest rate (float)
fixed_rate = 0.06  

# Number of years (int)
N = 20  


# Message printed to users (str)

message = f'''Calculating mortgage for ${value}
    with down payment ${downpay}
    at yearly rate {fixed_rate*100:.2f}%
    for {N} years
'''
print(message)


# Internal variables


# The mortgaged amount (principal)
PV = value - downpay  

# The monthly interest rate (1/12 of yearly rate)
i = fixed_rate / 12  

# The number of months (12 × number of years)
n = N * 12  

# The monthly payment formula:
# PMT = PV * (i * (1 + i)**n) / ((1 + i)**n - 1)
PMT = PV * (i * (1 + i)**n)
PMT /= ((1 + i)**n - 1)   # shorthand division operator (/=) as required

# -----------------------------------------------
# Outputs
# -----------------------------------------------

# The total payment for all months (float)
totalPMT = PMT * n  

# The total interest to pay (float)
totalInterests = totalPMT - PV  

# Output message to users (str)
output_message = f'''
Monthly payment is: ${PMT:.2f}
The total payment for the loan is: ${totalPMT:.2f}
The total interest to be paid is: ${totalInterests:.2f}
'''
print(output_message)


# Leap year check


# Input year (int)
year = 2024  

# Boolean expression: True if leap year
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)  

# Using DeMorgan’s Laws (expanded form)
# not(A and B) → (not A) or (not B)
# not(A or B) → (not A) and (not B)
is_not_leap = ((year % 4 != 0) or (year % 100 == 0)) and (year % 400 != 0)

# Message about leap year status (str)
leap_year_message = f"The year {year} is "
leap_year_message += "a leap year." if is_leap else "not a leap year."
print(leap_year_message)