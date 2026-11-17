# List Comprehension

The **Quick Sort** program uses a Python feature called *List Comprehension*, which provides a compact way to create a new list from an existing iterable.

### Basic Syntax

```python
new_list = [expression for item in iterable if condition]
```

**How it works:**
- `expression`: What to add to the new list.
- `item`: Each element being processed.
- `iterable`: The collection we iterate over.
- `condition`: An optional condition to filter elements.

### Implementation

In Quick Sort, we use list comprehension to divide the array into two lists based on the pivot:

```python
less = [i for i in array[1:] if i <= pivot]
greater = [i for i in array[1:] if i > pivot]
```

- `less`: Contains elements smaller than or equal to the pivot.
- `greater`: Contains elements greater than the pivot.

**Note:** List comprehension is a shorter alternative to creating a list using a `for` loop and `append()`. It still performs iteration internally.