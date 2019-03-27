def sum_of_multiples(num1, num2, limit):

    mult_num1 = num1
    mult_num2 = num2
    sum_list1 = []
    sum_list2 = []
    total_sum1 = 0
    total_sum2 = 0

    while mult_num1 < limit:

        sum_list1 += [mult_num1]
        mult_num1 = mult_num1 + num1

    while mult_num2 < limit:

        sum_list2 += [mult_num2]
        mult_num2 = mult_num2 + num2

    for num_1 in sum_list1:
        if num_1 % 5 != 0:
            total_sum1 += num_1

    for num_2 in sum_list2:

        total_sum2 += num_2

    total_sum = total_sum1 + total_sum2
    print total_sum2
    print total_sum1

    return total_sum

print sum_of_multiples(3, 5, 1000)

