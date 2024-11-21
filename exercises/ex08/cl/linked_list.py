"""Learning about linked lists/recursive functions."""

from __future__ import annotations

__author__ = "730761420"


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

print(recursive_range(1, 15))
"""


def value_at(head: Node | None, index: int) -> int:
    """Returns the value of the Node at the given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.value
    elif index < 0:
        raise IndexError("Index is out of bounds on the list.")
    else:
        if index > 0:
            return value_at(head.next, index - 1)
        else:
            return head.value


# my_node: Node = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, None))))))
# print(value_at(my_node, 0))


def max(head: Node | None) -> int:
    """Returns the maximum value in the linked list."""

    if head is None:
        raise ValueError("Cannot call max with None.")
    elif head.next is None:
        return head.value
    else:
        output: int = head.value
        if head.next.value > output:
            return max(head.next)
        else:
            return output


my_node: Node = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, None))))))
print(max(my_node))

tricky_node: Node = Node(1, Node(3, Node(2, Node(5, None))))
print(max(tricky_node))
