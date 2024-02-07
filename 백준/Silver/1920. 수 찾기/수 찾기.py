from collections import Counter

def find_integers(N, A, M, query):
    counter_A = Counter(A)
    for x in query:
        if counter_A[x] > 0:
            print(1)
        else:
            print(0)

N = int(input())
A = list(map(int, input().split()))
M = int(input())
query = list(map(int, input().split()))

find_integers(N, A, M, query)