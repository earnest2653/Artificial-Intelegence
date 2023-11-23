% Facts about planets
planet(mercury, 0.39, 88).
planet(venus, 0.72, 225).
planet(earth, 1.00, 365).
planet(mars, 1.52, 687).
planet(jupiter, 5.20, 4333).
planet(saturn, 9.58, 10759).
planet(uranus, 19.22, 30687).
planet(neptune, 30.05, 60190).

% Predicate to get the distance from the sun for a given planet
distance_from_sun(Planet, Distance) :-
    planet(Planet, Distance, _).

% Predicate to get the orbital period for a given planet
orbital_period(Planet, Period) :-
    planet(Planet, _, Period).
