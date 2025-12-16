"""
DSA Problems Package
Contains implementations of data structures, algorithms, and problem solutions.
"""

__version__ = "1.0.0"
__author__ = "pieby2"

# Import key components for easy access
from .data_structures.linked_list import LinkedList, Node
from .data_structures.stack import Stack
from .data_structures.queue import Queue, CircularQueue
from .data_structures.binary_tree import BinarySearchTree, TreeNode

__all__ = [
    'LinkedList',
    'Node',
    'Stack',
    'Queue',
    'CircularQueue',
    'BinarySearchTree',
    'TreeNode',
]
