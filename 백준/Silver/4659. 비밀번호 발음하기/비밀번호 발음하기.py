alpha_list = ["a","e","i","o","u"]

def first_checker(password):
    flag = False
    for alpha in alpha_list:
        if alpha in password:
            flag = True
    return flag

def second_checker(password):
    flag = True
    for i in range(0, len(password)-2):
        if password[i] in alpha_list and password[i+1] in alpha_list and password[i+2] in alpha_list:
            flag = False
        elif password[i] not in alpha_list and password[i+1] not in alpha_list and password[i+2] not in alpha_list:
            flag = False
    return flag

def third_checker(password):
    flag = True
    for i in range(0, len(password)-1):
        if password[i] == password[i+1]:
            if password[i] != "e" and password[i] != "o":
                flag = False
    return flag

word = input()
while word != "end":
    if first_checker(word) and second_checker(word) and third_checker(word):
        print("<" + word + "> is acceptable.")
    else:
        print("<" + word + "> is not acceptable.")
    word = input()