data = open('04.txt').read().split('\n')

words = ['XMAS', 'SAMX']
result = 0
n = len(data)
for i in range(n):
    for j in range(n):
        if j < n - 3 and ''.join([data[i][j + k] for k in range(4)]) in words:
            result += 1
        if i < n - 3 and ''.join([data[i + k][j] for k in range(4)]) in words:
            result += 1
        if j < n - 3 and i < n - 3 and ''.join([data[i + k][j + k] for k in range(4)]) in words:
            result += 1
        if j < n - 3 and i < n - 3 and ''.join([data[i + k][j + 3 - k] for k in range(4)]) in words:
            result += 1

print(result)

result = 0
for i in range(len(data) - 2):
    for j in range(len(data) - 2):
        diag1 = ''.join([data[i + k][j + k] for k in range(3)])
        diag2 = ''.join([data[i + k][j + 2 - k] for k in range(3)])
        if diag1 in ['MAS', 'SAM'] and diag2 in ['MAS', 'SAM']:
            result += 1

print(result)
