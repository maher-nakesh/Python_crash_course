def sieve_of_eratosthenes(n):
    prime=[]
    for k in range (2,n):
        prime.append(k)
    i = 2
    while (i <= int(n**(1/2))):
        if i in prime:
            for j in range(i * 2, n + 1, i):
                if j in prime:
                    prime.remove(j)
        i = i + 1
    return print (prime)



sieve_of_eratosthenes(10)