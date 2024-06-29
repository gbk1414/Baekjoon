from collections import deque

def change_card(card_list:deque):
    card_list.pop()
    first_card = card_list.pop()
    card_list.appendleft(first_card)
    return card_list

def main():
    N = int(input())
    card_list = deque([i for i in range(N, 0,-1)])
    while len(card_list) > 1:
        card_list = change_card(card_list)
    
    print(card_list[0])

if __name__ == "__main__":
    main()