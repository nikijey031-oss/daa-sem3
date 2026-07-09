def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1
    probes = 0

    while low <= high and arr[low] <= key <= arr[high]:
        probes += 1

        if arr[low] == arr[high]:
            if arr[low] == key:
                return low, probes
            break

        pos = low + ((key - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == key:
            return pos, probes
        elif arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1

    return -1, probes


def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    probes = 0

    while low <= high:
        mid = (low + high) // 2
        probes += 1

        if arr[mid] == key:
            return mid, probes
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1, probes


# Input sorted roll numbers
n = int(input("Enter number of students: "))

print("Enter sorted roll numbers:")
roll_numbers = list(map(int, input().split()))

if len(roll_numbers) != n:
    print("Error: Number of roll numbers does not match n.")
else:
    key = int(input("Enter roll number to search: "))

    i_index, i_probes = interpolation_search(roll_numbers, key)
    b_index, b_probes = binary_search(roll_numbers, key)

    print("\nInterpolation Search:")
    if i_index != -1:
        print("Roll number found at index", i_index)
    else:
        print("Roll number not found")
    print("Number of probes =", i_probes)

    print("\nBinary Search:")
    if b_index != -1:
        print("Roll number found at index", b_index)
    else:
        print("Roll number not found")
    print("Number of probes =", b_probes)