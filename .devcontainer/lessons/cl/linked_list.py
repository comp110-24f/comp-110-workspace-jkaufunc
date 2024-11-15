"""Learning about linked lists/recursive functions."""

from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        self.value = val
        self.next = next

    def __str__(self) -> str:
        rest: str = ""
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


def last(head: Node) -> int:
    if head.next is None:
        return head.value
    else:
        return last(head.next)


def recursive_range(start: int, end: int) -> Node | None:
    """Creates a linked list with values from start to end using the Node class."""
    # Edge case
    if start > end:
        raise ValueError("start cannot be greater than end")
    # Base case
    if start == end:
        return None
    # Recursive case
    else:
        first: int = start
        rest: Node | None = recursive_range(start + 1, end)
        return Node(first, rest)


"""
two: Node = Node(2, None)
one: Node = Node(1, two)
print(one)
print(last(one))
"""
print(recursive_range(1, 15))
