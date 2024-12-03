from collections import Counter

data = [[int(y) for y in x.split('  ')] for x in open('01.txt').read().split('\n')]
list1, list2 = zip(*data)
list1, list2 = sorted(list1), sorted(list2)

print(sum(map(lambda x, y: abs(x - y), list1, list2)))

counts = Counter(list2)

result = sum([i * counts.get(i, 0) for i in list1])
print(result)
