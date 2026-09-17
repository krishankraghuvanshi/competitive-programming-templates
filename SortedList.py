
from bisect import bisect_left, bisect_right, insort
from typing import Generic, TypeVar, Iterator

T = TypeVar("T")


class SortedList(Generic[T]):
    def __init__(self):
        self.data: list[T] = []

    def add(self, x: T) -> None:
        insort(self.data, x)

    def remove(self, x: T) -> None:
        i = bisect_left(self.data, x)

        if i == len(self.data) or self.data[i] != x:
            raise ValueError(f"{x} not in SortedList")

        self.data.pop(i)

    def discard(self, x: T) -> None:
        i = bisect_left(self.data, x)

        if i < len(self.data) and self.data[i] == x:
            self.data.pop(i)

    def bisect_left(self, x: T) -> int:
        return bisect_left(self.data, x)

    def bisect_right(self, x: T) -> int:
        return bisect_right(self.data, x)

    def __getitem__(self, index: int) -> T:
        return self.data[index]

    def __len__(self) -> int:
        return len(self.data)

    def __contains__(self, x: T) -> bool:
        i = bisect_left(self.data, x)
        return i < len(self.data) and self.data[i] == x

    def __iter__(self) -> Iterator[T]:
        return iter(self.data)

    def __repr__(self) -> str:
        return repr(self.data)
