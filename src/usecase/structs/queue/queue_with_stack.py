from src.usecase.structs.stack.base import StackBase
from src.usecase.structs.queue.base import QueueBase
from src.usecase.errors.struct_errors import QueueEmptyError


class QueueWithStack(QueueBase):
    """
    A queue implemented using a two stacks
    """

    def __init__(self, stack1: StackBase, stack2: StackBase) -> None:
        self.stack1: StackBase = stack1
        self.stack2: StackBase = stack2

    def enqueue(self, item: int) -> None:
        """
        Enqueues an item into the queue
        :param item: The item to enqueue
        """

        self.stack1.push(item)

    def dequeue(self) -> int:
        """
        Dequeues an item from the queue
        :return: The dequeued item
        """

        if self.is_empty():
            raise QueueEmptyError("Queue is empty")

        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        return self.stack2.pop()

    def front(self) -> int:
        """
        Gets the front item of the queue
        :return: The front item of the queue
        """

        if self.is_empty():
            raise QueueEmptyError("Queue is empty")

        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        return self.stack2.peek()

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty
        :return: True if the queue is empty, False otherwise
        """

        return self.stack1.is_empty() and self.stack2.is_empty()

    def __len__(self) -> int:
        """
        Gets the length of the queue
        :return: The length of the queue
        """

        return len(self.stack1) + len(self.stack2)


if __name__ == "__main__":
    from src.usecase.structs.stack.stack_linked_list import StackLinkedList

    queue = QueueWithStack(StackLinkedList(), StackLinkedList())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.front())
    print(queue.is_empty())
    print(len(queue))
    print(queue.dequeue())
