import re
file = open('regex_sum_142488.txt')
fileR = file.read()
fileN = re.findall('[0-9]+', fileR)
print(fileN)

total = 0

for num in fileN :
    total = total + int(num)

print(total)
