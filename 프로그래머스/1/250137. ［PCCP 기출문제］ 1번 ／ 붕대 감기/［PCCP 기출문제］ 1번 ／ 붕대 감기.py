def solution(bandage, health, attacks):
    t, x, y = bandage
    current_health = health
    current_time = 0
    consecutive_time = 0

    for attack_time, damage in attacks:
        while current_time < attack_time:
            current_health += x
            if current_health > health:
                current_health = health
            
            consecutive_time += 1
            current_time += 1

            if consecutive_time == t:
                current_health += y
                if current_health > health:
                    current_health = health
                consecutive_time = 0
        
        if current_time == attack_time:
            current_health -= damage
            if current_health <= 0:
                return -1
            consecutive_time = 0
            current_time += 1

    while consecutive_time > 0 and consecutive_time < t:
        current_health += x
        if current_health > health:
            current_health = health
        consecutive_time += 1
        current_time += 1

        if consecutive_time == t:
            current_health += y
            if current_health > health:
                current_health = health
            consecutive_time = 0
    
    return current_health