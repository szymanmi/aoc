from functools import cmp_to_key


def order(a, b):
    if f'{a}|{b}' in rules:
        return -1
    elif f'{b}|{a}' in rules:
        return 1
    else:
        return 0


rules, updates = open('05.txt').read().split('\n\n')
rules = rules.split('\n')
updates = [list(map(int, x.split(','))) for x in updates.split('\n')]

result = [0, 0]
for update in updates:
    sorted_update = sorted(update, key=cmp_to_key(order))
    result[1 if sorted_update != update else 0] += sorted_update[len(sorted_update) // 2]

print(result)
