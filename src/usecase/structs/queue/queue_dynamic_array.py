from src.usecase.structs.queue.base import QueueBase
from src.usecase.errors.struct_errors import QueueEmptyError


class QueueDynamicArray(QueueBase):
    """
    A queue implemented using a dynamic array
    """

    def __init__(self) -> None:
        self.items: list[int] = []
        self.head: int = 0
        self.tail: int = -1

    def enqueue(self, item: int) -> None:
        """
        Enqueues an item into the queue
        :param item: The item to enqueue
        """

        self.items.append(item)
        self.tail += 1

    def dequeue(self) -> int:
        """
        Dequeues an item from the queue
        :return: The dequeued item
        """

        print(self.head, self.tail, len(self.items))

        if self.head > self.tail:
            raise QueueEmptyError("Queue is empty")

        value = self.items[self.head]
        self.items[self.head] = 0
        self.head += 1

        if len(self.items) > len(self) * 2:
            self._free()
        if self.head == self.tail + 1:
            self.head = 0
            self.tail = -1
            self.items = []

        return value

    def front(self) -> int:
        """
        Gets the front item of the queue
        :return: The front item of the queue
        """

        if self.head == self.tail:
            raise QueueEmptyError("Queue is empty")

        return self.items[self.head]

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty
        :return: True if the queue is empty, False otherwise
        """

        return self.head == self.tail + 1

    def __len__(self) -> int:
        """
        Gets the length of the queue
        :return: The length of the queue
        """

        return self.tail - self.head + 1

    def _free(self) -> None:
        new_arr = [0] * (self.tail - self.head + 1)

        for i in range(len(new_arr)):
            new_arr[i] = self.items[self.head + i]

        self.head = 0
        self.tail = len(new_arr) - 1

        self.items = new_arr
