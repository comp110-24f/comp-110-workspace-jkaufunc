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
    """Returns the last integer in a linked list of Nodes."""
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
        x: int = max(head.next)
        if head.value > x:
            return head.value
        else:
            return max(head.next)
        # if head.next.value > output:
        #     return max(head.next)
        # else:
        #     return output


# my_node: Node = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, None))))))
# print(max(my_node))

# tricky_node: Node = Node(1, Node(3, Node(2, Node(5, None))))
# final_test_node: Node = Node(1, None)
# print(max(tricky_node))
# # print(max(None))
# print(max(final_test_node))


def linkify(input: list[int]) -> Node | None:
    """Converts a list of integers into a linked list of Nodes."""
    x: list[int] = list(input)
    if len(x) > 0:
        x.pop(0)
        return Node(input[0], linkify(x))


# test_list: list[int] = [1, 2, 3, 4, 5]
# ideal_node: Node = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
# print(linkify(test_list))


def scale(head: Node | None, factor: int) -> Node | None:
    """Multiplies all the terms in a linked list of Nodes by the inputted factor."""
    if head is None:
        raise ValueError("Cannot call scale with None.")
    elif head.next is None:
        return Node(head.value * factor, None)
    elif head.next is not None:
        return Node(head.value * factor, scale(head.next, factor))


# test_node: Node = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
# print(scale(test_node, 2))
