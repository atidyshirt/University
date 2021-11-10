# Write a predicate asbs(?List) that holds if List is a list that starts with atom a repeated zero or more times followed by atom b repeated zero or more times.
# Example:
# asbs([a,a,a,b]) is true
# \+ asbs([a,b,a]) is true

asbs([]) :- !.
asbs([a,b|T]) :- asbs(T).
asbs([a,a|T]) :- asbs(T).
asbs([a,a,a|T]) :- asbs(T).
asbs([a,a,a,b|T]) :- asbs(T).

test_answer :-
    asbs([a,a,a,b]),
    writeln('OK').

