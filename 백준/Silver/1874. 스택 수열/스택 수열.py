def find_sequence(sequence):
    stack = []
    result = []
    current_num = 1

    for num in sequence:
        while current_num <= num:
            stack.append(current_num)
            result.append('+')
            current_num += 1
        if stack[-1] == num:
            stack.pop()
            result.append('-')
        else:
            return "NO"

    return '\n'.join(result)

def main():
    n = int(input())
    sequence = [int(input()) for _ in range(n)]
    print(find_sequence(sequence))

if __name__ == "__main__":
    main()
