left_list = []
right_list = []
with open("1.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        left, right = line.strip().split("  ")
        left_list.append(int(left))
        right_list.append(int(right))

left_list = sorted(left_list)
right_list = sorted(right_list)

total_dist = 0
for i in range(len(left_list)):
    total_dist += abs(right_list[i] - left_list[i])

print(total_dist)

frequency = {}

for num in right_list:
    frequency[num] = frequency.get(num, 0) + 1

total_sim = 0

for num in left_list:
    if num in frequency:
        total_sim += num * frequency[num]

print(total_sim)
