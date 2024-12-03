import re

with open("3.txt", "r") as file:
    content = file.read()

pattern = r"mul\((\d+),(\d+)\)"

do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
mul_pattern = r"mul\((\d+),(\d+)\)"

pattern2 = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"

# Find all matches
matches = re.findall(pattern2, content)

total_mut = 0

# for match in matches:
#     total_mut += int(match[0]) * int(match[1])

print(total_mut)

valid_mul = []
is_enabled = True

for token in matches:
    if re.match(do_pattern, token):
        is_enabled = True
    elif re.match(dont_pattern, token):
        is_enabled = False
    elif re.match(mul_pattern, token) and is_enabled:
        match = re.match(mul_pattern, token)
        valid_mul.append((int(match.group(1)), int(match.group(2))))

for mul_val in valid_mul:
    total_mut += mul_val[0] * mul_val[1]

print(total_mut)
