'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

'''

class Node: 
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(tree):
    return seralizeNode(tree)

def seralizeNode(node):
    if (node.left == None and node.right == None):
        return f'Node(\'{node.val}\')'
    elif (node.left != None and node.right == None):
        return f'Node(\'{node.val}\', {seralizeNode(node.left)})'
    elif (node.left == None and node.right != None):
        return f'Node(\'{node.val}\', None, {seralizeNode(node.right)})'
    elif (node.left != None and node.right != None):
        return f'Node(\'{node.val}\', {seralizeNode(node.left)}, {seralizeNode(node.right)})'

def deserialize(treeString):
    node = eval(treeString)
    return node

def main():
    node = Node('root', Node('left', Node('left.left')), Node('right', Node('right.left', Node('right.left.left'), Node('right.left.right')), Node('right.right')))
    #print(serialize(node))
    print(deserialize(serialize(node)).left.left.val)

main()
