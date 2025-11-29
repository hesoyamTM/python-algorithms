from src.usecase.structs.stack.base import StackBase
from src.usecase.errors.struct_errors import StackEmptyError


class StackWithQueue(StackBase):
    """
    A stack implemented using a queue
    """

    def __init__(self) -> None:
        self.queue: list[int] = []
        self.mins: list[int] = []

    def push(self, item: int) -> None:
        """
        Pushes an item onto the stack
        :param item: The item to push
        """

        self.queue.append(item)

        if len(self.queue) == 1:
            self.mins.append(item)
        else:
            self.mins.append(min(item, self.mins[-1]))

    def pop(self) -> int:
        """
        Pops an item off the stack
        :return: The popped item
        """

        if len(self.queue) == 0:
            raise StackEmptyError("Stack is empty")

        for _ in range(len(self) - 1):
            self.queue.append(self.queue.pop(0))

        self.mins.pop()

        return self.queue.pop(0)

    def peek(self) -> int:
        """
        Peeks at the top item on the stack
        :return: The top item on the stack
        """

        if len(self.queue) == 0:
            raise StackEmptyError("Stack is empty")

        return self.queue[-1]

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty
        :return: True if the stack is empty, False otherwise
        """

        return len(self.queue) == 0

    def __len__(self) -> int:
        """
        Gets the length of the stack
        :return: The length of the stack
        """

        return len(self.queue)

    def min(self) -> int:
        """
        Gets the minimum item on the stack
        :return: The minimum item on the stack
        """

        return self.mins[-1]
