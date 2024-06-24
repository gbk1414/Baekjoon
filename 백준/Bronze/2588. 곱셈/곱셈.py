N1 = int(input())
N2 = int(input())
new_N2 = N2
while new_N2 > 0:
    print(N1*(new_N2%10))
    new_N2 = new_N2//10
print(N1*N2)