% Base case: Sum of integers from 1 to 1 is 1.
sum_integers(1, 1).

% Recursive case: Sum of integers from 1 to n is N + sum of integers from 1 to N-1.
sum_integers(N, Sum) :-
    N > 1,
    Prev is N - 1,
    sum_integers(Prev, PrevSum),
    Sum is N + PrevSum.
