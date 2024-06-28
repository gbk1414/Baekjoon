switch_cnt = int(input())
switch = list(map(int, input().split()))

def male_switch(selected_switch):
    for i in range(selected_switch - 1, switch_cnt, selected_switch):
        switch[i] = 1 - switch[i]
    return 

def female_switch(selected_switch):
    switch[selected_switch-1] = 1 - switch[selected_switch-1]
    left, right = selected_switch-2, selected_switch
    while left >= 0 and right < switch_cnt and switch[left] == switch[right]:
        switch[left] = 1 - switch[left]
        switch[right] = 1 - switch[right]
        left -= 1
        right += 1
    return

student_num = int(input())

for _ in range(student_num):
    gender, selected_switch = map(int, input().split())
    if gender == 1:
        male_switch(selected_switch)
    else:
        female_switch(selected_switch)

for i in range(0, switch_cnt, 20):
    print(' '.join(map(str, switch[i:i+20])))