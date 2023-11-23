% Database of names and dates of birth
dob(john, '1990-05-15').
dob(jane, '1985-12-10').
dob(bob, '2000-02-28').
dob(alice, '1998-08-20').

% Query to get the date of birth for a given person
get_dob(Person, DateOfBirth) :-
    dob(Person, DateOfBirth).
