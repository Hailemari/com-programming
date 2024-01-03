class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill) - 1

        chemistry = 0
        target = skill[l] + skill[r]
        flag = True
        while l < r:
            if skill[l] + skill[r] != target:
                flag = False
                break
            else:
                chemistry += skill[l] * skill[r]

            l += 1
            r -= 1
       
        return chemistry if flag else -1