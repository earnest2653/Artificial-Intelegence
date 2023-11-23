% Rules for the example forward chaining program
rule(has_fever(X)) :-
    symptom(X, fever).

rule(has_cough(X)) :-
    symptom(X, cough).

rule(has_headache(X)) :-
    symptom(X, headache),
    has_fever(X).

rule(has_flue(X)) :-
    has_fever(X),
    has_cough(X),
    has_headache(X).

% Facts about symptoms
symptom(john, fever).
symptom(jane, cough).
symptom(bob, headache).

% Forward chaining implementation
forward_chaining :-
    repeat,
    (apply_rules, !; true),
    write('No more rules can be applied.').
    
apply_rules :-
    rule(NewFact),
    \+ NewFact,
    assertz(NewFact),
    write('Derived: '), write(NewFact), nl.

% Example queries
% ?- forward_chaining.
