def sieve(n):
    if n <= 1:
        return []
    if n == 2:
        return [2]

    primes = [2]

    for i in range(3, n+1):
        for x in primes:
            is_prime = True
            if i%x == 0:
                is_prime = False
                break
            if is_prime:
                primes.append(i)
                break
                # print(i)
    return primes


def sieve2(n):
    for i in range(2, n):
        c = 0
        for j in range(2, i):
            if i%j == 0:
                c += 1
        if c == 0:
            print(i, end=" ")


# print(sieve(100))
print(sieve2(100))
