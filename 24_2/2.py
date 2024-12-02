def is_increasing_decreasing(arr):
    if arr == sorted(arr):
        return True
    if arr[::-1] == sorted(arr):
        return True
    return False


def is_diff_1_2(arr):
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) < 1 or abs(arr[i] - arr[i + 1]) > 3:
            return False
    return True


def can_it_be_safe(arr):
    for i in range(len(arr)):
        new_arr = arr.copy()
        del new_arr[i]
        if is_increasing_decreasing(new_arr) and is_diff_1_2(new_arr):
            return True
    return False


is_safe = 0
with open("2.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        arr = [int(x) for x in line.split(" ")]
        # print(arr)
        # print(is_increasing_decreasing(arr))
        # print(is_diff_1_2(arr))
        if is_increasing_decreasing(arr) and is_diff_1_2(arr):
            is_safe += 1
        else:
            if can_it_be_safe(arr):
                is_safe += 1


print(is_safe)
