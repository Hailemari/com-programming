class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = defaultdict(int)

        for bill in bills:
            if bill == 5:
                changes[bill] += 1
            elif bill == 10:
                five = changes[5]
                if five:
                    changes[5] -= 1
                else:
                    return False
                changes[bill] += 1
            else:
                fives = changes[5]
                tens = changes[10]
                
                if tens and fives:
                    changes[10] -= 1
                    changes[5] -= 1
                elif fives and fives >= 3:
                    changes[5] -= 3
                else:
                    return False
        return True