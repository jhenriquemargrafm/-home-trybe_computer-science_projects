class Queue:
    def __init__(self):
        self.queue = list()
        self.length = 0

    def __len__(self):
        return self.length

    def enqueue(self, value):
        self.queue.append(value)
        self.length += 1

    def dequeue(self):
        result = self.queue.pop(0)
        self.length -= 1
        return result

    def search(self, index):
        if self.length - 1 < index or index < 0:
            raise IndexError
        return self.queue[index]
