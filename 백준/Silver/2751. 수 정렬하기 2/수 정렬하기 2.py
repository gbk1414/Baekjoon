from sys import stdin, setrecursionlimit
input = stdin.readline

def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(arr, minsize):
    size = minsize
    while size < len(arr):
        for left in range(0, len(arr), 2*size):
            mid = min(len(arr), left + size)
            right = min(len(arr), left + 2*size)
            arr[left:right] = merge(arr[left:mid], arr[mid:right])
        size *= 2
    return arr


def main():
    N = int(input())
    array = []
    for i in range(N):
        array.append(int(input()))
    for e in merge_sort(array, 1):
        print(e)


if __name__ == "__main__":
    main()
