append([], L, L).
append([H|L1], L2, [H|L3]) :- append(L1, L2, L3).

# write a predicate even_length/1 that takes in a list and returns true if the length of the list is even.

even_length([]).
even_length([_,_|T]) :- even_length(T).

test_answer :-
    even_length([foo, bar, zoo, log]),
    writeln('OK').
