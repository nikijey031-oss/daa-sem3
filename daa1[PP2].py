import random


def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= key <= arr[high]:
        comparisons += 1

        if arr[high] == arr[low]:
            if arr[low] == key:
                return low, comparisons
            break

        pos = low + int(
            ((key - arr[low]) * (high - low))
            / (arr[high] - arr[low])
        )

        pos = max(low, min(pos, high))

        if abs(arr[pos] - key) < 1e-9:
            return pos, comparisons
        elif arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1

    return -1, comparisons


sizes = [10000, 50000, 100000]

for size in sizes:
    arr = sorted(random.uniform(0.0, 1000.0) for _ in range(size))

    # Choose an existing element so search is successful
    key = arr[random.randint(0, size - 1)]

    index, comparisons = interpolation_search(arr, key)

    print(f"Dataset Size: {size}")
    print(f"Element Found at Index: {index}")
    print(f"Number of Comparisons: {comparisons}")
    print("-" * 40)

OUTPUT:

Dataset Size: 10000
Element Found at Index: 8049
Number of Comparisons: 3
----------------------------------------
Dataset Size: 50000
Element Found at Index: 15702
Number of Comparisons: 4
----------------------------------------
Dataset Size: 100000
Element Found at Index: 4643
Number of Comparisons: 4
----------------------------------------
