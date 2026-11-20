# Implementing the graph

**We need to connect each node with its neighbour nodes.**  
**For that, we need a *data structure* named - Hash Tables.**

*In this case, I want to map a node to all of its out-neighbours*  

```python
graph = {}

graph["you"] = {"Alice", " Bob", "Claire"}
```

* Hash tables has no ordering. So it doesn't matter if I write:
```python
graph["Claire"] = ["Thom", "Jonny"]
graph["Anuj"] = []
```   
instead of
```python
graph["Anuj"] = []
graph["Claire"] = ["Thom", "Jonny"]
```
