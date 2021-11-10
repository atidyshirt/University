append([], L, L).
append([H|L1], L2, [H|L3]) :- append(L1, L2, L3).

# write a predicate same_evens that returns true if every second element in the list is the same
# The list is of even length

same_evens([]).
same_evens([T]) :- same_evens(T, H).
same_evens([_, H|T], H) :- same_evens(T, H).


test_answer :-
    same_evens([a, b, c, b, d, b]),
    same_evens([a, b]),
    same_evens([]),
    writeln('OK').
