max([], R, R).

max([X|Xs], Max, R):-
  X > Max,
  max(Xs, X, R).

max([X|Xs], Max, R):-
  X =< Max,
  max(Xs, Max, R).

max([X|Xs], R):-
  max(Xs, X, R).

test_answer :-
    max([1, 2, 3, 4, 5], M),
    writeln(M).
