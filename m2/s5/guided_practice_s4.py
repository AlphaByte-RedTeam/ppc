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


linked_list = LinkedList()

linked_list.insert_at_beginning(10)
linked_list.insert_at_beginning(20)
linked_list.insert_at_beginning(30)

print(linked_list)


print(linked_list.count_nodes())
