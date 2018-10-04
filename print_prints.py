"""printing 100 primes"""
import math

for num in range(2, 101):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    if prime:
        print(num)


print("---------")

for num in range(2, 101):
    if all(num % i != 0 for i in range(2, num)):
        print(num)

print("---------")

for num in range(2, 101):
    if all(num % i != 0 for i in range(2, int(math.sqrt(num))+1)):
        print(num)
