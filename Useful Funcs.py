def test_min_primes(num):
    #returns a list of minimum necessary primes used to test for other primes
    prime_lst = []
    max_num = (num ** 0.5)

    for poss_prime in range(2, int(max_num)):
        for factor in range(2, poss_prime):
            if poss_prime % factor == 0:
                break

        else:
            prime_lst += [poss_prime]

    return prime_lst

def lst_primes(num):
    #creates a list of all primes < num
    poss_prime = 2
    test_lst = test_min_primes(num)
    prime_lst = []

    while poss_prime < num:
        count = 0
        
        for prime in test_lst:
            if poss_prime % prime != 0 or poss_prime == prime:
                count += 1
                
                if count == len(test_lst):
                    prime_lst += [poss_prime]
                    poss_prime += 1
                   
                    break
                
                continue

            else:
                poss_prime += 1
                
                break

    return prime_lst
