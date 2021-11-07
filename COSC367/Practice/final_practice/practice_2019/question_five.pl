# write a predicate member(X,L) that succeeds if X is an element of the list L.

member(X,[X|_]) :- !.
member(X,[_|T]) :- member(X,T).

# write a predicate to check if a list contains a cycle

has_cycle(L) :- member(X,L), member(X,L).

test_answer :-
    \+ has_cycle([a,b,c,d,e,f]),
    writeln('OK').

test_answer :-
    writeln('Wrong!').
