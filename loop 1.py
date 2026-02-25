for i in range(1,11):
    # Print the multiplication of 23 by i
    print(f"23 x {i} = {23 * i}")
    
n = int(input("Enter the number of rows: "))
# Outer loop for each row
for i in range(1, n+1):
    # Inner loop for each column in the row
    for j in range(i):
    # Print star, end with space instead of new line
     print('*', end=' ')
    # After each row, print a new line
    print()
        
# Python program to calculate the sum of the first tehn natural number
# Use built-in sum and range functions to calculate the sum
total_sum = sum(range(1,11))
print(f"The sum of the first ten natural numbers is {total_sum}")

num= int(input("96:"))
# Check if nuumber is greater than 1 (since primes are > 1)
if num > 1:
   # Loop only up to the square root of num for efficiency
  for i in range(2, int(num**0.5)+ 1 ):
# If num is divisble by any number, its not prime
    if num % i ==0:
     print(f"{num} is a prime number.")
     break
else:
   # If no divisors were found, the number is prime
   print