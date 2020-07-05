# Do not alter the next two lines
from collections import namedtuple
Node = namedtuple("Node", ["value", "left", "right"])

# Rewrite the following function to avoid slicing
def binary_search_tree(nums, is_sorted=False, first=0, last=None):
    """Return a balanced binary search tree with the given nums
       at the leaves. Changed function
    """

    if not is_sorted:
        nums = sorted(nums)
    if last == None:
        last = len(nums) - 1
    if last == first:
        tree = Node(nums[first], None, None)  # A leaf
    else:
        mid = last - (last - first) // 2  # Halfway (approx)
        left = binary_search_tree(nums, True, first, mid-1)
        right = binary_search_tree(nums, True, mid, last)
        tree = Node(nums[mid - 1], left, right)
    return tree
    
# Leave the following function unchanged
def print_tree(tree, level=0):
    """Print the tree with indentation"""
    if tree.left is None and tree.right is None: # Leaf?
        print(2 * level * ' ' + f"Leaf({tree.value})")
    else:
        print(2 * level * ' ' + f"Node({tree.value})")
        print_tree(tree.left, level + 1)
        print_tree(tree.right, level + 1)

nums = [228, 227, 3]
tree = binary_search_tree(nums)
print_tree(tree)