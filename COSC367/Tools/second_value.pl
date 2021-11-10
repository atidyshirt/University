same_evens([]).
same_evens([_, _]).
same_evens([_, H, _, H|T]) :- same_evens(T).

test_answer :-
    \+ same_evens([a, b, c, b, d, c]),
    writeln('OK').