from collections import deque


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#     def __repr__(self):
        
#         return f"Node {self.val}"

 
# def buildTree(nums):
#     if not nums:
#         return None
#     root = TreeNode(nums[0])
#     q = [root]
#     i = 1
#     while i < len(nums):
#         curr = q.pop(0)
#         if i < len(nums):
#             curr.left = TreeNode(nums[i])
#             q.append(curr.left)
#             i += 1
#         if i < len(nums):
#             curr.right = TreeNode(nums[i])
#             q.append(curr.right)
#             i += 1
#     return root
 
# def printTree(root):
#     if not root:
#         return
#     printTree(root.left)
#     print(root.val, end=" ")
#     printTree(root.right)
# null=None
# nums = [1,3,2,5,null,null,9,6,null,7]
# root = buildTree(nums)
# printTree(root)
# print()

def widthOfBinaryTree(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:return 0
    maxw=1
    q=deque([root])
    iq=deque([1])
    while q:
        levelsize=len(q)
        l,r=0,0
        print(q)
        for i in range(levelsize):
            node=q.popleft()
            index=iq.popleft()
            

            if i==0:
                l=index
            if i==levelsize-1:
                r=index
            if node.left:
                q.append(node.left)
                iq.append(index*2)
            if node.right:
                q.append(node.right)
                iq.append(2*index+1)
        
        maxw=max(maxw,r-l+1)
    return maxw
#     """
#               0
#           0        1
#         0   1    2   3 
#       0 1  2 3   4 5  6 7

#     2*i 2*i+1 childs
#     """


from typing import List, Optional

class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"Node {self.val}"
    

def binary_tree(level_order) :
    values = iter(level_order)
    root = Node(next(values))
    nodes_to_fill = [root]
    try:
        while True:
            next_node = nodes_to_fill.pop(0)
            new_left = next(values)
            if new_left is not None:
                next_node.left = Node(new_left)
                nodes_to_fill.append(next_node.left)
            new_right = next(values)
            if new_right is not None:
                next_node.right = Node(new_right)
                nodes_to_fill.append(next_node.right)
    except StopIteration:
        return root
print(binary_tree([1,2,3,4,5]))
print(str(binary_tree([1,2,3,4,5])))

def preorder(root):
    if root:
        print(root.val)
    if not root:
        print("null")
    if root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)
    


#preorder(binary_tree([1,2,3,4,5,6,7,8,9,None,None,12,13]))
def printTree(root, level=0):
    if not root:
        return
    if level==0:
        s=''
    else:
        s='  '*(level)+"-"
    print(s, root.val)
    printTree(root.left, level + 1)
    printTree(root.right, level + 1)
printTree(binary_tree([1,2,3,4,5,6,7,8,9,None,None,12,13]))
print(widthOfBinaryTree(binary_tree([1,2,3,4,5,6,7,8,9,None,None,12,13])))
