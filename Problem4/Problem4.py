def Thr_dig_prod_palindrome(): #fuck this
    
    num1 = 999
    num2 = 999
    num3 = 999

    while num1 > 0:
    
        poss = str(num1 * num2)

        if poss[0:] != poss[0::-1]:

             num1 -= 1

        elif poss[0:] == poss[0::-1]:

            return poss

    if num1 == 0:

        poss = str(num2 * num3)

        if poss[0:] != poss[0::-1]:

            num2 -= 1
            num3 -= 1

        elif poss[0:] == poss[0::-1]:

            return poss

        else:

            return 'nope'

    else:

        return 'num1 never is 0'


def test_for_pal1(num): #fuck this
    
    num1 = num
    result = []

    for numb in range(num1, 0, -1):

        poss = str(num1 * numb)

        if poss[0:] == poss[0::-1]:

            result += int(poss)
    
    if result != []:

        return result

    else:

        return 'Nope'

def three_dig_prod_pal():# fuck this

    num1 = 999
    count = 999
    result = []
    final = []
    actual_ans = []
    answer = 0

    while count > 0:

        if test_for_pal1(num1) != 'Nope':

            result += test_for_pal1(num1)
            count -= 1
            num1 -= 1

        else:

            count -= 1
            num1 -= 1

    #for shit in result:

        #final += [int(shit)]

    for entry in final:

        if entry > answer:

            answer = entry

    return answer


#THE FOLLOWING FUCKING WORKS
def find_palindrome(num):

    pnum = str(num)

    if pnum[0:] == pnum[::-1]:

        return True

    else:

        return False

def thr_dig_palindrome(min, max):

    results = []
    ans = 0

    for num1 in range(max, min - 1, -1):

        for num2 in range(num1, min - 1, -1):

            poss_pal = num1 * num2

            if find_palindrome(poss_pal) == True:

                results += [poss_pal]

    for num in results:

        if num > ans:

            ans = num

    return ans

print thr_dig_palindrome(100,999)
