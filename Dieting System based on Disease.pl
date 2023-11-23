% Facts about diseases and recommended diets
diet_for_disease(diabetes, 'Low-carb diet. Increase fiber intake.').
diet_for_disease(hypertension, 'Low-sodium diet. Increase potassium intake.').
diet_for_disease(high_cholesterol, 'Low-cholesterol diet. Increase omega-3 fatty acids.').
diet_for_disease(celiac_disease, 'Gluten-free diet. Increase consumption of fruits, vegetables, and lean proteins.').
diet_for_disease(vegetarian, 'Plant-based diet. Ensure adequate protein intake from plant sources.').
diet_for_disease(vegan, 'Plant-based diet excluding all animal products. Ensure adequate protein and B12 intake.').

% Predicate to suggest a diet for a given disease
suggest_diet(Disease, Diet) :-
    diet_for_disease(Disease, Diet),
    format('For ~w, it is recommended to follow: ~w~n', [Disease, Diet]).

% Example queries
% ?- suggest_diet(diabetes, Diet).
% ?- suggest_diet(vegetarian, Diet).
