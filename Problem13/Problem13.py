import string
import sys

filename = sys.argv[1]
num_lst = []

try:
    numfile = open(filename)

except:
    exit()

for line in numfile:
    num_lst += [string.split(line)]

numfile.close()

for line in range(0, len(num_lst)):
    for num in range(0, len(num_lst[line])):
        num_lst[line] = int(num_lst[line][num])

big_sum = 0

for num in num_lst:
    big_sum += num

big_sum = str(big_sum)
answer = ''

for num in range(0, 10):
    answer += big_sum[num]

print answer
