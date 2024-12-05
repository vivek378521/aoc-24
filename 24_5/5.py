from collections import defaultdict

with open("5.txt", "r") as file:
    lines = file.readlines()

split_index = lines.index("\n")
part1 = lines[:split_index]
part2 = lines[split_index + 1 :]

rules = {}
for line in part1:
    key, value = map(int, line.strip().split("|"))
    if key not in rules:
        rules[key] = []
    rules[key].append(value)

arrays = [list(map(int, line.strip().split(","))) for line in part2]

total = 0
total2 = 0


def fix_update(rules, array):
    filtered_rules = defaultdict(set)
    for i in array:
        filtered_rules[i] = set(rules[i]).intersection(set(array))

    # ordered_items = sorted(filtered_rules.items(), key=lambda x: len(x[1]), reverse=True)
    # ordered_keys = [i[0] for i in ordered_items]
    ordered_keys = sorted(
        filtered_rules, key=lambda k: len(filtered_rules[k]), reverse=True
    )

    return ordered_keys


def is_valid(rules, array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[j] not in rules[array[i]]:
                return False
    return True


for array in arrays:
    if is_valid(rules, array):
        total += array[len(array) // 2]

for array in arrays:
    if not is_valid(rules, array):
        fix_update_arr = fix_update(rules, array)
        total2 += fix_update_arr[len(array) // 2]


print(total)
print(total2)
