parent(albert, bob).
parent(albert, betsy).
parent(albert, bill).

parent(alice, bob).
parent(alice, betsy).
parent(alice, bill).

parent(bob, carl).
parent(bob, charlie).

get_grandparent(Z) :-
  parent(X, Z),
  parent(Y, X),
  format("~w ~s grandparent ~n", [Y, "is the"]).

what_grade(5) :- write('Go to kindergarten').
what_grade(6) :- write('Go to 1st grade').
what_grade(Other) :- Grade is Other - 5,
format('Go to grade ~w', [Grade]).

/* similar functions that could be used */
reversed([], []).
reversed([H|T], L) :-
  reversed(T, X),
  append(X, [H], L).

new_append([],X,X).
new_append([X|Y],Z,[X|W]) :- new_append(Y,Z,W).

test_answer :-
    new_append([1, 2, 3], [a, b, c], L),
    writeln(L).
