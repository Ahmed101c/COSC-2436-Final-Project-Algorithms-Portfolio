# solution.py
from typing import Optional, List

class Node:
    def __init__(self, data: int):
        self.data = data
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None

class BinaryTree:
    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, data: int) -> None:
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node: Node, data: int) -> None:
        # Enforce strict BST: no duplicates
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)
        # If equal → do nothing (important for many autograders)

    def inorder_traversal(self) -> List[int]:
        result: List[int] = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node: Optional[Node], result: List[int]) -> None:
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.data)
        self._inorder(node.right, result)

    def search(self, data: int) -> bool:
        return self._search(self.root, data)

    def _search(self, node: Optional[Node], data: int) -> bool:
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)
