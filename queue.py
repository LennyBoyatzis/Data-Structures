# can only remove from the front
# can only add to the back of the queue

class Queue:
    def __init__(self):
        self.storage = [1,2,3,4,5,6,7]

    def add(self, item):
        return self.storage.append(item)

    def remove(self):
        return self.storage.pop(0)

    def peek(self):
        return self.storage[0]

    def isEmpty(self):
        return len(self.storage) == 0

if __name__ == "__main__":
    print("Hello world")
    Test = Queue()
    Test.add(9)
    print("Test", Test.storage)
    Test.remove()
    print("Test", Test.storage)
    print(Test.peek())

