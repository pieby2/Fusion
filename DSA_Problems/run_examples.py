"""
Run all DSA examples at once
This script demonstrates all implementations in the DSA_Problems package
"""

import sys
import os
import subprocess


def run_module(module_path, module_name):
    """Run a Python module and display results"""
    print("\n" + "=" * 70)
    print(f"  {module_name}")
    print("=" * 70)
    
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(base_dir, module_path)
        subprocess.run([sys.executable, full_path], cwd=base_dir, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {module_name}: {e}")
    except Exception as e:
        print(f"Unexpected error running {module_name}: {e}")


def main():
    """Run all example modules"""
    print("\n" + "#" * 70)
    print("#" + " " * 68 + "#")
    print("#  DSA Problems - Complete Examples".center(70) + "#")
    print("#" + " " * 68 + "#")
    print("#" * 70)
    
    examples = [
        # Data Structures
        ("data_structures/linked_list.py", "Linked List Implementation"),
        ("data_structures/stack.py", "Stack Implementation"),
        ("data_structures/queue.py", "Queue Implementation"),
        ("data_structures/binary_tree.py", "Binary Search Tree Implementation"),
        
        # Algorithms
        ("algorithms/sorting.py", "Sorting Algorithms"),
        ("algorithms/searching.py", "Searching Algorithms"),
        ("algorithms/graph_algorithms.py", "Graph Algorithms"),
        
        # Problems
        ("problems/array_problems.py", "Array Problems"),
        ("problems/string_problems.py", "String Problems"),
        ("problems/dynamic_programming.py", "Dynamic Programming Problems"),
        ("problems/tree_problems.py", "Tree Problems"),
    ]
    
    for module_path, module_name in examples:
        run_module(module_path, module_name)
        input("\nPress Enter to continue to next example...")
    
    print("\n" + "=" * 70)
    print("  All examples completed!")
    print("=" * 70)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExecution interrupted by user.")
        sys.exit(0)
