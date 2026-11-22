# Selection Sort — Visual Walkthrough

## Initial Array

```mermaid
flowchart LR
    A["29"] --- B["10"] --- C["14"] --- D["8"] --- E["5"]

    classDef unsorted fill:#D6D6D6,stroke:#555,color:#000
    class A,B,C,D,E unsorted
```

Array: `[29, 10, 14, 8, 5]`

---

## Pass 1 — Find the Smallest

The smallest element is `5`.

Remove it from the array and append it to the new sorted array.

```mermaid
flowchart LR
    A["29"] --- B["10"] --- C["14"] --- D["8"] --- E["5"]

    classDef smallest fill:#FFB6C1,stroke:#C0392B,color:#000
    classDef unsorted fill:#D6D6D6,stroke:#555,color:#000

    class E smallest
    class A,B,C,D unsorted
```

**Remove `5`:**

```mermaid
flowchart LR
    A["29"] --- B["10"] --- C["14"] --- D["8"]

    classDef unsorted fill:#D6D6D6,stroke:#555,color:#000
    class A,B,C,D unsorted
```

**New array:**

```mermaid
flowchart LR
    A["5"] --- B["29"] --- C["10"] --- D["14"] --- E["8"]

    classDef sorted fill:#90EE90,stroke:#228B22,color:#000
    classDef unsorted fill:#D6D6D6,stroke:#555,color:#000

    class A sorted
    class B,C,D,E unsorted
```

`[5]`

---

## Pass 2 — Find the Next Smallest

Remaining array: `[29, 10, 14, 8]`

The smallest element is `8`.

```mermaid
flowchart LR
    A["29"] --- B["10"] --- C["14"] --- D["8"]

    classDef smallest fill:#FFB6C1,stroke:#C0392B,color:#000
    classDef unsorted fill:#D6D6D6,stroke:#555,color:#000

    class D smallest
    class A,B,C unsorted
```

Remove `8` and append it to the new array.

```mermaid
flowchart LR
    A["5"] --- B["8"] --- C["29"] --- D["10"] --- E["14"]

    classDef sorted fill:#90EE90,stroke:#228B22,color:#000
    classDef unsorted fill:#D6D6D6,stroke:#555,color:#000

    class A,B sorted
    class C,D,E unsorted
```

`[5, 8]`

---

## Pass 3 — Find the Next Smallest

Remaining array: `[29, 10, 14]`

The smallest element is `10`.

```mermaid
flowchart LR
    A["29"] --- B["10"] --- C["14"]

    classDef smallest fill:#FFB6C1,stroke:#C0392B,color:#000
    classDef unsorted fill:#D6D6D6,stroke:#555,color:#000

    class B smallest
    class A,C unsorted
```

Remove `10` and append it.

```mermaid
flowchart LR
    A["5"] --- B["8"] --- C["10"] --- D["29"] --- E["14"]

    classDef sorted fill:#90EE90,stroke:#228B22,color:#000
    classDef unsorted fill:#D6D6D6,stroke:#555,color:#000

    class A,B,C sorted
    class D,E unsorted
```

`[5, 8, 10]`

---

## Pass 4 — Final Element

Remaining array: `[29, 14]`

The smallest element is `14`.

```mermaid
flowchart LR
    A["29"] --- B["14"]

    classDef smallest fill:#FFB6C1,stroke:#C0392B,color:#000
    classDef unsorted fill:#D6D6D6,stroke:#555,color:#000

    class B smallest
    class A unsorted
```

Remove `14` and append it.

```mermaid
flowchart LR
    A["5"] --- B["8"] --- C["10"] --- D["14"] --- E["29"]

    classDef sorted fill:#90EE90,stroke:#228B22,color:#000

    class A,B,C,D,E sorted
```

`[5, 8, 10, 14]`

---

## Final Step

Only `29` remains.

```mermaid
flowchart LR
    A["5"] --- B["8"] --- C["10"] --- D["14"] --- E["29"]

    classDef sorted fill:#90EE90,stroke:#228B22,color:#000

    class A,B,C,D,E sorted
```

Append the final element.

# Final Sorted Array

```mermaid
flowchart LR
    A["5"] --- B["8"] --- C["10"] --- D["14"] --- E["29"]

    classDef sorted fill:#90EE90,stroke:#228B22,color:#000

    class A,B,C,D,E sorted
```

`[5, 8, 10, 14, 29]`

---

## Algorithm Overview

```mermaid
flowchart TD
    A["Start with unsorted array"] --> B["Find smallest element"]
    B --> C["Remove smallest element"]
    C --> D["Append to new array"]
    D --> E{"Any elements left?"}
    E -->|Yes| B
    E -->|No| F["Sorted array"]

    classDef process fill:#D6EAF8,stroke:#2874A6,color:#000
    classDef decision fill:#F9E79F,stroke:#B7950B,color:#000
    classDef finish fill:#90EE90,stroke:#228B22,color:#000

    class B,C,D process
    class E decision
    class F finish
```

## Complexity

For an array of size `n`:

| Property | Complexity |
|---|---|
| Comparisons | $n(n−1)/2$ |
| Time | $O(n²)$ |
| Space | $O(n)$ — new array implementation |

For `n = 5`:

$$
\frac{5(5-1)}{2} = 10
$$

**10 comparisons** are needed in the standard implementation.
