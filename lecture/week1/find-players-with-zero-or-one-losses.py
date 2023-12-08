class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers_count = set(), {}

        # Count the number of losses for each player
        for winner, loser in matches:
            winners.add(winner)
            losers_count[loser] = losers_count.get(loser, 0) + 1

        no_losses = [player for player in winners if player not in losers_count]
        one_loss = [player for player, count in losers_count.items() if count == 1]

        no_losses.sort()
        one_loss.sort()

        return [no_losses, one_loss] 

        
        