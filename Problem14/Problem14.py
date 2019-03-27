#collatz seq
import timeit

def col_seq():
    strt_num = 1
    num = strt_num
    count = 0
    answer = 0
    max_count = 0

    while strt_num <= 1000000:
        while num > 1:
            if num % 2 == 0:
                num /= 2
            elif num % 2 != 0:
                num = (3 * num) + 1
        
            count += 1

        if count >= max_count:
            max_count = count
            answer = strt_num
    
        count = 0
        strt_num += 1
        num = strt_num
    
    return answer

print timeit.timeit(col_seq)
