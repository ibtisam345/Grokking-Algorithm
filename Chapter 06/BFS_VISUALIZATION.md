
# Breadth-First Search (BFS) — Visual Guide

This document visually explains the Breadth-First Search (BFS) implementation from Chapter 6 of **Grokking Algorithms**.

For the complete code explanation, see [`EXPLANATION.md`](./EXPLANATION.md).

---

## 1. The Social Network Graph

Imagine we are searching for a mango seller among our friends and their friends.

Each person is a node, and each connection represents a person we can contact.

```mermaid
graph TD
    You --> Bob
    You --> Alice
    You --> Claire

    Bob --> Anuj
    Bob --> Peggy
    Alice --> Peggy
    Claire --> Thom
    Claire --> Jonny

    class Thom seller
    classDef seller fill:#90EE90,stroke:#228B22,stroke-width:3px,color:#000
```

Our goal is to find someone whose name ends with `"m"`.

In our implementation:

```python
def person_is_seller(name):
    return name[-1] == "m"
```

Therefore, **Thom** is our mango seller.

---

## 2. BFS Traversal Levels

BFS explores the network level by level.

It first checks people directly connected to us, then people connected to them, and so on.

```mermaid
flowchart TD
    A["You<br/>Level 0"] --> B["Bob<br/>Level 1"]
    A --> C["Alice<br/>Level 1"]
    A --> D["Claire<br/>Level 1"]

    B --> E["Anuj<br/>Level 2"]
    B --> E["Peggy<br/>Level 2"]
    C --> F["Peggy<br/>Level 2"]
    D --> G["Thom 🍋<br/>Level 2"]
    D --> H["Jonny<br/>Level 2"]

    class G seller
    classDef seller fill:#90EE90,stroke:#228B22,stroke-width:3px,color:#000
```

### The order of exploration

1. **Level 0:** You
2. **Level 1:** Bob → Alice → Claire
3. **Level 2:** Anuj → Peggy → Thom → Jonny

Because BFS explores level 1 before level 2, it finds the mango seller at the shortest connection distance.

---

## 3. How the Algorithm Works

The following flowchart represents the logic of `breadth_first_search(name)`.

```mermaid
flowchart TD
    A([Start]) --> B["Create queue<br/>Add starting person's friends"]
    B --> C["Create empty searched set"]
    C --> D{"Is queue empty?"}

    D -->|Yes| E["No mango seller found"]
    E --> F([Return False])

    D -->|No| G["Remove first person<br/>from queue"]
    G --> H{"Already searched?"}

    H -->|Yes| D
    H -->|No| I["Add person to searched"]

    I --> J{"Is this person<br/>a mango seller?"}

    J -->|Yes| K["Mango seller found!"]
    K --> L([Return True])

    J -->|No| M["Add their friends<br/>to the queue"]
    M --> D
```

The important idea is that the queue controls **the order in which people are explored**.

---

## 4. Queue State During Execution

A queue follows the **FIFO** principle:

> First In, First Out.

The person who enters the queue first is the person who gets checked first.

Let's follow the queue step by step.

### Initial state

We start by adding You's friends to the queue.

```mermaid
flowchart LR
    A["Bob"] --> B["Alice"] --> C["Claire"]

    style A fill:#FFE4B5,color:#000,stroke:#8B4513
    style B fill:#FFE4B5,color:#000,stroke:#8B4513
    style C fill:#FFE4B5,color:#000,stroke:#8B4513
```

Queue:

```text
[Bob, Alice, Claire]
```

### Step 1 — Check Bob

Bob is removed from the front.

Bob is not a mango seller, so we add Bob's friend Anuj.

```text
Queue before: [Bob, Alice, Claire]
Check: Bob
Queue after:  [Alice, Claire, Anuj]
```

### Step 2 — Check Alice

Alice is removed from the front.

Alice is not a mango seller, so Peggy is added.

```text
Queue before: [Alice, Claire, Anuj]
Check: Alice
Queue after:  [Claire, Anuj, Peggy]
```

### Step 3 — Check Claire

Claire is removed from the front.

Claire is not a mango seller, so Jonny and Thom are added.

```text
Queue before: [Claire, Anuj, Peggy]
Check: Claire
Queue after:  [Anuj, Peggy, Jonny, Thom]
```

### Step 4 — Check Anuj

Anuj is removed from the front.

Anuj is not a mango seller and has no additional friends in our graph.

```text
Queue before: [Anuj, Peggy, Jonny, Thom]
Check: Anuj
Queue after:  [Peggy, Jonny, Thom]
```

### Step 5 — Check Peggy

Peggy is removed from the front.

Peggy is not a mango seller.

```text
Queue before: [Peggy, Jonny, Thom]
Check: Peggy
Queue after:  [Jonny, Thom]
```

### Step 6 — Check Jonny

Jonny is removed from the front.

Jonny is not a mango seller.

```text
Queue before: [Jonny, Thom]
Check: Jonny
Queue after:  [Thom]
```

### Step 7 — Check Thom 🍋

Thom is removed from the front.

```mermaid
flowchart LR
    A["Queue"] --> B["Thom"]
    B --> C["Check Thom"]
    C --> D{"name[-1] == 'm'?"}
    D -->|Yes| E["MANGO SELLER FOUND!"]

    style E fill:#90EE90,color:#000000,stroke:#000000,stroke-width:3px
```

```python
person_is_seller("Thom")
```

Returns:

```python
True
```

The search terminates immediately.

---

## 5. Complete Dry Run

| Step | Person Checked | Queue After Checking | Searched Set | Seller? |
|------|----------------|---------------------|---------------|---------|
| 0 | — | Bob, Alice, Claire | `{}` | — |
| 1 | Bob | Alice, Claire, Anuj | `{Bob}` | No |
| 2 | Alice | Claire, Anuj, Peggy | `{Bob, Alice}` | No |
| 3 | Claire | Anuj, Peggy, Jonny, Thom | `{Bob, Alice, Claire}` | No |
| 4 | Anuj | Peggy, Jonny, Thom | `{Bob, Alice, Claire, Anuj}` | No |
| 5 | Peggy | Jonny, Thom | `{Bob, Alice, Claire, Anuj, Peggy}` | No |
| 6 | Jonny | Thom | `{Bob, Alice, Claire, Anuj, Peggy, Jonny}` | No |
| 7 | **Thom** | — | `{Bob, Alice, Claire, Anuj, Peggy, Jonny, Thom}` | **YES!** |

The search stops at Step 7.

---

## 6. Why Do We Need the `searched` Set?

Imagine two different people have a connection to the same person.

For example:

```mermaid
graph TD
    You --> Bob
    You --> Alice

    Bob --> Peggy
    Alice --> Peggy

    Peggy --> Thom
```

Both Bob and Alice know Peggy.

Without a `searched` set, Peggy could be added to the queue multiple times.

```mermaid
flowchart TD
    A["Bob"] --> C["Peggy"]
    B["Alice"] --> C

    C --> D["Peggy added twice!"]
    
    style D fill:#FFB6C1,color:#000000,stroke:#DC143C,stroke-width:2px
```

This creates unnecessary work.

Our implementation prevents this using:

```python
searched = set()
```

Before processing someone:

```python
if person not in searched:
    searched.add(person)
```

Once Peggy is added to `searched`, we know that she has already been examined.

### The protection mechanism

```mermaid
flowchart TD
    A["Person appears in queue"] --> B{"Already in searched?"}

    B -->|Yes| C["Skip this person"]
    B -->|No| D["Add to searched"]
    D --> E["Check if seller"]
    E --> F["Explore their friends"]

    style C fill:#FFE4B5,color:#000000
    style D fill:#90EE90,color:#000000
```

The `searched` set ensures that every person is processed **at most once**.

---

## 7. The Moment Thom Is Found

Let's zoom in on the final moment.

```mermaid
sequenceDiagram
    participant Q as Queue
    participant S as search()
    participant C as person_is_seller()

    Q->>S: Thom
    S->>S: Remove Thom from queue
    S->>C: person_is_seller("Thom")
    C->>C: Check final character
    C-->>S: True
    S-->>Q: Search terminates
```

The function returns:

```python
True
```

No further people are checked.

---

## 8. The Core Idea of BFS

BFS is not simply about searching through a graph.

It is about searching **in order of increasing distance from the starting node**.

```mermaid
flowchart TD
    A["Starting Point"] --> B["Distance 1"]
    A --> C["Distance 1"]
    A --> D["Distance 1"]

    B --> E["Distance 2"]
    C --> F["Distance 2"]
    D --> G["Distance 2"]

    E --> H["Distance 3"]
    F --> I["Distance 3"]
    G --> J["Distance 3"]

    subgraph Level0["Level 0"]
        A
    end

    subgraph Level1["Level 1"]
        B
        C
        D
    end

    subgraph Level2["Level 2"]
        E
        F
        G
    end

    subgraph Level3["Level 3"]
        H
        I
        J
    end
```

### Remember

- **Queue:** Determines who gets explored next.
- **BFS:** Explores nearby nodes before distant nodes.
- **`searched`:** Prevents duplicate processing.
- **Seller check:** Determines whether the current person satisfies our goal.
- **Early termination:** Stops the search as soon as the seller is found.

In one sentence:

> **Breadth-First Search explores a graph level by level using a queue, allowing it to find the closest matching node first.**

---

## Related Files

- [`EXPLANATION.md`](./EXPLANATION.md) — Detailed explanation of the implementation.
- [`BFS_VISUALIZATION.md`](./BFS_VISUALIZATION.md) — Visual representation of BFS using Mermaid diagrams.
