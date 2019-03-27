def even_fib_sum(limit):

    num1 = 0
    num2 = 1
    num1_plus_num2 = num1 + num2
    total_sum = 0

    while num1_plus_num2 < limit:
        
        if (num1_plus_num2 % 2) == 0:

            total_sum += num1_plus_num2

        num1_plus_num2 = num1 + num2
        num1 = num2
        num2 = num1_plus_num2
        
    return total_sum

print even_fib_sum(4000000)
