def py_trip_prod():#sum of nums is 1000
    a = 0
    b = 0
    c = 0

    a_lst = range(0, 500)
    b_lst = range(0, 500)
    c_lst = range(0, 1000)

    for num_a in a_lst:
        for num_b in b_lst:
            for num_c in c_lst:
                if ((num_a + num_b + num_c) == 1000) & ((num_a ** 2 + num_b **2) == (num_c ** 2)):
                    return num_a * num_b * num_c

print py_trip_prod()
