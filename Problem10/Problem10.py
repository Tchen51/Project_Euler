def sum_prime(num):
    sum_primes = 0
    poss_prime = 2
    test_lst = eff_test_primes(num)

    while poss_prime < num:
        count = 0
        for prime in test_lst:
            if poss_prime % prime != 0 or poss_prime == prime:
                count += 1
                if count == len(test_lst):
                    sum_primes += poss_prime
                    poss_prime +=1
                    break
                continue

            else:
                poss_prime += 1
                break
    
    return sum_primes

def test_primes(num):
    #returns list of necessary primes to use to test for other primes
    prime_lst = []
    max_num = (num ** 0.5)
    poss_prime = 2

    while poss_prime < max_num:
        factor = 2

        while (factor <= poss_prime):
            if factor == poss_prime:
                prime_lst += [poss_prime]
                factor = 2
                poss_prime += 1
                break

            elif (poss_prime % factor) != 0:
                factor += 1

            else:
                poss_prime += 1
                factor = 2
                break

    return prime_lst

def eff_test_primes(num):
    #same as test_primes, just more efficient
    prime_lst = []
    max_num = (num ** 0.5)
    
    for poss_prime in range(2, int(max_num)):
        for factor in range(2, poss_prime):
            if poss_prime % factor == 0:
                break

        else:
            prime_lst += [poss_prime]
    
    return prime_lst
print sum_prime(2000000)
#print eff_test_primes(37)
