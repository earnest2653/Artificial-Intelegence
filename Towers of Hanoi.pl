% Define the Hanoi predicate with three parameters:
% - N: the number of disks to move
% - From: the source peg
% - To: the destination peg
% - Via: the auxiliary peg
hanoi(1, From, To, _) :-
    write('Move disk 1 from '), write(From), write(' to '), write(To), nl.
hanoi(N, From, To, Via) :-
    N > 1,
    M is N - 1,
    hanoi(M, From, Via, To),
    write('Move disk '), write(N), write(' from '), write(From), write(' to '), write(To), nl,
    hanoi(M, Via, To, From).

% Define a predicate to start the Hanoi with the given number of disks.
start_hanoi(N) :-
    hanoi(N, 'A', 'C', 'B').

% Example usage:
% To move 3 disks from peg A to peg C:
% ?- start_hanoi(3).
