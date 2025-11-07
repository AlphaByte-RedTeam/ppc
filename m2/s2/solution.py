#!/usr/bin/env python3
"""
dsa_session2_exercises.py

Single-file program for:
- Timing list operations: append, insert(0,x), pop(), pop(0) and plotting results.
- Solutions to practice problems:
    - reverse_in_place(lst)
    - flatten_2d(lst2d)
    - count_duplicates_list_only(lst)
    - max_in_sublists(list_of_lists)
    - DynamicArray (doubling/shrinking)
- Demo and simple tests.

Usage:
    python dsa_session2_exercises.py

Requirements:
    - Python 3.7+
    - matplotlib (optional, for plotting). If not available the program still runs timings and prints results.
"""

from __future__ import annotations
import time
import sys
import math
import statistics
from typing import List, Any, Iterable, Optional, Tuple

# Try import matplotlib but keep optional
try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except Exception:
    MATPLOTLIB_AVAILABLE = False


# ---------------------------
# Timing utilities & profiler
# ---------------------------

def time_operation(func, repeats: int = 5) -> float:
    """Time a callable `func` executed `repeats` times and return average seconds."""
    if repeats <= 0:
        raise ValueError("repeats must be >= 1")
    times = []
    for _ in range(repeats):
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        times.append(end - start)
    return statistics.mean(times)


def profile_list_operations(sizes: Iterable[int], repeats: int = 3) -> dict:
    """
    Profile list operations for given sizes.
    Returns dict with keys: 'append', 'insert0', 'pop', 'pop0' => lists of times per size.
    Each operation is measured by preparing a list of the target size and then performing
    the operation `repeats` times (re-initializing as needed).
    """
    results = {
        'sizes': [],
        'append': [],
        'insert0': [],
        'pop': [],
        'pop0': []
    }

    for n in sizes:
        results['sizes'].append(n)

        # Prepare baseline data: list of n elements
        base = list(range(n))

        # append: measure time to append one element to copy of base
        def op_append():
            lst = base.copy()
            lst.append(-1)

        t_append = time_operation(op_append, repeats=repeats)

        # insert(0, x): measure time to insert at start
        def op_insert0():
            lst = base.copy()
            lst.insert(0, -1)

        t_insert0 = time_operation(op_insert0, repeats=repeats)

        # pop(): pop last element
        def op_pop_end():
            lst = base.copy()
            if lst:
                lst.pop()

        t_pop = time_operation(op_pop_end, repeats=repeats)

        # pop(0): pop from start
        def op_pop0():
            lst = base.copy()
            if lst:
                lst.pop(0)

        t_pop0 = time_operation(op_pop0, repeats=repeats)

        results['append'].append(t_append)
        results['insert0'].append(t_insert0)
        results['pop'].append(t_pop)
        results['pop0'].append(t_pop0)

        print(f"n={n:7d} | append={t_append:.6f}s | insert0={t_insert0:.6f}s | pop_end={t_pop:.6f}s | pop0={t_pop0:.6f}s")

    return results


def plot_profile(results: dict, save_path: Optional[str] = None) -> None:
    """Plot results using matplotlib if available. Otherwise skip."""
    if not MATPLOTLIB_AVAILABLE:
        print("\nmatplotlib not available — skipping plot. Install matplotlib to see graphs.")
        return

    sizes = results['sizes']
    plt.figure(figsize=(9, 5))
    plt.plot(sizes, results['append'], label='append()', marker='o')
    plt.plot(sizes, results['insert0'], label='insert(0, x)', marker='o')
    plt.plot(sizes, results['pop'], label='pop() (end)', marker='o')
    plt.plot(sizes, results['pop0'], label='pop(0)', marker='o')
    plt.xlabel('n (list size)')
    plt.ylabel('time (seconds)')
    plt.title('List operation timings')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
        print(f"Saved plot to {save_path}")
    plt.show()


# ---------------------------
# Practice problem solutions
# ---------------------------

def reverse_in_place(lst: List[Any]) -> None:
    """
    Reverse list in place without using reversed() or slicing.
    Uses two-pointer swap.
    """
    if not isinstance(lst, list):
        raise TypeError("reverse_in_place expects a list")
    i, j = 0, len(lst) - 1
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1


def flatten_2d(lst2d: Iterable[Iterable[Any]]) -> List[Any]:
    """
    Flatten a 2D list (or iterable-of-iterables) to a single list.
    Preserves order.
    """
    result = []
    for row in lst2d:
        # Accept any iterable row
        for x in row:
            result.append(x)
    return result


def count_duplicates_list_only(lst: List[Any]) -> List[Tuple[Any, int]]:
    """
    Count duplicates using only lists (no dict). Returns list of (value, count).
    This is O(n^2), but respects the 'no dict' constraint.
    Keeps unique items in order of first appearance.
    """
    if not isinstance(lst, list):
        raise TypeError("count_duplicates_list_only expects a list")
    uniques = []
    counts = []
    for item in lst:
        try:
            idx = uniques.index(item)
            counts[idx] += 1
        except ValueError:
            uniques.append(item)
            counts.append(1)
    return list(zip(uniques, counts))


def max_in_sublists(list_of_lists: Iterable[Iterable[float]]) -> Optional[float]:
    """
    Given an iterable of iterables (list of lists), find the maximum element across all sublists.
    Returns None if there are no elements.
    """
    max_val = None
    found_any = False
    for sub in list_of_lists:
        for x in sub:
            if not found_any:
                max_val = x
                found_any = True
            else:
                if x > max_val:  # relies on comparable items
                    max_val = x
    return max_val


# ---------------------------
# DynamicArray Implementation
# ---------------------------

class DynamicArray:
    """
    Simple dynamic array implementation that uses a Python list as underlying storage,
    but simulates capacity, doubling when full, and shrinking when underused.

    Methods:
        - append(x)
        - pop()
        - insert(index, x)
        - __len__, __getitem__, __setitem__
    """

    def __init__(self, initial_capacity: int = 4):
        if initial_capacity <= 0:
            initial_capacity = 4
        self._capacity = int(initial_capacity)
        self._size = 0
        # allocate internal storage with None placeholders up to capacity
        self._data = [None] * self._capacity

    def __len__(self) -> int:
        return self._size

    def _resize(self, new_capacity: int):
        if new_capacity < self._size:
            raise ValueError("new_capacity must be >= size")
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def append(self, item: Any):
        if self._size >= self._capacity:
            # double capacity
            new_cap = max(1, self._capacity * 2)
            self._resize(new_cap)
        self._data[self._size] = item
        self._size += 1

    def pop(self) -> Any:
        if self._size == 0:
            raise IndexError("pop from empty DynamicArray")
        val = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        # shrink when quarter full to avoid thrashing
        if self._size > 0 and self._size <= self._capacity // 4:
            new_cap = max(4, self._capacity // 2)
            if new_cap < self._capacity:
                self._resize(new_cap)
        return val

    def insert(self, index: int, item: Any):
        if index < 0:
            index = 0
        if index > self._size:
            index = self._size
        if self._size >= self._capacity:
            self._resize(self._capacity * 2)
        # shift elements to right
        i = self._size
        while i > index:
            self._data[i] = self._data[i - 1]
            i -= 1
        self._data[index] = item
        self._size += 1

    def __getitem__(self, index: int) -> Any:
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        return self._data[index]

    def __setitem__(self, index: int, value: Any):
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        self._data[index] = value

    def capacity(self) -> int:
        return self._capacity

    def to_list(self) -> List[Any]:
        return [self._data[i] for i in range(self._size)]

    def __repr__(self) -> str:
        return f"DynamicArray(size={self._size}, capacity={self._capacity}, data={self.to_list()})"


# ---------------------------
# Demo / Test harness
# ---------------------------

def demo_exercises():
    print("\n=== Exercises demo & tests ===\n")

    # reverse_in_place
    lst1 = [1, 2, 3, 4, 5]
    print("Original lst1:", lst1)
    reverse_in_place(lst1)
    print("Reversed in place:", lst1)
    assert lst1 == [5, 4, 3, 2, 1], "reverse_in_place failed"

    # flatten_2d
    matrix = [[1, 2], [3, 4], [], [5]]
    flat = flatten_2d(matrix)
    print("Matrix:", matrix)
    print("Flattened:", flat)
    assert flat == [1, 2, 3, 4, 5], "flatten_2d failed"

    # count_duplicates_list_only
    arr = [1, 2, 1, 3, 2, 1]
    counts = count_duplicates_list_only(arr)
    print("Counts (value, count):", counts)
    # expected order: first appearance 1,2,3
    assert counts == [(1, 3), (2, 2), (3, 1)], "count_duplicates_list_only failed"

    # max_in_sublists
    lol = [[-1, -5], [0], [10, 3, 7]]
    max_val = max_in_sublists(lol)
    print("Max in sublists:", max_val)
    assert max_val == 10, "max_in_sublists failed"

    # DynamicArray test
    da = DynamicArray(initial_capacity=2)
    print("\nDynamicArray initial:", da)
    for i in range(8):
        da.append(i)
        print(f"append({i}): size={len(da)}, capacity={da.capacity()}")
    print("DynamicArray after appends:", da)
    for _ in range(6):
        v = da.pop()
        print(f"popped {v}: size={len(da)}, capacity={da.capacity()}")
    print("DynamicArray final:", da)

    # final confirm
    print("\nAll demos/tests ran (asserts passed).")


def main():
    print("DSA Session 2 - Advanced Arrays & Lists - demo and profiler\n")

    # 1) Profile list operations
    sizes = [1000, 5000, 10000, 20000, 40000]  # adjust these as needed
    print("Profiling list operations for sizes:", sizes)
    results = profile_list_operations(sizes, repeats=3)

    # 2) Plot (if available)
    plot_profile(results, save_path="list_ops_profile.png" if MATPLOTLIB_AVAILABLE else None)

    # 3) Discussion hint (printed)
    print("\nDiscussion (short):")
    print(" - append() is fast (amortized O(1)) because Python's list has spare capacity and only")
    print("   occasionally needs to allocate a larger buffer and copy elements.")
    print(" - insert(0, x) is slow (O(n)) because inserting at the beginning requires shifting")
    print("   all existing elements one position to the right.")
    print(" - pop() at end is O(1); pop(0) is O(n) for same reason as insert(0).")
    print("\nSee the plotted timing results to observe how insert(0) and pop(0) grow linearly with n.\n")

    # 4) Run exercises demo & tests
    demo_exercises()

    # 5) Quick interactive demonstration for DynamicArray (optional)
    try:
        print("\nYou can inspect DynamicArray behavior interactively. Example:")
        da = DynamicArray(2)
        da.append("a")
        da.append("b")
        print("Before append (a,b):", da)
        da.append("c")
        print("After append(c) -> capacity should increase:", da)
    except Exception as e:
        print("Interactive DynamicArray demo failed:", e)


if __name__ == "__main__":
    main()

