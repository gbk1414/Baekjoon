def solution(friends, gifts):
    gifted = {friend: {} for friend in friends}
    gift_index = {friend: 0 for friend in friends}

    for gift in gifts:
        giver, receiver = gift.split()
        if receiver in gifted[giver]:
            gifted[giver][receiver] += 1
        else:
            gifted[giver][receiver] = 1
        gift_index[giver] += 1
        gift_index[receiver] -= 1

    will_get = [0] * len(friends)
    for i, curr_friend in enumerate(friends):
        for j in range(i + 1, len(friends)):
            next_friend = friends[j]
            gifts_to_next = gifted[curr_friend].get(next_friend, 0)
            gifts_from_next = gifted[next_friend].get(curr_friend, 0)

            if gifts_to_next > gifts_from_next:
                will_get[i] += 1
            elif gifts_to_next < gifts_from_next:
                will_get[j] += 1
            else:
                if gift_index[curr_friend] > gift_index[next_friend]:
                    will_get[i] += 1
                elif gift_index[curr_friend] < gift_index[next_friend]:
                    will_get[j] += 1

    return max(will_get)
