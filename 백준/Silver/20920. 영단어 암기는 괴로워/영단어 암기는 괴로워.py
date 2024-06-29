import sys
from collections import Counter

def sort_word(word_list):
    new_word_list = []
    word_cnt = Counter(word_list)
    for word, cnt in word_cnt.items():
        new_word_list.append([word, cnt, len(word)])
    
    new_word_list = sorted(new_word_list, key= lambda x: (-x[1], -x[2], x[0]))

    return new_word_list

def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    word_list = []
    for _ in range(N):
        word_list.append(sys.stdin.readline().rstrip())
    
    word_list = [word for word in word_list if len(word) >= M]

    answer = sort_word(word_list)
    for word in answer:
        print(word[0])


if __name__ == "__main__":
    main()