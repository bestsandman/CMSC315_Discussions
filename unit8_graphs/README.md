# Unit 8 Discussion: Breadth-First Search (BFS)

## Implementation Summary

In this assignment, I implemented Breadth-First Search (BFS) in Python to traverse an unweighted network.

- Data Representation: Modeled a movie recommendation network with 7 nodes using an adjacency list 
(Python dictionary).
- Queue Implementation: Used collections.deque to maintain a FIFO queue structure, ensuring nodes were processed 
level by level.
- Cycle Prevention: Used a Python set to track visited nodes to avoid infinite loops and duplicate traversals.
- Graph Updates: Added a new node (Arrival) and an edge connecting it to The Martian, demonstrating how BFS expands 
dynamically to deeper levels.
- Edge Cases Tested: Validated edge cases including an empty graph, non-existent starting nodes, and disconnected 
sub-graphs.

## Discussion Board Reflection

WCompleting this assignment helped me get a clearer handle on representing graphs with adjacency lists in Python and
seeing how a queue drives the BFS traversal order. One issue I bumped into was handling missing keys cleanly without 
throwing a KeyError whenever an invalid starting node was passed or when working with disconnected pieces of the graph. 
I handled this by adding quick membership checks before running the queue loop.

Conceptually, BFS spreads out evenly across each level, making it the right pick for finding shortest paths or nearby 
neighbors. Depth-First Search (DFS), on the other hand, dives down one path as deep as it can go before backtracking.
Seeing how switching from a FIFO queue in BFS to a LIFO stack or recursion in DFS completely changes the search behavior
made the trade-offs between the two much more intuitive to understand.