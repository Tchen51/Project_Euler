def sum_multiples(num1, num2, limit):

    count = 1
    sum = 0

    while count < limit:
        
        if count % 3 == 0 and count % 5 != 0:
            sum = sum + count
        elif count % 5 == 0:
            sum = sum + count
        count = count + 1
    return sum

print sum_multiples(3, 5, 1000)

