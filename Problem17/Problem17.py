#number letter count, 1-1000

letter_count = 0

#adds one thousand
letter_count += 11

#sums hundred + and
for idx in range(100, 1000):
    letter_count += 7 #hundred = 7
    letter_count += 3 #and = 3

letter_count -= 27 #subtract extra 'and' for 100, 200, 300, etc

#variable for 1-9
O_Nvar = 0
O_Nvar += 3 #one
O_Nvar += 3 #two
O_Nvar += 5 #three
O_Nvar += 4 #four
O_Nvar += 4 #five
O_Nvar += 3 #six
O_Nvar += 5 #seven
O_Nvar += 5 #eight
O_Nvar += 4 #nine

#sums x-hundred, (one in 100)
for idx in range(0, 100): 
    letter_count += O_Nvar

#variable that sums 20-29, 30-39, 80-89, 90-99
six_var = 0
for idx in range(0, 10):
    six_var += 6 #includes hyphen
six_var *= 4
six_var += O_Nvar * 4


#variable that sums 40-49, 50-59, 60-69
five_var = 0
for idx in range(0, 10):
    five_var += 5 #includes hyphen
five_var *= 3
five_var += O_Nvar * 3

#variable for 70-79
seven_var = 0
for idx in range(0, 10):
    seven_var += 7 #includes hyphen
seven_var += O_Nvar

#var for 10-19
t_var = 0
t_var += 3 #ten
t_var += 6 #eleven
t_var += 6 #twelve
t_var += 8 #thirteen
t_var += 8 #fourteen
t_var += 7 #fifteen
t_var += 7 #sixteen
t_var += 9 #seventeen
t_var += 8 #eighteen
t_var += 8 #nineteen

#var x_1-x_99
hund_sum = 0
hund_sum += t_var
hund_sum += five_var
hund_sum += six_var
hund_sum += seven_var
hund_sum += O_Nvar

#adds hund_sums
for idx in range(0, 10):
    letter_count += hund_sum

print letter_count
