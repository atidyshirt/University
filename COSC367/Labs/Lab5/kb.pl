% QUESTION 1
second([_,X|_],X).
% QUESTION 2
swap12([A,B|C],[B,A|C]).
% QUESTION 3
listtran([],[]).
listtran([H1|T1], [H2|T2]) :- tran(H1,H2), listtran(T1,T2).
tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).
% QUESTION 4
twice([],[]).
twice([H|T1],[H,H|T2]) :- twice(T1,T2).
% QUESTION 5
remove(X, [], []).
remove(X, [H1|T1], ListOut) :-
    =(X, H1),
    remove(X, T1, ListOut);
    remove(X, T1, Z),
    append([H1], Z, ListOut).
% QUESTION 6
split_odd_even([], [], []).
split_odd_even([A|[B|After]], [A|ListA], [B|ListB]) :-
  split_odd_even(After, ListA, ListB).
split_odd_even([A|After], [A|ListA], ListB) :-
  =(After, []),
  split_odd_even(After, ListA, ListB).
% QUESTION 7
preorder(leaf(L), [Traverse]) :- Traverse = L.
preorder(tree(R, LS, RS), [R|Traverse]) :-
  preorder(LS, LT), preorder(RS, RT),
  append(LT, RT, Traverse).
