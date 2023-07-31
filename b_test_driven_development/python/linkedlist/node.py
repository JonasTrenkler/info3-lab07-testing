from typing import Self


class Node:
    data: str
    next: Self

    def __init__(self, data: str, next: Self = None):
        self.data = data
        self.next = next

    def from_str(string: str) -> Self:
        split: list = [s.strip() for s in string.split(",")]
        root: Node = Node(split.pop(0))
        curr: Node = root

        for data in split:
            curr.next = Node(data)
            curr = curr.next

        return root

    def last(self) -> Self:
        curr = self

        while curr.next is not None:
            curr = curr.next

        return curr

    def append(self, data: str):
        self.last().next = Node(data)

    def delete(self, data: str) -> Self:
        if self.data == data:
            return self.next
        else:
            root = self
            last = root
            curr = root.next

            while curr is not None:
                if curr.data == data:
                    last.next = curr.next
                last = curr
                curr = curr.next

            return root

    def reverse(self) -> Self:
        new = self.shallow_copy()
        prev = new
        curr: Node = self.next

        while curr is not None:
            new = curr.shallow_copy()
            new.next = prev
            prev = new
            curr = curr.next

        return new

    def copy(self) -> Self:
        # This solution works but is boring:
        # from copy import copy
        # return copy(self)

        copy = self.shallow_copy()
        curr = self.next

        while curr is not None:
            copy.append(curr.data)
            curr = curr.next

        return copy

    def shallow_copy(self) -> Self:
        return Node(self.data)

    def __len__(self) -> int:
        curr = self
        count: int = 1

        while curr.next is not None:
            count += 1
            curr = curr.next

        return count

    def __str__(self) -> str:
        text: str = self.data
        curr = self.next

        while curr is not None:
            text += f", {curr.data}"
            curr = curr.next

        return text

    def __iter__(self):
        curr = self

        while curr is not None:
            yield curr.data
            curr = curr.next
