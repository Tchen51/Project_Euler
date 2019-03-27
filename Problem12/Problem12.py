#generates triangular nums w/out storing
#at each num, check to see if it has > 500 divisors
last_num = 1
idx = 2
t_num = last_num + idx
div_count = 0
answer = 0
limit = 500

while div_count <= limit:
    factor = 1
    
    while factor <= (t_num ** 0.5):
        if t_num % factor == 0:
            div_count += 1
            #print div_count
        factor += 1

    if div_count > (limit / 2):
        answer = t_num
        break

    else:
        #print t_num
        idx += 1
        last_num = t_num
        t_num = last_num + idx
        div_count = 0
        factor = 1

print answer
