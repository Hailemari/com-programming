class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.capacity = k
        self.front = None
        self.rear = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = ListNode(value)
        if self.isEmpty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.front.val if self.front else -1

    def Rear(self) -> int:
        return self.rear.val if self.rear else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()