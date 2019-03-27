def pwrdigsum(num):
    #2^x, then sums digits
    pwrnum = 2 ** num
    sum_digits = 0
    for digit in str(pwrnum):#casts pwrnum to string so I can iterate
        sum_digits += int(digit)

    return sum_digits

print pwrdigsum(1000)
