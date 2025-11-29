from src.usecase.structs.queue.base import QueueBase
from src.usecase.errors.struct_errors import QueueEmptyError


class QueueLinkedList(QueueBase):
    """
    A queue implemented using a linked list
    """

    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size: int = 0

    def enqueue(self, item: int) -> None:
        """
        Enqueues an item into the queue
        :param item: The item to enqueue
        """

        node = Node(item)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            if self.tail is None:
                raise QueueEmptyError("Queue is empty")

            self.tail.next = node
            self.tail = node

        self.size += 1

    def dequeue(self) -> int:
        """
        Dequeues an item from the queue
        :return: The dequeued item
        """

        if self.head is None:
            raise QueueEmptyError("Queue is empty")

        value = self.head.value
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.size -= 1

        return value

    def front(self) -> int:
        """
        Gets the front item of the queue
        :return: The front item of the queue
        """

        if self.head is None:
            raise QueueEmptyError("Queue is empty")

        return self.head.value

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty
        :return: True if the queue is empty, False otherwise
        """

        return self.head is None

    def __len__(self) -> int:
        """
        Gets the length of the queue
        :return: The length of the queue
        """

        return self.size


class Node:
    """
    A node in a linked list
    """

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Node | None = None
