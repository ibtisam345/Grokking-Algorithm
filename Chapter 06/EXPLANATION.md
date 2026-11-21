# Explanation of the BFS (Breadth-First Search) Algorithm implementation

## Overview
Breadth-First Search (BFS) is a graph traversal algorithm that explores nodes level by level. It starts from a given node, visits its immediate neighbours first, then their neighbours, and continues until the target is found or all reachable nodes have been explored.   
In this example, we search a social network to find a mango seller. A person is considered a seller if their name ends with the letter `m`.  

## Code Explanation
1. **Importing `deque`**
```python
from collections import deque
```
`deque` (double-ended queue) is a data structure that allows efficient insertion and removal of elements from both ends. 

BFS uses a queue following **FIFO (First In, First Out)** principle. The person added first is processed first.  

We use `deque` because removing an element from the beginning using `popleft()` is efficient, unlike `list.pop(0)`.  

2. **Seller-checking function**
```python
def person_is_seller(name):
    return name[-1] == 'm'
```
This function checks whether the last character of a person's name is `m`.  
* `name[-1]` accesses the last character of the string.  
* `== 'm'` compares that character with the string `'m'`.  
* The expression returns either `True` or `False`.   

For example:
```python
person_is_seller("Thom")  # True
person_is_seller("Bob")   # False
```

3. **Creating the graph**
```python
graph = {}
```
Creates an empty dictionary to represent the graph.  
```python
graph["you"] = ["Alice", "Bob", "Claire"]
```
The node `"you"` is connected to Alice, Bob, and Claire.
```python
graph["Bob"] = ["Anuj", "Peggy"]
graph["Alice"] = ["Peggy"]
graph["Claire"] = ["Thom", "Jonny"]
```
These lines define the neighbours of each person.
```python
graph["Anuj"] = []
graph["Peggy"] = []
graph["Thom"] = []
graph["Jonny"] = []
```
These people have no outgoing connection in this graph.  

The graph is represented using an **adjacency list**, where each dictionary key is a node and its value is a list of neighbouring nodes.

4. **Defining the search function**
```python
def breadth_first_search(name):
```
Defines a function named `breadth_first_search`. The parameter `name` represents the starting node.

5. **Creating the search queue**
```python
search_queue = deque()
```
Creates an empty queue that will store people waiting to be examined.  
```python
search_queue += [name]
```
Adds the starting person to the queue.  
Alternatively, we could write:
```python
search_queue.append(name)
```

6. **Creating the searched set**
```python
searched = set()
```
Creates an empty set to keep track of people who have already been processed. 

This prevents the algorithm from examining the same person repeatedly, which is especially important when the graph contains duplicate connections or cycles. 

7. **The main loop**
```python
while search_queue:
```
Continues running as long as the queue is not empty.  

An empty queue means there are no people left to examine.

8. **Removing the next person**
```python
person = search_queue.popleft()
```
Removes the person at the front of the queue and stores their name in `person`.  

Because the queue follows FIFO, the earliest discovered person is processed first. 

9. **Skipping already-searched people**
```python
if person in searched:
    continue
```
Checks whether the person has already been processed.    

If they have, `continue` skips the remaining code in the current iteration and moves to the next person in the queue. 

This prevents unnecessary repeated work.   

10. **Checking for a mango seller**
```python
if person_is_seller(person):
```
Calls the seller-checking function.  

If it returns `True`, the following statements execute:
```python
print(person + " is a mango seller!")
    return True
```
The first line prints a message indicating that the seller has been found.  

The second line immediately terminates the search function and returns `True`.  

There is no need to continue searching after finding the target. 

11. **Adding neighbours to the queue**
```python
search_queue += graph[person]
```
Retrieves the person's neighbours from the graph and adds them to the end of the queue.   

This is the main step that expands the search into the graph.   

Because neighbours are added to the back of the queue, BFS explores nodes level by level. 

12. **Marking the person as searched**
```python
searched.add(person)
```
Adds the current person to the `searched` set.  

The algorithm now remembers that this person has already been processed.

13. **Returning `False`**
```python
return False
```
This statement executes if the queue becomes empty without finding a seller.  

It indicates that no mango seller exists among the reachable nodes.

14. **Starting the search**
```python
breadth_first_search("you")
```
Calls the function with `"you"` as the starting node.  

The algorithm begins exploring the social network from this person.  

## Dry Run

Initial state:  

```
Queue:    [you]
Searched: {}
```

| Step | Person | Seller? | Queue after processing |
| :--- | :--- | :--- | :--- |
| 1 | you | No | Alice, Bob, Claire |
| 2 | Alice | No | Bob, Claire, Peggy |
| 3 | Bob | No | Claire, Peggy, Anuj, Peggy |
| 4 | Claire | No | Peggy, Anuj, Peggy, Thom, Jonny |
| 5 | Peggy | No | Anuj, Peggy, Thom, Jonny |
| 6 | Anuj | No | Peggy, Thom, Jonny |
| 7 | Peggy | Already searched | Thom, Jonny |
| 8 | Thom | **Yes** | Search terminates |

When Peggy appears for the second time, the `searched` set detects the duplicate and skips her.

When Thom is examined, his name ends with `'m'`, so the seller-checking function returns `True`.

Output:
```
Thom is a mango seller!
```

## Key Concepts

- **Graph**: Represents relationships between nodes.
- **Adjacency list**: Stores each node's neighbours.
- **Queue**: Determines the order of exploration (FIFO).
- **Set**: Prevents repeated processing of nodes.
- **BFS**: Explores a graph level by level.
- **Shortest path**: BFS finds the shortest path in an unweighted graph.

### Complexity

Let `V` be the number of vertices and `E` the number of edges.

- Time complexity: $O(V + E)$
- Space complexity: $O(V)$, excluding the graph itself.

BFS is useful for finding shortest paths in unweighted graphs, exploring social networks, solving mazes, and finding connections between nodes.