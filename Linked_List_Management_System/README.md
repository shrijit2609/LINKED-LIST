# Linked List Management System

A menu-driven Data Structures and Algorithms mini-project implemented in **Python 3**.

## Objective
Demonstrate linked-list operations by implementing a singly linked list and a doubly linked list using manually created nodes and references.

## Language Used
Python 3. No C++ or Java code is included.

## Features

### Singly Linked List
- Insert at beginning, end, position, before a value, and after a value
- Delete from beginning, end, position, and by value
- Search, update, display, count nodes
- Find maximum, minimum, and middle element
- Reverse, sort ascending, remove duplicates

### Doubly Linked List
- All the operations above
- Display forward and backward

### Other
- Main menu to select list type
- Singly vs doubly linked list comparison
- Input validation and messages for empty lists, missing values, and invalid positions

## Project Structure
```text
Linked-List-Management-System/
├── README.md
├── .gitignore
├── src/
│   ├── Main.py
│   ├── singly_linked_list.py
│   └── doubly_linked_list.py
├── sample-output/
│   └── output.txt
└── docs/
    └── project-report.md
```

## How to Run

Requires Python 3.10 or later (Python 3.8+ should also work).

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python src/Main.py
```

On some systems, use `python3 src/Main.py` instead.

The source files are in the same `src` folder, so the imports work when launching `Main.py` using the command above.

## Sample Output
```text
================================
   LINKED LIST MANAGEMENT SYSTEM
================================
1. Singly Linked List
2. Doubly Linked List
3. Compare Singly vs Doubly Linked List
4. Exit
Enter your choice: 1

--- Singly Linked List ---
1. Insert at beginning
2. Insert at end
...
```

A short illustrative transcript is in `sample-output/output.txt`.

## Design Notes
- Singly linked nodes store `data` and `next`.
- Doubly linked nodes store `data`, `prev`, and `next`.
- Positions are 1-based.
- Insert-before, insert-after, delete-by-value, search, and update act on the first matching value.
- For even-length lists, `middle()` returns the second middle node.
- Sorting uses Bubble Sort by swapping node data.
- Duplicate removal keeps the first occurrence of each value.
- Built-in Python lists are not used to implement the linked-list data structures.

## Typical Time Complexity
| Operation | Typical complexity |
|---|---:|
| Insert at beginning | O(1) |
| Insert at end (singly list without tail) | O(n) |
| Insert at position | O(n) |
| Delete from beginning | O(1) |
| Delete from end (singly list) | O(n) |
| Search / display / count | O(n) |
| Find minimum / maximum / middle | O(n) |
| Reverse | O(n), O(1) extra space |
| Bubble Sort | O(n²) |
| Simple duplicate removal | O(n²) |

## Testing
Try empty lists, one-node lists, first/last positions, invalid positions, absent values, duplicates, zero/negative values, sorting and reversing empty/single-node lists.

## Author
Add your name, roll number, class/section, and faculty details here before submission.
