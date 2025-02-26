

def prime_num (n):
    if n < 2:
          return False
    for prime_range in range (2, int(n**0.5) + 1):
         if n % prime_range == 0:
              return False
    return True
num = int(input("enter the number: "))
if prime_num(num):
     print(f"your number is prime number")
else:
     print(f"your number is not a prime number")



