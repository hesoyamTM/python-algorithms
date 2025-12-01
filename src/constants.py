from typing import TypeVar, Protocol, Any


class Comparable(Protocol):
    """
    Comparable protocol
    """

    def __lt__(self, other: Any) -> bool: ...

    def __gt__(self, other: Any) -> bool: ...

    def __le__(self, other: Any) -> bool: ...

    def __ge__(self, other: Any) -> bool: ...


T = TypeVar("T")
C = TypeVar("C", bound=Comparable)
