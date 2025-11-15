#!/usr/bin/env python3
"""
linked_list_guided_practice.py

Guided practice full code for Session 4 - Linked Lists.

Implements:
 - Node, LinkedList
 - insert_at_beginning, insert_at_end
 - insert_at_position, delete_by_value
 - search, count_nodes, print_list
 - reverse (in-place)
 - to_list (utility)
Includes demo / test runs at the bottom.
"""

from __future__ import annotations

from typing import Any, Optional


class Node:
    """A node in a singly linked list."""

    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Optional[Node] = None

    def __repr__(self):
        return f"Node({self.data!r})"


class LinkedList:
    """Singly linked list with common operations."""

    def __init__(self):
        self.head: Optional[Node] = None

    # ---------- Insertion ----------
    def insert_at_beginning(self, data: Any) -> None:
        """Insert new node at the head (O(1))."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data: Any) -> None:
        """Insert new node at the tail (O(n) unless tail stored)."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def insert_at_position(self, index: int, data: Any) -> None:
        """
        Insert at specified index (0-based).
        If index <= 0 => insert at beginning.
        If index >= length => insert at end.
        """
        if index <= 0 or not self.head:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        cur = self.head
        pos = 0
        # Stop at node before desired position or at last node
        while cur.next and pos < index - 1:
            cur = cur.next
            pos += 1
        # insert after cur
        new_node.next = cur.next
        cur.next = new_node

    # ---------- Deletion ----------
    def delete_by_value(self, value: Any) -> bool:
        """
        Delete first node with given value.
        Returns True if deleted, False if not found.
        """
        cur = self.head
        prev = None

        while cur:
            if cur.data == value:
                if prev is None:
                    # deleting head
                    self.head = cur.next
                else:
                    prev.next = cur.next
                return True
            prev = cur
            cur = cur.next
        return False

    # ---------- Query ----------
    def search(self, value: Any) -> bool:
        """Return True if value exists in the list."""
        cur = self.head
        while cur:
            if cur.data == value:
                return True
            cur = cur.next
        return False

    def count_nodes(self) -> int:
        """Return number of nodes."""
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def to_list(self) -> list:
        """Utility: return Python list of node data."""
        out = []
        cur = self.head
        while cur:
            out.append(cur.data)
            cur = cur.next
        return out

    # ---------- Traversal / Display ----------
    def print_list(self) -> None:
        """Nicely print the list contents."""
        cur = self.head
        parts = []
        while cur:
            parts.append(str(cur.data))
            cur = cur.next
        parts.append("None")
        print(" -> ".join(parts))

    # ---------- Reverse ----------
    def reverse(self) -> None:
        """
        Reverse the linked list in-place using three pointers.
        prev <- current <- next_node
        """
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

    # ---------- Utilities ----------
    def clear(self) -> None:
        """Clear the list."""
        self.head = None


# -----
# Demo
# -----


def demo_basic_operations():
    print("=== LinkedList: basic operations demo ===")
    ll = LinkedList()

    print("\nInsert at end: 10, 20, 30")
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.print_list()  # expected: 10 -> 20 -> 30 -> None

    print("\nInsert at beginning: 5")
    ll.insert_at_beginning(5)
    ll.print_list()  # expected: 5 -> 10 -> 20 -> 30 -> None

    print("\nInsert at position 2: 15 (0-based)")
    ll.insert_at_position(2, 15)
    ll.print_list()  # expected: 5 -> 10 -> 15 -> 20 -> 30 -> None

    print("\nSearch for 20 and 99")
    print("Found 20?", ll.search(20))  # True
    print("Found 99?", ll.search(99))  # False

    print("\nCount nodes:", ll.count_nodes())  # expected 5

    print("\nDelete value 15 (middle)")
    deleted = ll.delete_by_value(15)
    print("Deleted?", deleted)
    ll.print_list()  # expected: 5 -> 10 -> 20 -> 30 -> None

    print("\nDelete head (5)")
    ll.delete_by_value(5)
    ll.print_list()  # expected: 10 -> 20 -> 30 -> None

    print("\nDelete tail (30)")
    ll.delete_by_value(30)
    ll.print_list()  # expected: 10 -> 20 -> None


def demo_reverse():
    print("\n=== LinkedList: reverse demo ===")
    ll = LinkedList()
    for v in [1, 2, 3, 4, 5]:
        ll.insert_at_end(v)
    print("Before reverse:")
    ll.print_list()  # 1 -> 2 -> 3 -> 4 -> 5 -> None
    ll.reverse()
    print("After reverse:")
    ll.print_list()  # 5 -> 4 -> 3 -> 2 -> 1 -> None


def demo_edge_cases():
    print("\n=== LinkedList: edge cases demo ===")
    ll = LinkedList()
    print("Empty list operations:")
    ll.print_list()
    print("Delete from empty (should be False):", ll.delete_by_value(1))
    print("Search in empty (should be False):", ll.search(1))
    print("Reverse empty:")
    ll.reverse()
    ll.print_list()

    print("\nSingle element list:")
    ll.insert_at_end("only")
    ll.print_list()
    ll.reverse()
    print("After reverse single element list:")
    ll.print_list()
    print("Delete the only element (should be True):", ll.delete_by_value("only"))
    ll.print_list()


def run_all_demos():
    demo_basic_operations()
    # demo_reverse()
    # demo_edge_cases()
    # print("\nAll demos completed.")


if __name__ == "__main__":
    run_all_demos()
