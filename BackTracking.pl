% Facts about fruits and their colors
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(watermelon, green).

% Predicate to query the color of a fruit
fruit_color_query(Fruit, Color) :-
    fruit_color(Fruit, Color).

% Backtracking predicate to find all fruits and their colors
all_fruit_colors(Fruit, Color) :-
    fruit_color(Fruit, Color).

% Example queries
% ?- fruit_color_query(apple, Color).
% ?- all_fruit_colors(Fruit, Color).
