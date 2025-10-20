import math


pi_approx = 2.0  # Initial pi
i = 1  # Counter to keep track of which term we're at
previous_pi = 0  # Initial previous value of pi 
tolerance = 1e-8  # Tolerance for the error
max_iterations = 100000  # Maximum iterations 
iterations = 0  # number of iterations


while iterations < max_iterations:
    # Calculate the current term 
    curr_pi = pi_approx * (4 * i ** 2) / (4 * i ** 2 - 1)
    
    # Calculate the error between the current and previous approximation
    error = abs(curr_pi - pi_approx)  # Take the absolute difference
    
    # Update the approximation
    pi_approx = curr_pi
    
    # Increment 
    i += 1
    iterations += 1
    
    # stopping the loop
    if error < tolerance:
        break



# Print the final results
print(f"Approximated value of pi: {pi_approx}")
print(f"Difference from real value of pi: {abs(pi_approx - math.pi)}")


#PROBLEM 2

# Train schedule 
schedule = [
    [6, 11, 'Albany'],
    [6, 42, 'Salem'],
    [7, 24, 'Oregon City'],
    [8, 20, 'Portland'],
    [8, 38, 'Vancouver'],
    [9, 11, 'Kelso-Longview'],
    [9, 52, 'Centralia'],
    [10, 13, 'Olympia-Lacey'],
    [10, 53, 'Tacoma'],
    [11, 22, 'Tukwila']
]

# Define the start and end stops
start_stop = 'Albany'
end_stop = 'Portland'

# Initialize variables for start and end times
start_time = None
end_time = None

for stop in schedule:
    hour, minute, stop_name = stop  # Extracting each stop into hour, minute, and stop name
    
    # Convert hour and minute into total minutes from midnight
    time_in_minutes = hour * 60 + minute
    
    # Check 
    if stop_name == start_stop:
        start_time = time_in_minutes
    
    if stop_name == end_stop:
        end_time = time_in_minutes


if start_time is not None and end_time is not None:
    travel_time = end_time - start_time  # Calculate the difference in minutes
    print(f"Travel time from {start_stop} to {end_stop} is {travel_time} minutes.")

