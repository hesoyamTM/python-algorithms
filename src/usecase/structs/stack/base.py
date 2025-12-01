from typing import Protocol


class StackBase(Protocol):
    """
    Stack interface
    """

    def push(self, item: int) -> None:
        """
        Push an item to the stack
        """
        ...

    def pop(self) -> int:
        """
        Pop an item from the stack
        """
        ...

    def peek(self) -> int:
        """
        Peek at the top of the stack
        """
        ...

    def is_empty(self) -> bool:
        """
        Check if the stack is empty
        """
        ...

    def __len__(self) -> int:
        """
        Get the size of the stack
        """
        ...

    def min(self) -> int:
        """
        Get the minimum value in the stack
        """
        ...
