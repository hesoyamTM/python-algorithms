from typing import Protocol


class QueueBase(Protocol):
    """
    Queue interface
    """

    def enqueue(self, item: int) -> None:
        """
        Enqueue an item to the queue
        """
        ...

    def dequeue(self) -> int:
        """
        Dequeue an item from the queue
        """
        ...

    def front(self) -> int:
        """
        Get the front item of the queue
        """
        ...

    def is_empty(self) -> bool:
        """
        Check if the queue is empty
        """
        ...

    def __len__(self) -> int:
        """
        Get the size of the queue
        """
        ...
