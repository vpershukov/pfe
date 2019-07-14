file = open('mbox-short.txt')

counts = dict()

for line in file :
    if line.startswith('From ') :
        email = line.split()[1]
        counts[email] = counts.get(email, 0) + 1

common_email = None
common_num = None

for email, num in counts.items() :
    if common_email is None or common_num < num :
        common_email = email
        common_num = num

print(common_email, common_num)
