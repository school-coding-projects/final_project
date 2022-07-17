# **Tree**
| [Stack](1-stack.md) | [Set](2-set.md) | [Binary Tree](3-tree.md) |
| ------------------- | --------------- | --------------------- |

## **Introduction**

A **`Tree`** is a data structure in which elements are connected in a hierarchical manner. Different tree data structures allow quicker and easier access data.

The **`Tree`** data structure O notation will result in O(log n)n when the tree is balanced. If the **`Tree`** is more like a linked list, the O notation will result in O(n).

**Root Node** 

The _`Root`_ node if the topmost of a **`Tree`**. This is the first node that is created with creating a **`Tree`**. You are able to start at the root and then branch out to a node which will either have zero or more nodes connected as children. There is always only one root node.

**Parent Node**

A node that has connected nodes is called a _`Parent`_ Node.

**Child Node**

The node connected to the _Parent_ node is a _`Child`_ node.



## **Types of Trees**

**Binary Tree**

A _**Binary Tree**_ has links to no more than two other nodes. The top node is called the `root` node. A node that has connected nodes is called a `parent` node. The nodes connected to the `parent` node are called `child` nodes. The nodes to the left and right of the `parent` node form a `subtree`. Nodes that connect to no other nodes are called `leaf` nodes. 

<picture>
    <source media="(prefers-color-scheme: dark)" srcset="Images\Binary_tree.png">
    <source media="(prefers-color-scheme: light)" srcset="Images\Binary_tree.png">
    <img alt="Binary Tree" src="Images\Binary_tree.png">
</picture>


**Binary Search Tree**

When adding elements, we always start with comparing the data to the root node. Then we are able to see if our data is less than or greater than. If it is less than the root data, the new data will go to the Left Node. If the data is greater than the root data, the new datat will go to the Right Node. We keep comparing until we find an empty place for the new node.
If duplicates are allowed, then the duplicate can be put to either the left or right side of the root. Storing the data this way sorts the data.  



**Balanced Binary Tree**

With a _**Balanced Binary Tree (BST)**_, the difference in height between any two subtrees will no be significant. We can find the height of a tree by counting the maximum number of nodes between the root node to the deepest leaves.

```python
def height(node):
    if node is None:
        return 0
    else:
        return max(height(node.left), height(node.right)) + 1
```


## **Create Root**
To create a _**Tree**_ we can create a Node class and then assign a value to the node. This then becomes a tree with a root node.

```python
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def PrintTree(self):
      print(self.data)

root = Node(5)
root.PrintTree()
# 5
```

## **Inserting into a Tree**

To insert into a _**Tree**_, we add the a function within the class to help identify the `parent` and whether to add to the left or right node. 

```python
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Function to look for a place to insert a node with 'data' inside of it. 
    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            # Checking if 'data' belong on left side
            if data < self.data:
                if self.left is None:
                    # Found an empty spot
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            # Checking if 'data' belongs on right side
            elif data > self.data:
                if self.right is None:
                    # Found an empty spot
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Function to print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

# Establishing Root
root = Node(20)

# Using insert to add nodes to the tree
root.insert(5)
root.insert(15)
root.insert(10)

# Printing the tree
root.PrintTree()

# 5 10 15 20 
```


# **Tree Traversal**

Traversal is a process in which we visit all the nodes of a tree in order to possibly display the data. Due to all nodes being connected , we start at the root node. We are unable to randomly access a node in a tree so it must be traversed. With these traversals, we will be referencing the steps for _**Binary Search Trees**_.

There are three ways to traverse a tree. 

- In-Order Traversal
- Pre-Order Traversal
- Post-Order Traversal

## **In-Order Traversal**

With this traversal, we visit each node from smallest to largest. To accomplish this, we start with the left subtree is visited first, then the root and finally the right subtree. 

For this traversal, we will create an empty list to add the left node(s) to first, then to the root, and finally to the right node(s). 

```python
# Add to the class Node.

    # In-order traversal
    # Left Node --> Root --> Right Node
    def inorder_traversal(self, root):
        inorder = []
        if root:
            inorder = self.inorder_traversal(root.left)
            inorder.append(root.data)
            inorder += self.inorder_traversal(root.right)
        return inorder

# Establishing Root
root = Node(20)

# Using insert to add nodes to the tree
root.insert(5)
root.insert(25)
root.insert(10)
root.insert(35)
root.insert(15)

print(root.inorder_traversal(root))
# [5, 10, 15, 20, 25, 35]
```

## **Pre-Order Traversal**

In Pre-order traversal the root node is visited first, followed by the left subtree and then the right subtree. 

```python
# Add to the class Node.

    # Pre-order traversal
    # Root --> Left Node --> Right Node
    def preorder_traversal(self, root):
        preorder = []
        if root:
            preorder.append(root.data)
            preorder += self.preorder_traversal(root.left)
            preorder += self.preorder_traversal(root.right)
        return preorder

# Establishing Root
root = Node(20)

# Using insert to add nodes to the tree
root.insert(5)
root.insert(25)
root.insert(10)
root.insert(35)
root.insert(15)

print(root.preorder_traversal(root))
# [20, 5, 10, 15, 25, 35]
```

## **Post-Order Traversal**

In Post-order traversal the left node is visited first, followed by the right subtree and finally the root.

```python
# Add to the class Node.

    # Post-order traversal
    # Left node --> Right Node --> Root
    def postorder_traversal(self, root):
        postorder = []
        if root:
            postorder = self.postorder_traversal(root.left)
            postorder += self.postorder_traversal(root.right)
            postorder.append(root.data)
        return postorder

# Establishing Root
root = Node(20)

# Using insert to add nodes to the tree
root.insert(5)
root.insert(25)
root.insert(10)
root.insert(35)
root.insert(15)

print(root.postorder_traversal(root))

```







## **Example**
In this example we will find the sum of each subtree.
```python
class TreeNode:
    # Creating Root
    def __init__(self, l_Value, l_Left=None, l_Right=None):
        self.Value = l_Value
        self.Left = l_Left
        self.Right = l_Right

# Finding where to insert value
def addNode(root, l_Val):
    newNode = TreeNode(l_Val)
    queue = []
    queue.append(root)
    while(len(queue) > 0):
        node = queue.pop(0)
        if node.Left is None:
            node.Left = newNode
            break

        if node.Right is None:
            node.Right = newNode
            break

        queue.append(node.Left)
        queue.append(node.Right)

# Creating a way to add numbers into the tree more efficiently
def createBinaryTree(l_List):
    binaryTree = None
    for i in l_List:
        if i != -1:
            if binaryTree is not None:
                addNode(binaryTree, i)
            else:
                binaryTree = TreeNode(i)
    return binaryTree

# Finding the values in each subtree
def sum(node):
    if node is None:
        return 0
    # Find values in Left subtree   
    l_LeftVal = sum(node.Left)
    # Find values in Right Subtree
    l_RightVal = sum(node.Right)

    return (l_LeftVal + l_RightVal + node.Value)
   

# Finding the sum of each subtree
def solution(binaryTree):
    if binaryTree == None:
        return 0

    if binaryTree != None:
        # Find sum of Left Subtree
        total_left = sum(binaryTree.Left)
        # Find sum of Right Subtree
        total_right = sum(binaryTree.Right)

        return(f"Total of Left Subtree: {total_left} \nTotal of Right Subtree: {total_right}")


if __name__=='__main__':
    binaryTree = createBinaryTree([1, 2, 3, 4, 5, 6, 7])
    print(solution(binaryTree))

# Total of Left Subtree: 11 
# Total of Right Subtree: 16
```












## **Problem to Solve**
Delete a Node from a Tree
```python
class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Write function to add Child data to tree
    def add_child(self, data):
        pass

    # Write function to search the tree for 'val'
    def search(self, val):
        pass

    # Write function to perform in-order traversal
    def inorder_traversal(self):
        pass

    # Write function to find max
    def find_max(self):
        pass

    # Write function to find min
    def find_min(self):
        pass

    # Write function to delete 'val' from tree
    def delete(self, val):
        pass


# Build function that will take 'elements' and build the tree
def build_tree(elements):
    print("Building tree:", elements)

    pass


if __name__=='__main__':
    numbers_tree = build_tree([5, 25, 20, 10, 15, 50, 30])
    # Building tree: [5, 25, 20, 10, 15, 50, 30]
    numbers_tree.delete(50)
    print("After deleting 50: ", numbers_tree.inorder_traversal())
    # After deleting 50:  [5, 10, 15, 20, 25, 30, 50]

```








[Deleting Node Solution](python-files\binary_tree_solution.py)

[Back to Welcome page](welcome.md)