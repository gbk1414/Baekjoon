def is_valid_parenthesis(s: str) -> str:
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return "NO"
            stack.pop()

    return "YES" if not stack else "NO"

if __name__ == "__main__":
    T = int(input())  # Read the number of test cases

    for _ in range(T):
        s = input()  # Read the parentheses string for each test case
        result = is_valid_parenthesis(s)
        print(result)
