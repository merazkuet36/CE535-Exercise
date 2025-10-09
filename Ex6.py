# Value of a house in dollar (float)
value = 350000.0  

# Down payment in dollar (float)
downpay = 70000.0  

# yearly fixed rate (float)
fixed_rate = 0.06  

# number of years (int)
N = 20

# print 
message = f'''Calculating mortgage for $ {value}
    with down payment $ {downpay}
    at yearly rate {fixed_rate*100}%
    for {N} years
'''
print(message)


# The mortgaged amount
PV = value - downpay

# The monthly rate
i = fixed_rate / 12

# The number of months 
n = N * 12

# The monthly payment
PMT = PV * (i * (1 + i)**n) / ((1 + i)**n - 1)

# Outputs
# The total payment for all months (float)
totalPMT = PMT * n

# The total interest to pay (float)
totalInterests = totalPMT - PV

# Output message
output_message = f'''
Monthly payment is: ${PMT:.2f}
The total payment for the loan is: ${totalPMT:.2f}
The total interest to be paid is: ${totalInterests:.2f}
'''
print(output_message)

# Leap Year check
year = 2024  

# Check 
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# using DeMorgan's Laws
is_not_leap = not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

# Result
leap_year_message = f"The year {year} is {'a leap year' if is_leap else 'not a leap year'}."
print(leap_year_message)
