file = open('mbox-short.txt')
read_file = file.read()
words = read_file.split()

counts = dict()

for word in words :
    counts[word] = counts.get(word, 0) + 1

new_counts = sorted([(a, b) for b, a in counts.items()], reverse=True)
print(new_counts[:1])

for c, d in new_counts[:1] :
    print('The most common word is %s.' % d, 'It counts', c, 'times.')
