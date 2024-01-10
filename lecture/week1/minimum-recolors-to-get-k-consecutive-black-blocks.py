class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        recolors = 0

        window = blocks[:k]
        recolors = window.count("W")

        curr = recolors
        for right in range(k, len(blocks)):
            if blocks[right - k] == "W":
                curr -= 1
            if blocks[right] == "W":
                curr += 1
            recolors = min(recolors, curr)

        return recolors