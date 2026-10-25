"""Manual singly linked list implementation."""


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def insert_end(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def insert_position(self, position, value):
        if position < 1:
            print("Invalid position.")
            return
        if position == 1:
            self.insert_beginning(value)
            return
        current = self.head
        for _ in range(position - 2):
            if current is None:
                print("Invalid position.")
                return
            current = current.next
        if current is None:
            print("Invalid position.")
            return
        node = Node(value)
        node.next = current.next
        current.next = node

    def insert_after(self, target, value):
        current = self.head
        while current and current.data != target:
            current = current.next
        if current is None:
            print(f"Value {target} not found.")
            return
        node = Node(value)
        node.next = current.next
        current.next = node

    def insert_before(self, target, value):
        if self.head is None:
            print(f"Value {target} not found.")
            return
        if self.head.data == target:
            self.insert_beginning(value)
            return
        previous, current = None, self.head
        while current and current.data != target:
            previous, current = current, current.next
        if current is None:
            print(f"Value {target} not found.")
            return
        node = Node(value)
        previous.next = node
        node.next = current

    def delete_beginning(self):
        if self.head is None:
            return "List is empty."
        value = self.head.data
        self.head = self.head.next
        return f"Deleted {value}."

    def delete_end(self):
        if self.head is None:
            return "List is empty."
        if self.head.next is None:
            value = self.head.data
            self.head = None
            return f"Deleted {value}."
        previous, current = None, self.head
        while current.next:
            previous, current = current, current.next
        previous.next = None
        return f"Deleted {current.data}."

    def delete_position(self, position):
        if position < 1 or self.head is None:
            return "Invalid position or empty list."
        if position == 1:
            return self.delete_beginning()
        previous, current = self.head, self.head.next
        index = 2
        while current and index < position:
            previous, current = current, current.next
            index += 1
        if current is None:
            return "Position out of range."
        previous.next = current.next
        return f"Deleted {current.data}."

    def delete_value(self, value):
        if self.head is None:
            return "List is empty."
        if self.head.data == value:
            return self.delete_beginning()
        previous, current = self.head, self.head.next
        while current and current.data != value:
            previous, current = current, current.next
        if current is None:
            return f"Value {value} not found."
        previous.next = current.next
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
            print(current.data, end=" -> ")
            current = current.next
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
        previous, current = None, self.head
        while current:
            following = current.next
            current.next = previous
            previous, current = current, following
        self.head = previous

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
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next
