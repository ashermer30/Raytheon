import math as mt
import time

def SieveOfEratosthenes(n):
    """Using the sieve of Eratostenes method to find the prime numbers between 1 and n.
    Create array of prime=True values with size n. Remove all non-prime values until
    left with only the prime values."""
    #Initialise array of Prime True values.
    prime = [True for i in range(n+1)]
    #0 and 1 are not prime numbers so first set those values to False.
    prime[0] = False
    prime[1] = False
    #Start at p=2, the smallest prime number.
    p = 2
    #iterate through up to sqrt n
    for p in range(2, int(mt.sqrt(n))+1):
        
        if prime[p]:
            #remove the multiples of p starting at p*p.
            for i in range(p*p, n+1, p):
                prime[i] = False
        p+=1
    for p in range(n+1):
        if prime[p]:
            print(p)

if __name__=='__main__': 
    #Main run file section.
    n = 100
    t0 = time.time()
    print("Prime numbers between 1 and", n,":")
    SieveOfEratosthenes(n)
    t1 = time.time()
    print("Time taken:", t1-t0)
        
        
    
        