# Lab Report

## Student Information

**Name:** Ahmed Ajlal
**Date:** 03/09/2026
**Course:** COSC 2436

## Algorithm Analysis

### Binary Search Tree

* **Search Time, Balanced BST:** O(log n)
* **Search Time, Unbalanced BST:** O(n)
* **BST Property:** A binary search tree keeps values organized so that, for each node, all values in the left subtree are smaller and all values in the right subtree are greater. This structure helps make searching efficient when the tree is balanced.

A balanced binary search tree can search quickly because each comparison removes about half of the remaining tree from consideration. However, if the tree becomes unbalanced, searching can become much slower because the tree may act more like a linked list.

## Traversals

| Traversal | Order             | Use Case                |
| --------- | ----------------- | ----------------------- |
| Preorder  | Root, Left, Right | Copying a tree          |
| Inorder   | Left, Root, Right | Getting sorted elements |
| Postorder | Left, Right, Root | Deleting a tree         |

## Reflection Questions

### 1. Why does inorder traversal give sorted output?

Inorder traversal gives sorted output in a binary search tree because it visits the left subtree first, then the root node, and then the right subtree. Since the left subtree contains smaller values and the right subtree contains larger values, the values are processed in ascending order. This makes inorder traversal useful when you want to print or collect the elements of a BST in sorted order.

### 2. When would a BST become unbalanced?

A binary search tree can become unbalanced when values are inserted in sorted or nearly sorted order. For example, if the values are inserted as 1, 2, 3, 4, and 5, each new value may keep going to the right side of the tree. This creates a long chain instead of a balanced structure, making the BST act more like a linked list.

### 3. What is the difference between BFS and DFS for trees?

BFS, or breadth-first search, explores a tree level by level. It usually uses a queue to visit all nodes on one level before moving to the next level. DFS, or depth-first search, explores as far as possible down one branch before backtracking, usually using recursion or a stack. BFS is useful when you want to see nodes by level, while DFS is useful for exploring paths deeply.

## Challenges Encountered

One challenge in this lab was understanding why a binary search tree can be fast in one case but slow in another. At first, it seemed like every BST should have O(log n) search time, but I learned that this only happens when the tree is balanced. If values are inserted in sorted order, the tree can become unbalanced and searching can take O(n) time, which is much slower.
