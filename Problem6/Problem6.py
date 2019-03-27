def sum_sq_diff(upper_limit):
    lst_nums = range(1, upper_limit + 1)
    sum_indi_num = 0
    sum_all_num = 0

    for num in lst_nums:
        sum_indi_num += (num ** 2)

    for num in lst_nums:
        sum_all_num += num

    sum_sq_diff = (sum_all_num ** 2) - sum_indi_num

    return sum_sq_diff

print sum_sq_diff(100)
