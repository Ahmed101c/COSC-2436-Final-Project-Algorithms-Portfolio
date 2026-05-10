from typing import Optional, Any, List


class AVLNode:
    """AVL tree node with height tracking."""
    def __init__(self, value: Any):
        self.value = value
        self.left: Optional['AVLNode'] = None
        self.right: Optional['AVLNode'] = None
        self.height: int = 1


class AVLTree:
    """Self-balancing AVL tree."""
    
    def __init__(self):
        self.root: Optional[AVLNode] = None
    
    def height(self, node: Optional[AVLNode]) -> int:
        """Get height of node (None = 0)."""
        return node.height if node else 0
    
    def balance_factor(self, node: AVLNode) -> int:
        """
        Calculate balance factor: height(left) - height(right)
        
        From Chapter 8:
        - Balance factor of -1, 0, or 1 is balanced
        - Other values require rotation
        """
        return self.height(node.left) - self.height(node.right)
    
    def rotate_right(self, y: AVLNode) -> AVLNode:
        """
        Right rotation for left-heavy tree.
        
            y                x
           / \              / \
          x   C    -->     A   y
         / \                  / \
        A   B                B   C
        """
        x = y.left
        B = x.right

        x.right = y
        y.left = B

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x
    
    def rotate_left(self, x: AVLNode) -> AVLNode:
        """Left rotation for right-heavy tree."""
        y = x.right
        B = y.left

        y.left = x
        x.right = B

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y
    
    def insert(self, value: Any) -> None:
        """Insert value and rebalance."""
        self.root = self._insert(self.root, value)
    
    def _insert(self, node: Optional[AVLNode], value: Any) -> AVLNode:
        """Recursive insert with rebalancing."""
        # 1. Standard BST insert
        if node is None:
            return AVLNode(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node  # no duplicates

        # 2. Update height
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        # 3. Check balance factor
        balance = self.balance_factor(node)

        # 4. Rotate if needed

        # LL Case
        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)

        # RR Case
        if balance < -1 and value > node.right.value:
            return self.rotate_left(node)

        # LR Case
        if balance > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # RL Case
        if balance < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node
    
    def inorder(self) -> List[Any]:
        """Return sorted values."""
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node: Optional[AVLNode], result: List[Any]) -> None:
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)
