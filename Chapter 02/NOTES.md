# Python List Methods: `append()` and `pop()`

In Python, `append()` and `pop()` are built-in list methods used to add and remove elements dynamically. Together, they allow a Python list to function as a **LIFO (Last-In, First-Out) stack**.

---

## 1. `list.append(item)`
Adds a **single element** to the very end of a list.

* **Syntax:** `my_list.append(item)`
* **Modifies in-place:** Yes, it updates the original list directly.
* **Return Value:** `None` (Do **not** do `my_list = my_list.append(x)` or you will overwrite your list with `None`).

### Example
```python
fruits = ["apple", "banana"]
fruits.append("cherry")

print(fruits)  # Output: ['apple', 'banana', 'cherry']
```
> **Note:** Appending a list to another list adds it as a single nested element (e.g., `[1, 2, [3, 4]]`). Use `.extend()` to merge elements individually.

---

## 2. `list.pop([index])`
Removes and **returns** an item at a given index. If no index is passed, it defaults to the **last item** (`index = -1`).

* **Syntax:** `my_list.pop()` or `my_list.pop(index)`
* **Modifies in-place:** Yes, it shrinks the original list.
* **Return Value:** The removed element.
* **Errors:** Raises an `IndexError` if the list is empty or the index is out of range.

### Example
```python
colors = ["red", "green", "blue"]

# Remove and return the last item
last = colors.pop()
print(last)    # Output: 'blue'
print(colors)  # Output: ['red', 'green']

# Remove and return item at index 0
first = colors.pop(0)
print(first)   # Output: 'red'
print(colors)  # Output: ['green']
```

---

## Quick Comparison

| Feature | `append(x)` | `pop([i])` |
| :--- | :--- | :--- |
| **Action** | Adds `x` to the end | Removes item at `i` (default: last) |
| **Arguments** | Required (1 item) | Optional (`index`) |
| **Returns** | `None` | The removed item |

