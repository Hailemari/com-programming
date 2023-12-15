class ATM:

    def __init__(self):
        self.banknotes = [0, 0, 0, 0, 0]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.banknotes[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        withdrawn_banknotes = [0, 0, 0, 0, 0]
        remaining_amount = amount

        for i in range(4, -1, -1):
            banknote_value = [20, 50, 100, 200, 500][i]
            banknotes_to_withdraw = min(self.banknotes[i], remaining_amount // banknote_value)
            withdrawn_banknotes[i] = banknotes_to_withdraw
            remaining_amount -= banknotes_to_withdraw * banknote_value

        if remaining_amount == 0:
            for i in range(5):
                self.banknotes[i] -= withdrawn_banknotes[i]
            return withdrawn_banknotes
        else:
            return [-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)