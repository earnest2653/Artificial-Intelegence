% Rules for the example backward chaining program
rule(has_flue(X)) :-
    has_fever(X),
    has_cough(X),
    has_headache(X).

rule(has_headache(X)) :-
    symptom(X, headache).

rule(has_cough(X)) :-
    symptom(X, cough).

rule(has_fever(X)) :-
    symptom(X, fever).

% Facts about symptoms
symptom(john, fever).
symptom(jane, cough).
symptom(bob, headache).

% Backward chaining implementation
backward_chaining(Goal) :-
    solve(Goal),
    write('Goal achieved: '), write(Goal), nl.

solve(Goal) :-
    rule(Goal),
    \+ Goal,
    write('Derived: '), write(Goal), nl.

solve(Goal) :-
    rule(Goal),
    Goal.

% Example queries
% ?- backward_chaining(has_flue(john)).
% ?- backward_chaining(has_flue(bob)).
