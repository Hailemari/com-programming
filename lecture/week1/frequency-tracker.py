class FrequencyTracker:
    def __init__(self):
        self.value_frequency = {}
        self.frequency_count = {}

    def add(self, number: int) -> None:
        if number in self.value_frequency:
            old_frequency = self.value_frequency[number]
            self.frequency_count[old_frequency] -= 1
            if self.frequency_count[old_frequency] == 0:
                del self.frequency_count[old_frequency]

            self.value_frequency[number] += 1
            new_frequency = self.value_frequency[number]
            if new_frequency in self.frequency_count:
                self.frequency_count[new_frequency] += 1
            else:
                self.frequency_count[new_frequency] = 1
        else:
            self.value_frequency[number] = 1
            if 1 in self.frequency_count:
                self.frequency_count[1] += 1
            else:
                self.frequency_count[1] = 1

    def deleteOne(self, number: int) -> None:
        if number in self.value_frequency:
            old_frequency = self.value_frequency[number]
            self.frequency_count[old_frequency] -= 1
            if self.frequency_count[old_frequency] == 0:
                del self.frequency_count[old_frequency]

            if old_frequency > 1:
                self.value_frequency[number] -= 1
                new_frequency = self.value_frequency[number]
                if new_frequency in self.frequency_count:
                    self.frequency_count[new_frequency] += 1
                else:
                    self.frequency_count[new_frequency] = 1
            else:
                del self.value_frequency[number]

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.frequency_count and self.frequency_count[frequency] > 0

