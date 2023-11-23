% Example graph represented as edges
edge(a, b, 3).
edge(a, c, 5).
edge(b, d, 2).
edge(b, e, 8).
edge(c, f, 4).
edge(d, g, 1).
edge(e, g, 7).
edge(f, g, 6).

% Heuristic values for each node
heuristic(a, 8).
heuristic(b, 6).
heuristic(c, 7).
heuristic(d, 4).
heuristic(e, 2).
heuristic(f, 5).
heuristic(g, 0).

% Best-First Search algorithm
best_first_search(Start, Goal) :-
    best_first_search([node(Start, 0, Heuristic)], Goal, []).

best_first_search([node(Goal, Cost, _)|_], Goal, Visited) :-
    reverse([node(Goal, Cost, _)|Visited], Path),
    format('Goal reached! Path: ~w~n', [Path]).

best_first_search([node(Current, Cost, _)|Rest], Goal, Visited) :-
    findall(node(Next, NewCost, NextHeuristic),
            (edge(Current, Next, StepCost),
             \+ member(Next, Visited),
             NewCost is Cost + StepCost,
             heuristic(Next, NextHeuristic)),
            Children),
    append(Children, Rest, UpdatedQueue),
    sort_queue(UpdatedQueue, SortedQueue),
    best_first_search(SortedQueue, Goal, [Current|Visited]).

% Predicate to sort the queue based on heuristic values
sort_queue(Queue, SortedQueue) :-
    predsort(compare_nodes, Queue, SortedQueue).

% Predicate to compare nodes based on heuristic values
compare_nodes(Order, node(_, Cost1, Heuristic1), node(_, Cost2, Heuristic2)) :-
    F1 is Cost1 + Heuristic1,
    F2 is Cost2 + Heuristic2,
    compare(Order, F1, F2).

% Example query
% ?- best_first_search(a, g).
