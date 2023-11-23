% Facts about symptoms and diseases
symptom(john, fever).
symptom(john, cough).
symptom(jane, headache).
symptom(jane, fatigue).
symptom(bob, sore_throat).
symptom(bob, cough).

disease(cold, [fever, cough]).
disease(flue, [fever, cough, headache, fatigue]).
disease(tonsillitis, [sore_throat, fever]).

% Predicate to check if a person has a specific symptom
has_symptom(Person, Symptom) :-
    symptom(Person, Symptom).

% Predicate to check if a person has a specific disease
has_disease(Person, Disease) :-
    disease(Disease, Symptoms),
    forall(member(Symptom, Symptoms), has_symptom(Person, Symptom)).

% Predicate for medical diagnosis
diagnose(Person, Disease) :-
    has_disease(Person, Disease),
    format('~w is diagnosed with ~w.~n', [Person, Disease]).

% Example queries
% ?- diagnose(john, cold).
% ?- diagnose(jane, flue).
% ?- diagnose(bob, tonsillitis).
