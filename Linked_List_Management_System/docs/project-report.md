# Project Report: Linked List Management System

## 1. Introduction
This console-based DSA mini-project demonstrates the implementation and use of singly and doubly linked lists in Python.

## 2. Objective
To implement common linked-list operations manually, understand node links, and compare singly and doubly linked lists.

## 3. Data Structure Design
### Singly Linked List
Each node stores an integer value and a `next` reference. The list is accessed through `head`.

### Doubly Linked List
Each node stores an integer value, a `prev` reference, and a `next` reference. The implementation maintains both `head` and `tail`.

## 4. Operations
Both implementations provide insertion at the beginning/end/position and before/after a target value; deletion at the beginning/end/position and by value; search; update; display; count; minimum; maximum; middle; reverse; sort; and duplicate removal. The doubly linked list additionally displays in reverse order.

## 5. Complexity
Most traversals take O(n). Insertion at the beginning and deletion at the beginning take O(1). Bubble sort and the simple duplicate-removal algorithm take O(n²). Singly linked-list insertion at the end takes O(n) because there is no tail reference.

## 6. Testing
Test empty and one-node lists, valid and invalid positions, values that are absent, duplicate values, zero and negative values, and sorting/reversing empty and one-node lists.

## 7. Conclusion
The project demonstrates how nodes and references can implement linked lists without using Python's built-in list as the underlying data structure.
