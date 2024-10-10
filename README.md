# Sorting Algorithms and Testing

This repository contains Python implementations of various sorting algorithms and a simple test file demonstrating Python's built-in list sorting. The `algorithms.py` file showcases multiple sorting methods and benchmarks their performance using the `timeit` library, while `test.py` provides a quick sort operation example using Python's built-in functionality.

## Table of Contents
- [Overview](#overview)
- [Files](#files)
- [Sorting Algorithms](#sorting-algorithms)
- [Performance Testing](#performance-testing)
- [Setup and Usage](#setup-and-usage)
- [Notes](#notes)

## Overview
The repository demonstrates and compares the performance of various sorting algorithms, including:
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Heap Sort

The project is intended for educational purposes, providing insights into the implementation and performance of common sorting techniques.

## Files

### `algorithms.py`
This file contains implementations of several sorting algorithms and tests their execution time using the `timeit` library. The following functions are included:
- `bubble_sort(arr)`: Sorts the array using the Bubble Sort algorithm.
- `selection_sort(arr)`: Sorts the array using the Selection Sort algorithm.
- `insertion_sort(arr)`: Sorts the array using the Insertion Sort algorithm.
- `merge_sort(arr)`: Sorts the array using the Merge Sort algorithm.
- `heap_sort(arr)`: Sorts the array using the Heap Sort algorithm leveraging Python’s `heapq` module.

It also includes benchmarking code that measures the time taken for each sorting function to sort a sample array.

### `test.py`
A simple script that demonstrates sorting a list using Python's built-in `sort()` method. This file serves as a quick example of how Python’s native sorting compares to the custom algorithms provided in `algorithms.py`.

## Sorting Algorithms

1. **Bubble Sort**:
   - A simple comparison-based algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
2. **Selection Sort**:
   - An in-place comparison-based algorithm that selects the smallest (or largest) element from an unsorted sublist and swaps it with the beginning element.
3. **Insertion Sort**:
   - A simple algorithm that builds the sorted array one element at a time by comparing the current element to its predecessors and inserting it into the correct position.
4. **Merge Sort**:
   - A divide-and-conquer algorithm that splits the array into smaller subarrays, sorts them recursively, and then merges them.
5. **Heap Sort**:
   - A comparison-based algorithm that uses a binary heap structure to sort elements.

## Performance Testing
The `algorithms.py` file includes performance testing using Python’s `timeit` library, measuring the time taken by each sorting algorithm to sort an array of integers. This gives a basic idea of how these algorithms perform relative to each other.

### Sample Output
The output displays execution times for each sorting algorithm when sorting a sample array:

```
Original array: [64, 34, 25, 12, 22, 11, 90]
Bubble sort time: 0.032
Selection sort time: 0.041
Insertion sort time: 0.028
Merge sort time: 0.013
Heap sort time: 0.010
```

*Note*: The actual times will vary based on system specifications.

## Setup and Usage

### Prerequisites
- Python 3.x installed on your system.

### Running the Code
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sorting-algorithms.git
   cd sorting-algorithms
   ```

2. Run the `algorithms.py` file to see the sorting algorithms in action:
   ```bash
   python algorithms.py
   ```

3. Run the `test.py` file to see the built-in sort method:
   ```bash
   python test.py
   ```

## Notes
- The performance measurements in `algorithms.py` are for demonstration and may not be accurate for very large datasets.
- Ensure that any modifications made to the sorting functions preserve the algorithm's integrity and efficiency.
