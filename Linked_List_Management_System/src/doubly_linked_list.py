"""Manual doubly linked list implementation."""


class Node:
    def __init__(self, data: int):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insert_end(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def _node_at(self, position):
        if position < 1:
            return None
        current, index = self.head, 1
        while current and index < position:
            current, index = current.next, index + 1
        return current

    def insert_position(self, position, value):
        if position < 1:
            print("Invalid position.")
        elif position == 1:
            self.insert_beginning(value)
        elif position == self.count() + 1:
            self.insert_end(value)
        else:
            target = self._node_at(position)
            if target is None:
                print("Invalid position.")
                return
            node = Node(value)
            node.prev = target.prev
            node.next = target
            target.prev.next = node
            target.prev = node

    def insert_after(self, target_value, value):
        current = self.head
        while current and current.data != target_value:
            current = current.next
        if current is None:
            print(f"Value {target_value} not found.")
            return
        if current is self.tail:
            self.insert_end(value)
            return
        node = Node(value)
        node.prev, node.next = current, current.next
        current.next.prev = node
        current.next = node

    def insert_before(self, target_value, value):
        current = self.head
        while current and current.data != target_value:
            current = current.next
        if current is None:
            print(f"Value {target_value} not found.")
            return
        if current is self.head:
            self.insert_beginning(value)
            return
        node = Node(value)
        node.prev, node.next = current.prev, current
        current.prev.next = node
        current.prev = node

    def delete_beginning(self):
        if self.head is None:
            return "List is empty."
        value = self.head.data
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return f"Deleted {value}."

    def delete_end(self):
        if self.tail is None:
            return "List is empty."
        value = self.tail.data
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return f"Deleted {value}."

    def delete_position(self, position):
        node = self._node_at(position)
        if node is None:
            return "Invalid position or position out of range."
        if node is self.head:
            return self.delete_beginning()
        if node is self.tail:
            return self.delete_end()
        node.prev.next = node.next
        node.next.prev = node.prev
        return f"Deleted {node.data}."

    def delete_value(self, value):
        current = self.head
        while current and current.data != value:
            current = current.next
        if current is None:
            return f"Value {value} not found."
        if current is self.head:
            return self.delete_beginning()
        if current is self.tail:
            return self.delete_end()
        current.prev.next = current.next
        current.next.prev = current.prev
        return f"Deleted {value}."

    def search(self, value):
        current, position = self.head, 1
        while current:
            if current.data == value:
                return f"Value {value} found at position {position}."
            current, position = current.next, position + 1
        return f"Value {value} not found."

    def update(self, old_value, new_value):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
                return f"Updated {old_value} to {new_value}."
            current = current.next
        return f"Value {old_value} not found."

    def display(self):
        if self.head is None:
            print("NULL (empty)")
            return
        current = self.head
        while current:
            print(current.data, end=" <-> " if current.next else " ")
            current = current.next
        print("<-> NULL")

    def display_backward(self):
        if self.tail is None:
            print("NULL (empty)")
            return
        current = self.tail
        print("NULL <-", end=" ")
        while current:
            print(current.data, end=" <- " if current.prev else " ")
            current = current.prev
        print("NULL")

    def count(self):
        total, current = 0, self.head
        while current:
            total += 1
            current = current.next
        return total

    def maximum(self):
        if self.head is None:
            return "List is empty."
        result, current = self.head.data, self.head.next
        while current:
            result = max(result, current.data)
            current = current.next
        return f"Maximum: {result}"

    def minimum(self):
        if self.head is None:
            return "List is empty."
        result, current = self.head.data, self.head.next
        while current:
            result = min(result, current.data)
            current = current.next
        return f"Minimum: {result}"

    def middle(self):
        if self.head is None:
            return "List is empty."
        slow = fast = self.head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return f"Middle element: {slow.data} (second middle for even length)."

    def reverse(self):
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.head, self.tail = self.tail, self.head

    def sort(self):
        if self.head is None:
            return
        changed = True
        while changed:
            changed = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    changed = True
                current = current.next

    def remove_duplicates(self):
        current = self.head
        while current:
            runner = current.next
            while runner:
                if runner.data == current.data:
                    following = runner.next
                    if runner.prev:
                        runner.prev.next = runner.next
                    if runner.next:
                        runner.next.prev = runner.prev
                    if runner is self.tail:
                        self.tail = runner.prev
                    runner = following
                else:
                    runner = runner.next
            current = current.next
