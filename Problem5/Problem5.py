'''Smallest pos num that is evenly divisible by [nums]'''
def smallest_multiple(lst_nums):
    '''only works if 2nd number isn't 1 or 0'''
    test_lst = lst_nums
    count = 0
    s_mult = test_lst[0] * test_lst[1]

    while count <= len(test_lst):
        for num in test_lst:
            if (s_mult % num) != 0:
                s_mult += 1
                count = 0
            elif (s_mult % num) == 0:
                count += 1

    return s_mult

tst_lst = range(1, 21)

print smallest_multiple(tst_lst)
