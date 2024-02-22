from sys import stdin
input = stdin.readline


def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(arr, min_size):
    while min_size < len(arr):
        for left in range(0, len(arr), 2*min_size):
            mid = min(len(arr), left+min_size)
            right = min(len(arr), left + 2*min_size)
            arr[left:right] = merge(arr[left:mid], arr[mid:right])
        min_size *= 2
    return arr


def main():
    N = int(input())
    array = []
    for _ in range(N):
        age, name = input().split()
        array.append([int(age), name])

    for e in merge_sort(array, 1):
        print("{} {}".format(e[0], e[1]))


if __name__ == "__main__":
    main()
