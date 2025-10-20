N = 100  # The range of prime numbers

primes = [] # list to store the numbers

for num in range(2, N+1): # outer loop
     is_prime = True # assume the number prime initially
     
     for i in range(2, num): # inner loop
    
      if num % i == 0:  # if number is divide by i
          
          is_prime = False  # break the loop
          
     if is_prime:
         primes.append(num)  # storing the numbers it to the priviously created list
               
      
print("The prime numbers btn 2 and", N, ":", primes)  