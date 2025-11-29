from src.usecase.structs.queue.queue_dynamic_array import QueueDynamicArray
from src.usecase.structs.queue.queue_linked_list import QueueLinkedList
from src.usecase.structs.queue.queue_with_stack import QueueWithStack
from src.usecase.errors.struct_errors import QueueEmptyError
from src.usecase.structs.stack.stack_linked_list import StackLinkedList
import pytest


@pytest.mark.parametrize(
    "queue",
    [
        QueueDynamicArray(),
        QueueLinkedList(),
        QueueWithStack(StackLinkedList(), StackLinkedList()),
    ],
)
def test_queue_happy_path(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.is_empty()
    assert len(queue) == 0


@pytest.mark.parametrize(
    "queue",
    [
        QueueDynamicArray(),
        QueueLinkedList(),
        QueueWithStack(StackLinkedList(), StackLinkedList()),
    ],
)
def test_queue_empty_error(queue):
    with pytest.raises(QueueEmptyError):
        queue.dequeue()
