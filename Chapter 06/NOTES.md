# Implementing a Graph

A graph can be represented with an **adjacency list**: each node is stored as a key in a dictionary, and its value is a list of connected nodes (its neighbours).

In this example, each key maps to all of the node's **out-neighbours**:

```python
graph = {}

graph["you"] = ["Alice", "Bob", "Claire"]
graph["Bob"] = ["Anuj", "Peggy"]
graph["Alice"] = ["Peggy"]
graph["Claire"] = ["Thom", "Jonny"]
graph["Anuj"] = []
graph["Peggy"] = []
graph["Thom"] = []
graph["Jonny"] = []
```

Here, `"you"` points to `"Alice"`, `"Bob"`, and `"Claire"`. `"Anuj"`, `"Peggy"`, `"Thom"`, and `"Jonny"` have no out-neighbours, so their values are empty lists.

## Hash Table Ordering

Key order is not part of a graph's meaning. A dictionary may display keys in insertion order in modern Python, but changing the order in which you add nodes does not change the graph:

```python
graph = {}

graph["Anuj"] = []
graph["Claire"] = ["Thom", "Jonny"]
graph["you"] = ["Alice", "Bob", "Claire"]
```

This is also true for dictionary literals:

```python
graph = {
    "Anuj": [],
    "Claire": ["Thom", "Jonny"],
    "you": ["Alice", "Bob", "Claire"],
}
```
