from src.usecase.structs.stack.stack_dynamic_array import StackDynamicArray
from src.usecase.structs.stack.stack_linked_list import StackLinkedList
from src.usecase.structs.stack.stack_with_queue import StackWithQueue
from src.usecase.errors.struct_errors import StackEmptyError
import pytest


def test_stack_dynamic_array():
    stack = StackDynamicArray()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty()
    assert len(stack) == 0


def test_stack_linked_list():
    stack = StackLinkedList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty()
    assert len(stack) == 0


def test_stack_with_queue():
    stack = StackWithQueue()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty()
    assert len(stack) == 0


def test_stack_dynamic_array_empty_error():
    stack = StackDynamicArray()
    with pytest.raises(StackEmptyError):
        stack.pop()


def test_stack_linked_list_empty_error():
    stack = StackLinkedList()
    with pytest.raises(StackEmptyError):
        stack.pop()


def test_stack_with_queue_empty_error():
    stack = StackWithQueue()
    with pytest.raises(StackEmptyError):
        stack.pop()


def test_stack_dynamic_array_min():
    stack = StackDynamicArray()
    stack.push(5)
    assert stack.min() == 5
    stack.push(2)
    assert stack.min() == 2
    stack.push(3)
    assert stack.min() == 2
    stack.push(4)
    assert stack.min() == 2
    stack.push(5)
    assert stack.min() == 2
    for _ in range(4):
        stack.pop()
    assert stack.min() == 5


def test_stack_linked_list_min():
    stack = StackLinkedList()
    stack.push(5)
    assert stack.min() == 5
    stack.push(2)
    assert stack.min() == 2
    stack.push(3)
    assert stack.min() == 2
    stack.push(4)
    assert stack.min() == 2
    stack.push(5)
    assert stack.min() == 2
    for _ in range(4):
        stack.pop()

    assert stack.min() == 5


def test_stack_with_queue_min():
    stack = StackWithQueue()
    stack.push(5)
    assert stack.min() == 5
    stack.push(2)
    assert stack.min() == 2
    stack.push(3)
    assert stack.min() == 2
    stack.push(4)
    assert stack.min() == 2
    stack.push(5)
    assert stack.min() == 2
    for _ in range(4):
        stack.pop()

    assert stack.min() == 5
