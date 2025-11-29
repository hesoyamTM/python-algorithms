from src.usecase.structs.stack.base import StackBase
from src.usecase.errors.struct_errors import ObjectIsNoneError, StackEmptyError


class StackLinkedList(StackBase):
    """
    A stack implemented using a linked list
    """

    def __init__(self) -> None:
        self.head: Node | None = None
        self.min_head: MinNode | None = None
        self.size: int = 0

    def push(self, item: int) -> None:
        """
        Pushes an value onto the stack
        :param value: The value to push
        """

        node = Node(item)

        if self.head is None:
            self.head = node
            self.min_head = MinNode(node)
        else:
            node.next = self.head
            self.head = node

            if self.min_head is None:
                raise ObjectIsNoneError("Current min is None")

            if item < self.min_head.node.value:
                new_node = MinNode(node)
                new_node.next = self.min_head
                self.min_head = new_node

        self.size += 1

    def pop(self) -> int:
        """
        Pops an value off the stack
        :return: The popped value
        """

        if self.head is None:
            raise StackEmptyError("Stack is empty")

        value = self.head.value
        self.head = self.head.next

        if self.head is None:
            self.min_head = None
        else:
            if value <= self.min():
                if self.min_head is None:
                    raise ObjectIsNoneError("Current min is None")

                self.min_head = self.min_head.next

        self.size -= 1
        return value

    def peek(self) -> int:
        """
        Peeks at the top value on the stack
        :return: The top value on the stack
        """

        if self.head is None:
            raise StackEmptyError("Stack is empty")

        return self.head.value

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty
        :return: True if the stack is empty, False otherwise
        """

        return self.head is None

    def __len__(self) -> int:
        """
        Gets the length of the stack
        :return: The length of the stack
        """

        return self.size

    def min(self) -> int:
        """
        Gets the minimum value on the stack
        :return: The minimum value on the stack
        """

        if self.head is None:
            raise StackEmptyError("Stack is empty")

        if self.min_head is None:
            raise ObjectIsNoneError("Current min is None")

        return self.min_head.node.value


class Node:
    """
    A node in a linked list
    """

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Node | None = None


class MinNode:
    """
    A node in a linked list that keeps track of the minimum value on the stack
    """

    def __init__(self, node: Node) -> None:
        self.node: Node = node
        self.next: MinNode | None = None
