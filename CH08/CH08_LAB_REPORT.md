2436 Lab 8 Balanced Trees

Lab Report

Student Information

Name: Ahmed Ajlal
Date: 4/4/2026
Algorithm Analysis

AVL Trees

Balance Factor Range: -1, 0, 1

Why rebalance? To keep the tree height close to log n, so searches, insertions, and deletions do not degrade into the O(n) time of an unbalanced BST.

**Time Complexity: O(log n)

Rotation Cases

Case	Imbalance	Fix
LL	Left subtree of left child is heavy.	Single right rotation
RR	Right subtree of right child is heavy.	Single left rotation
LR	Right subtree of left child is heavy.	Left rotation on left child, then right rotation
RL	Left subtree of right child is heavy.	Right rotation on right child, then left rotation
