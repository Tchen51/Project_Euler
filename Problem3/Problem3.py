def largest_prime_factor(num):

    small_factor = 2
    temp_num = num
    
    while small_factor < (temp_num ** 0.5):

        if (temp_num % small_factor) == 0:
        
            temp_num = temp_num / small_factor
            small_factor = 2

        else:

            small_factor += 1

    return temp_num

print largest_prime_factor(600851475143)
