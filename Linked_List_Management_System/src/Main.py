"""
Linked List Management System
DSA mini-project implemented in Python.

The linked-list nodes and operations are implemented manually. Python's
built-in list is not used to represent either linked list.
"""

from singly_linked_list import SinglyLinkedList
from doubly_linked_list import DoublyLinkedList


def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def linked_list_menu(linked_list, kind: str) -> None:
    while True:
        print(f"\n--- {kind} Linked List ---")
        options = [
            "Insert at beginning", "Insert at end", "Insert at position",
            "Insert after a node", "Insert before a node",
            "Delete from beginning", "Delete from end", "Delete from position",
            "Delete by value", "Search", "Update", "Display",
            "Display backward" if kind == "Doubly" else None,
            "Count nodes", "Find maximum", "Find minimum", "Find middle",
            "Reverse", "Sort", "Remove duplicates", "Return to main menu"
        ]
        action_map = {}
        number = 1
        for label in options:
            if label is not None:
                print(f"{number}. {label}")
                action_map[number] = label
                number += 1

        choice = read_int("Enter choice: ")
        action = action_map.get(choice)
        if action is None:
            print("Invalid choice.")
            continue

        if action == "Return to main menu":
            return
        elif action == "Insert at beginning":
            linked_list.insert_beginning(read_int("Value: "))
        elif action == "Insert at end":
            linked_list.insert_end(read_int("Value: "))
        elif action == "Insert at position":
            linked_list.insert_position(read_int("Position (1-based): "), read_int("Value: "))
        elif action == "Insert after a node":
            linked_list.insert_after(read_int("Existing value: "), read_int("New value: "))
        elif action == "Insert before a node":
            linked_list.insert_before(read_int("Existing value: "), read_int("New value: "))
        elif action == "Delete from beginning":
            print(linked_list.delete_beginning())
        elif action == "Delete from end":
            print(linked_list.delete_end())
        elif action == "Delete from position":
            print(linked_list.delete_position(read_int("Position (1-based): ")))
        elif action == "Delete by value":
            print(linked_list.delete_value(read_int("Value to delete: ")))
        elif action == "Search":
            print(linked_list.search(read_int("Value to search: ")))
        elif action == "Update":
            print(linked_list.update(read_int("Old value: "), read_int("New value: ")))
        elif action == "Display":
            linked_list.display()
        elif action == "Display backward":
            linked_list.display_backward()
        elif action == "Count nodes":
            print(f"Node count: {linked_list.count()}")
        elif action == "Find maximum":
            print(linked_list.maximum())
        elif action == "Find minimum":
            print(linked_list.minimum())
        elif action == "Find middle":
            print(linked_list.middle())
        elif action == "Reverse":
            linked_list.reverse()
            print("List reversed.")
        elif action == "Sort":
            linked_list.sort()
            print("List sorted in ascending order.")
        elif action == "Remove duplicates":
            linked_list.remove_duplicates()
            print("Duplicate values removed.")
        print("Current list:", end=" ")
        linked_list.display()


def compare_lists() -> None:
    print("\nSingly Linked List")
    print("- Each node stores data and a next reference.")
    print("- Traversal is forward only.")
    print("- Uses less link storage per node.")
    print("\nDoubly Linked List")
    print("- Each node stores data, prev, and next references.")
    print("- Traversal is forward and backward.")
    print("- Uses extra memory for the prev reference.")
    print("\nBoth lists support dynamic insertion and deletion.")


def main() -> None:
    singly = SinglyLinkedList()
    doubly = DoublyLinkedList()
    while True:
        print("\n================================")
        print("   LINKED LIST MANAGEMENT SYSTEM")
        print("================================")
        print("1. Singly Linked List")
        print("2. Doubly Linked List")
        print("3. Compare Singly vs Doubly Linked List")
        print("4. Exit")
        choice = read_int("Enter your choice: ")
        if choice == 1:
            linked_list_menu(singly, "Singly")
        elif choice == 2:
            linked_list_menu(doubly, "Doubly")
        elif choice == 3:
            compare_lists()
        elif choice == 4:
            print("Thank you for using the Linked List Management System.")
            break
        else:
            print("Invalid choice. Select 1-4.")


if __name__ == "__main__":
    main()
