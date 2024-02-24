def maximum_budget(nums: list[int], M: int) -> int:
    nums.sort()
    if nums[0] >= M//len(nums):
        return M//len(nums)
    start, end = nums[0], nums[-1]
        
    
    while start <= end:
        mid = (start + end) // 2

        total_val = sum(min(num, mid) for num in nums)

        if total_val > M:
            end = mid - 1
        else:
            start = mid + 1

    return end


def main():
    N = int(input())
    nums = list(map(int, input().split()))
    M = int(input())

    print(maximum_budget(nums, M))


if __name__ == "__main__":
    main()
