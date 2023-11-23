% Initial state: monkey is at floor, monkey is not holding banana, monkey is not on the chair.
initial_state(state(at_floor, not_holding_banana, not_on_chair)).

% Final state: monkey is holding banana.
final_state(state(_, holding_banana, _)).

% Valid moves
move(state(at_floor, not_holding_banana, not_on_chair), grasp_banana, state(at_floor, holding_banana, not_on_chair)).
move(state(at_floor, not_holding_banana, not_on_chair), climb_chair, state(at_floor, not_holding_banana, on_chair)).
move(state(at_floor, holding_banana, not_on_chair), climb_chair, state(at_floor, holding_banana, on_chair)).
move(state(at_floor, holding_banana, on_chair), push_chair, state(at_floor, holding_banana, on_chair)).
move(state(at_floor, holding_banana, on_chair), go_to_floor, state(at_floor, holding_banana, not_on_chair)).
move(state(at_floor, not_holding_banana, on_chair), push_chair, state(at_floor, not_holding_banana, on_chair)).
move(state(at_floor, not_holding_banana, on_chair), go_to_floor, state(at_floor, not_holding_banana, not_on_chair)).

% Define the goal predicate
goal(State) :-
    final_state(State).

% Solve the problem using depth-first search
solve(State, _, Actions) :-
    goal(State),
    reverse(Actions, ActionsReversed),
    format('Solution: ~w~n', [ActionsReversed]).

solve(State, Visited, Actions) :-
    \+ member(State, Visited),
    move(State, Move, NextState),
    solve(NextState, [State | Visited], [Move | Actions]).

% Example query
% ?- initial_state(InitialState), solve(InitialState, [], Actions).
