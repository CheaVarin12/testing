#​Write a function to check whether a given number is a prime number (n)

def check_prime(n):
    if n < 2:
        print(n, "is not a prime number.")
        return
    
    i = 2
    while i * i <= n:  
        if n % i == 0:
            print(n, "is not a prime number.")
            return
        i += 1 
    
    print(n, "is a prime number.")

check_prime(7)
check_prime(10)

