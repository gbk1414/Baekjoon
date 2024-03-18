def hanoi_recursive(N, start, end):
    if N == 1:
        return [[start, end]]
    else:
        moves = hanoi_recursive(N - 1, start, 6 - start - end)
        moves.append([start, end])
        moves.extend(hanoi_recursive(N - 1, 6 - start - end, end))
        return moves

def hanoi(N) -> list[list[int]]:
    return hanoi_recursive(N, 1, 3)

def main():
    N = int(input())
    answer = hanoi(N)
    print(len(answer))
    for move in answer:
        print("{} {}".format(move[0], move[1]))

if __name__ == "__main__":
    main()
