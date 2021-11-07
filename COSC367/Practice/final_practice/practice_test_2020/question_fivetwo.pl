
all_distinct([]).
all_distinct([H|T]) :-
  all_distinct(T),
  \+ member(H, T).



test_answer :-
    all_distinct([1,2,3,4]),
    writeln('OK').
