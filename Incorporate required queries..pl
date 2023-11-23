% Facts about birds
bird(canary).
bird(penguin).
bird(albatross).

% Facts about flying capability
can_fly(canary).
can_fly(albatross).
cannot_fly(penguin).

% Predicate to check if a bird can fly
can_fly_or_not(Bird) :-
    (can_fly(Bird) -> 
        format('~w can fly.~n', [Bird])
    ;   
        format('~w cannot fly.~n', [Bird])
    ).

% Example queries
% ?- can_fly_or_not(canary).
% ?- can_fly_or_not(penguin).
% ?- can_fly_or_not(albatross).
