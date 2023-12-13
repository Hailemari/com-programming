class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * (n + 1)  # Initialize an array to store the stream
        self.ptr = 1  # Pointer to the next available position in the stream
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value   # Insert the chunk at the specified ID
        result = []

        # Iterate from the current pointer to find consecutive chunks
        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            result.append(self.stream[self.ptr])
            self.ptr += 1

        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)