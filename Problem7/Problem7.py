def nth_prime(nth_term):
    prime_num = 2 # 2 is first prime
    #also prime_num is not actually always a prime...
    count = 0
    nth_prime = prime_num
    irr_count = 1

    while irr_count > 0:
        factor = 2

        if count == nth_term:
            return nth_prime

        while factor <= prime_num:
            #checks if prime_num is prime.
            #if prime_num is a prime, count + 1
            #if not, then prime_num + 1
            if factor == prime_num: # here prime_num must be a prime
                count += 1
                nth_prime = prime_num 
                prime_num += 1
                factor = 2
                break # need break to avoid inf looping

            elif (prime_num % factor) != 0:
                factor += 1
 
            else:
                irr_count += 1
                prime_num += 1
                factor = 2
                break # need break to avoid inf looping

print nth_prime(10001)
