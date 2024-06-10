def solution(x):
    def get_sum(x):
        val = 0
        while x > 0:
            val += x%10
            x = x//10
        return val
    
    def checker(x):
        val_x = get_sum(x)
        return x % val_x == 0
    
    return checker(x)