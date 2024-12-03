import re
regex = r'mul\((\d{1,3}),(\d{1,3})\)'
data = open('03.txt').read()

result = sum(int(a) * int(b) for a, b in re.findall(regex, data))
print(result)

result = sum(
    int(a) * int(b)
    for s in data.split('do()')
    for a, b in re.findall(regex, s.split("don't()")[0])
)
print(result)
