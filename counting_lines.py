file = input('Enter name of the file: ')
fOpen = open(file)

count = 0
total = 0

for line in fOpen :
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        m = float(line[20:40].strip())
        total = total + m

print('Average spam confidence:', total / count)
