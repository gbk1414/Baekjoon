def hansu_checker(n):
    if n < 100:
        return True
    before_num = n%10
    n = n//10
    current_num = n%10
    difference = current_num - before_num
    n = n//10
    while n>0:
        before_num = current_num
        current_num = n%10
        if current_num - before_num != difference:
            return False
        n = n//10
    return True


n = int(input())
cnt = 0
for i in range(1,n+1):
    if hansu_checker(i):
        cnt += 1
        
print(cnt)