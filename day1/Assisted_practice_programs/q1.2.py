#PROG 1.2 Adding 2 Numbers Measuring Time

import time 
first= int(input("Enter the first number: "))
second= int(input("Enter the second number: "))
start_time=time.time()
total=first+second
end_time=time.time()

print(f"The sum of the two numbers is: {total}")
print(f"Time taken to execute the program: {end_time - start_time} seconds")

