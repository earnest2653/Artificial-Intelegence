% Facts about students
student(john, cs101).
student(jane, math200).
student(bob, cs101).
student(alice, phys150).

% Facts about teachers
teacher(prof_smith, cs101).
teacher(prof_doe, math200).
teacher(prof_jones, phys150).

% Facts about subject codes
subject_code(cs101, 'Introduction to Computer Science').
subject_code(math200, 'Advanced Mathematics').
subject_code(phys150, 'Physics for Beginners').

% Predicate to find the teacher of a given subject
teaches_subject(Teacher, Subject) :-
    teacher(Teacher, Subject).

% Predicate to find the subjects a student is enrolled in
enrolled_subjects(Student, Subjects) :-
    findall(Subject, student(Student, Subject), Subjects).

% Predicate to find the subjects taught by a teacher
taught_subjects(Teacher, Subjects) :-
    findall(Subject, teacher(Teacher, Subject), Subjects).
