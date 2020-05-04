def shipWithinDays(weights, D: int) -> int:
    
    def shipinD(cap):
        day = 0
        remain = cap
        for num in weights:
            if num > cap:
                return False
            else:
                remain = remain - num
                if remain < 0:
                    remain = cap - num
                    day += 1
            return day <= D
    
    total = sum(weights)
    left = 0
    while total > left:
        middle = (total + left) >> 1
        if shipinD(middle):
            total = middle
        else:
            left = middle -1
    return left
