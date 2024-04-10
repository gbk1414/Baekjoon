def calc_LIS_length(num_array):
    answer = [num_array[0]]
    for i in num_array:
        if answer[-1] < i:
            answer.append(i)
        else:
            position = find_postion_by_binary(answer, i)
            answer[position] = i

    return len(answer)


def find_postion_by_binary(answer_array, target):
    left = 0
    right = len(answer_array)
    while left <= right:
        mid = (left + right)//2
        if answer_array[mid] == target:
            return mid
        elif answer_array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


def main():
    N = int(input())
    num_array = list(map(int, input().split()))

    print(calc_LIS_length(num_array))


if __name__ == "__main__":
    main()
