from typing import Any, Optional


class Node:
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Optional[Node] = None

    def __repr__(self):
        return f"Node({self.data!r})"


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def insert_at_beginning(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current))
            current = current.next
        return " -> ".join(nodes)

    def count_nodes(self) -> int:
        """Return number of nodes."""
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def reverse(self) -> None:
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insert_at_position(self, index: int, data: Any) -> None:
        if index <= 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        pos = 0
        while current and pos < index - 1:
            current = current.next
            pos += 1
        if not current:
            self.insert_at_end(data)
        else:
            new_node.next = current.next
            current.next = new_node

    def insert_at_end(self, data: Any) -> None:
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


class DNode:
    def __init__(self, data: Any):
        self.data = data
        self.prev = None
        self.next = None


linked_list = LinkedList()
linked_list.insert_at_beginning(10)
linked_list.insert_at_beginning(20)
linked_list.insert_at_beginning(30)


print(linked_list)


linked_list.reverse()
print("Reversed List:")
print(linked_list)


linked_list.insert_at_position(1, 25)
print("\nAfter Inserting 25 at Position 1:")
print(linked_list)


print("\nNode count:", linked_list.count_nodes())
