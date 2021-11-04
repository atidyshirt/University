# write a predicate to check if all elements in a list are distinct

all_distinct([]) :- !.
all_distinct([H|T]) :- \+ member(H,T), all_distinct(T).

test_answer :-
    all_distinct([1,2,3,4]),
    writeln('OK').
