#HW5
#Olivia Gardella

import re

file = open('regex_sum_35643.txt')
list = []

for line in file:
    line = line.rstrip()
    words = re.findall('([0-9]+)', line)
    value = sum(map(int, words))
    list.append(value)

count = 0
for num in list:
    count += num
print(count)
