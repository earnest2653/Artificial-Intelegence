% Facts about family relationships
parent(john, jim).
parent(john, ann).
parent(mary, jim).
parent(mary, ann).
parent(jim, pat).
parent(ann, tom).

% Rules to define different relationships
father(Father, Child) :-
    parent(Father, Child),
    male(Father).

mother(Mother, Child) :-
    parent(Mother, Child),
    female(Mother).

% Define males and females in the family
male(john).
male(jim).
male(pat).
male(tom).

female(mary).
female(ann).

% Rules for other relationships (grandparent, sibling)
grandparent(Grandparent, Grandchild) :-
    parent(Grandparent, Parent),
    parent(Parent, Grandchild).

sibling(Sibling1, Sibling2) :-
    parent(Parent, Sibling1),
    parent(Parent, Sibling2),
    Sibling1 \= Sibling2.

% Example queries
% ?- father(john, jim).
% ?- mother(mary, tom).
% ?- grandparent(john, tom).
% ?- sibling(jim, ann).
