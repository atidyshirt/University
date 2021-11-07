#================================
# Quiz 4 : swipl files
#================================

# 1
eats(X, Y) :- likes(X, Y); edible(Y), hungry(X).

# 3
reflection(point(X1, Y1), point(X2, Y2)) :- X1 = Y2, Y1 = X2.

# 5
/* tear rate related clauses */
normal_tear_rate(RATE) :- RATE >= 5.
low_tear_rate(RATE) :- RATE < 5.

/* age-related clauses */
young(AGE) :- AGE < 45.

diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :-
    low_tear_rate(Tear_Rate), Recommend = no_lenses;
    young(Age), normal_tear_rate(Tear_Rate), Astigmatic = yes, Recommend = hard_lenses;
    young(Age), normal_tear_rate(Tear_Rate), Astigmatic = no, Recommend = soft_lenses.

# 6
directlyIn(irina, natasha).
directlyIn(natasha, olga).
directlyIn(olga, katarina).

contains(X, Y) :- directlyIn(Y, X); directlyIn(Y, Z), contains(X, Z).

# 7
solution(V1, V2, V3, H1, H2, H3) :-
    word(V1, _, V1H1, _, V1H2, _, V1H3, _),
    word(V2, _, V2H1, _, V2H2, _, V2H3, _),
    word(V3, _, V3H1, _, V3H2, _, V3H3, _),
    word(H1, _, V1H1, _, V2H1, _, V3H1, _),
    word(H2, _, V1H2, _, V2H2, _, V3H2, _),
    word(H3, _, V1H3, _, V2H3, _, V3H3, _).

# 8
mirror(X, Y) :-
    X = tree(T1, T2), Y = tree(T3, T4), mirror(T1, T4), mirror(T2, T3);
    X = leaf(B1), Y = leaf(B2), B1 = B2.



#================================
# Quiz 5 : swipl files
#================================



# 6
'''
Write a predicate addone(+ListIn, ?List) whose first argument is a list of integers,
and whose second argument is the list of integers obtained by adding 1 to each integer
in the first list. For example, the query

e.g.
?- addone([1,2,7,2], X).
X = [2,3,8,3].
'''

addone([], []).
addone([H1|T1], [H2|T2]) :- is(H2, H1 + 1), addone(T1, T2).

test_answer :-
    addone([3, 6, 7], L),
    writeln(L).

test_answer :-
    addone([1, 2, 3, 4], [2, 3, 4, 5]),
    writeln('OK').


test_answer :-
    addone([], []),
    writeln('OK').

# 7
'''
Write a predicate element(?List, ?Index, ?Value) that succeeds if Value is at position Index of List.
Assume that the first element of a list is at index zero.
'''

element([Element|_], 0, Element).
element([_|T], Index, Element) :- element(T, I, Element), is(Index, I + 1).

test_answer :-
    element([a, b, c, d, e, f], 2, X),
    writeln(X).

test_answer :-
    element([a, b, c, d], I, d),
    writeln(I).

test_answer :-
    element([a, b, c, d], 6, X),
    writeln('Wrong answer!').

test_answer :-
    writeln('OK').

test_answer :-
    element(L, I, X),
    writeln('OK').


# 8
'''
Write a predicate remove(+X, +ListIn, ?ListOut) that succeeds
if ListOut can be obtained by removing all instances of X from ListIn.
Note that the first two arguments will always be bound (input argument).
'''

remove(X, [X|T], ListOut) :- remove(X, T, ListOut).
remove(X, ListIn, ListIn) :- \+ member(X, ListIn).
remove(X, [H|T], [H|T1]) :- X \= H, remove(X, T, T1).

test_answer :-
    remove(a, [a, b, a, c, d, a, b], L),
    writeln(L).

test_answer :-
    remove(2, [2], L),
    writeln(L).

test_answer :-
    remove(d, [a, b, c], L),
    write(L).

test_answer :-
    remove(a, [], L),
    write(L).

test_answer :-
    remove(term2, [term1, term2, term3], [term1, term3]),
    write('OK').

# 9
'''
Write a predicate split_odd_even(+ListIn, ?ListA, ?ListB) whose first argument is a list,
and whose second and third arguments are the odd and even indexed elements in that list respectively.
Assume the first element of a list is indexed 1.
'''

split_odd_even([H], [H], []).
split_odd_even([], [], []).
split_odd_even([H1, H2|T], [H1|T1], [H2|T2]) :- split_odd_even(T, T1, T2).

test_answer :-
    split_odd_even([a], A, B),
    write(A),
    writeln(B).

test_answer :-
    split_odd_even([a,b,c,d,e,f,g], A, B),
    write(A),
    writeln(B).

test_answer :-
    split_odd_even([1,2,3,5], A, B),
    write(A),
    writeln(B).

# 10
'''
Write a predicate merge(+ListAIn, +ListBIn, ?List) whose first and second arguments
are lists of integers in ascending order,
and whose third argument is the list of integers obtained by merging (in order)
the first two arguments. For example, the query

?- merge([1,2,4], [2,5], X).
should give
X = [1,2,2,4,5].
Note: the first two arguments will always be instantiated.
'''

merge([H1|T1], [H2|T2], [H1|T]) :- H1 =< H2, merge(T1, [H2|T2], T).
merge([H1|T1], [H2|T2], [H2|T]) :- H1 >= H2, merge([H1|T1], T2, T).
merge([], L2, L2).
merge(L1, [], L1).
merge([], [], []).


test_answer :-
    merge([3, 6, 7], [1, 2, 3, 5, 8], L),
    writeln(L).


test_answer :-
    merge([3, 6, 7], [], L),
    writeln(L).

# 11
'''
Write a predicate merge_sort(+ListIn, ?List) whose first argument is a list of integers,
and whose second argument is the list of integers in ascending order obtained by performing merge sort.

For anyone who is unfamiliar with merge sort or needs a refresher,
merge sort works by recursively splitting a list in to two parts then merge sorting those parts
and merging the sorted parts together. The base cases are singleton lists and empty lists;
these are already sorted.

For splitting the list into two parts use the predicate
split_odd_even(+ListIn, ?ListA, ?ListB)
and for merging use the predicate
merge(+ListAIn, +ListBIn,  ?List).
Note your solution should provide these predicates.
'''
merge_sort([], []).
merge_sort([H], [H]).
merge_sort(L1, L2) :-
    split_odd_even(L1, Odd, Even),
    merge_sort(Odd, Odd_sort),
    merge_sort(Even, Even_sort),
    merge(Odd_sort, Even_sort, L2).

#===========================================
'''Another solution without split_odd_even/3 and merge/3,
but need to correct the part of remove which remove all the repeated numbers.
That leads to a problem of incorrect ordering.
'''

 min([H|T], A, Min) :- H < A, min(T, H, Min).
 min([H|T], A, Min) :- H >= A, min(T, A, Min).
 min([], A, A).

remove(X, [X|T], ListOut) :- remove(X, T, ListOut).
remove(X, ListIn, ListIn) :- \+ member(X, ListIn).
remove(X, [H|T], [H|T1]) :- X \= H, remove(X, T, T1).

merge_sort([], []).
merge_sort(L1, [Min|T]) :- min(L1, 9999, Min), remove(Min, L1, L2),
    merge_sort(L2, T).

# 12
'''
Write a predicate inside(+Min, +Max, ?X) that successively attempts to bind X to all integers
between and including the integers Min and Max. You are not allowed to use the builtin between/2
predicate (as it has near identical behaviour to the predicate you are implementing).

Note: Such predicates are useful as they allow us to perform arithmetic operations on a variable,
 a feat not possible with unbound variables. It should also be noted this can be extremely inefficient for large ranges.
'''

inside(Min, Max, X) :- Min =< Max, X = Min.
inside(Min, Max, X) :-
    Min < Max,
    is(NewMin, Min + 1),
    inside(NewMin, Max, X).

test_answer :-
    inside(1,3,2),
    writeln('OK').
#Answer : OK

test_answer: -
findall(X, inside(1, 3, X), List),
writeln(List).
#Answer : [1,2,3]

test_answer: -
findall(X, inside(1, -1, X), List),
writeln(List).


test_answer: -
findall(X, inside(1, 1, X), List),
writeln(List).

# 13
'''
A Pythagorean triple is a non-decreasing sequence of three positive integers
that are the lengths of edges of a right angle triangle.
In other words integers a, b and c form a Pythagorean triple
if 0 < a <= b <= c and a^2+b^2=c^2.

Write a predicate py_triple(+A, +B, +C) that holds iff the arguments
form a Pythagorean triple. All arguments are bound and integers.
'''
py_triple(A, B, C) :- 0 < A, A =< B, B =< C, A^2 + B^2 =:= C^2.


test_answer :-
    py_triple(3,4,5),
    write('OK').
#Answer : OK

test_answer :-
    py_triple(4,3,5),
    writeln('Incorrect, a Pythagorean triple is non-decreasing!').

test_answer :-
    py_triple(0,0,0),
    writeln('Incorrect, a Pythagorean triple contains only positive integers!').

test_answer :-
    py_triple(3,4,7),
    writeln('Incorrect!').

test_answer :-
    writeln('OK').
#Answer : OK

test_answer: -
py_triple(24, 45, 51),
write('OK').
#Answer : OK


# 14
'''
A Pythagorean triple is a non-decreasing sequence of three positive integers
that are the lengths of edges of a right angle triangle.
In other words integers a, b and c form a Pythagorean triple iff 0 < a <= b <= c and a^2+b^2=c^2.

Write a predicate py_triple(?A, ?B, ?C, +Min, +Max)
that holds iff the arguments A, B, C form a Pythagorean triple and each is between or equal to the integers Min and Max.
Note that A, B and C don't have to be bound.
In the case of multiple solutions they must be visited in ascending order of A and
then ascending order of B (e.g. A=5, B=12, C=13 must be visited before A=6, B=8, C=10).

Note: one way of testing the predicate (in addition to what you see in the test cases) is
to ask a query such as py_triple(A, B, C, 1, 100) and backtrack (by pressing semicolon) to generate more solutions.

Hint: use the predicate inside/2 from earlier (or the inbuilt predicate between/2)
to attempt to bind each of the arguments to each value from Min to Max.
'''
py_triple(A, B, C, Min, Max) :-
	between(Min, Max, A),
	between(Min, Max, B),
	between(Min, Max, C),
	0 < A, A =< B, B =< C, A^2 + B^2 =:= C^2.


test_answer :-
    findall([A,B,C],py_triple(A,B,C,1,10),List),
    writeln(List).
#Answer : [[3,4,5],[6,8,10]]



#================================
# Additional material : Prolog
#================================
# 1
'''
Write a predicate product(+Numbers, Product) that calculates the product of a list of numbers.
If the list is empty, the product is 1.
'''
product([], 1).
product([H1|T], Product) :- product(T, NewProduct), is(Product, H1 * NewProduct).

test_answer :- product([1, 2, 3], X),
               writeln(X).
#Answer : 6

test_answer :- product([], X),
               writeln(X).
#Answer : 6

test_answer :- product([-2, 5, 1, 3], X),
               writeln(X).
# 2
'''
Write a predicate binary_number(+ListOfAtoms) that only succeeds if the given list of atoms is a valid binary number.
We consider a binary number valid if it matches the following regex: 0b(0|(1(0|1)*)).
'''
binary_check([H|T]) :- member(H, [0, 1]), binary_check(T).
binary_check([]).
binary_number([0, b, 1|T1]) :- binary_check(T1).
binary_number([0, b, 0]).


test_answer :- binary_number([0, b, 1, 0, 1]),
               writeln('OK').
#Answer : OK

test_answer :- binary_number([0, b, 0, 1]),
               writeln('Wrong'), halt.

test_answer :- writeln('OK').

#Answer : OK

# 3
'''
DNA is a really big molecule that encodes all the information about an organism.
It has four bases: cytosine (c), guanine (g), adenine (a), and thymine (t).
Base c always pairs with g, and a always pairs with t,
meaning that from a single half of a DNA strand you can always build the other:
this is exactly what your body does when cells are splitting!
Write a predicate dna(?Left, ?Right) that makes sure the left and right halves of a DNA strand match.
'''

dna([a|T1], [t|T2]) :- dna(T1, T2).
dna([t|T1], [a|T2]) :- dna(T1, T2).
dna([g|T1], [c|T2]) :- dna(T1, T2).
dna([c|T1], [g|T2]) :- dna(T1, T2).
dna([], []).

test_answer :- dna([a, t, c, g], X),
               writeln(X).
#Answer : [t,a,g,c]
test_answer :- dna(X, [t, a, g, c]),
               writeln(X).
#Answer : [a,t,c,g]


# 4
'''
Write a predicate new_append(?A, ?B, ?AB) that behaves exactly the same as the built-in append/3, without using append/3.
'''

new_append([], L2, L2).
new_append([H1|T1], L2, [H1|T3]) :- new_append(T1, L2, T3).

test_answer :-
    new_append([1, 2, 3], [a, b, c], L),
    writeln(L).
#Answer : [1,2,3,a,b,c]

test_answer :-
    new_append([1, 2, 3], L, [1, 2, 3, 4, 5]),
    writeln(L).
#Answer : [4,5]

test_answer :-
    new_append(L, [a, b, c], [x, y, z, a, b, c]),
    writeln(L).
#Answer : [x,y,z]


# 5
'''
Write a predicate reversed(?Forward, ?Backward) that asserts Backward is the reverse of Forward.
It should behave identically to the built-in predicate reverse/2, but should not use this predicate.

'''


reversed([], []).
reversed([H], [H]).
reversed([H1|T1], L2) :- append(T2, [H1], L2), reversed(T1, T2).

test_answer :-
    reversed([1, 2, 3, 4, 5], L),
    writeln(L).
#Answer : [5,4,3,2,1]
test_answer :-
    reversed(L, [d, c, b, a]),
    writeln(L).
#Answer : [a,b,c,d]


# 6
'''Write a predicate max(+List, ?Max) that is true when List is a list of numbers and Max is the largest number in the list.
The predicate should be false for empty lists.

'''


max([H|T], Max, M) :- H > Max, max(T, H, M).
max([H|T], Max, M) :- H =< Max, max(T, Max, M).
max([], Max, Max).
max([H|T], M) :- max(T, 0, Max), H > Max, M = H.
max([H|T], M) :- max(T, 0, Max), H =< Max, M = Max.

test_answer :-
    max([1, 2, 3, 4, 5], M),
    writeln(M).
#Answer : 5
test_answer :-
    max([], M),
    writeln("Max of an empty list is undefined!").


# 7
'''Write a predicate preorder(+Tree, Traversal) that determines the preorder traversal of a given binary tree.
Each tree/subtree is either a leaf or of the form tree(root, left_subtree, right_subtree).
A preorder traversal records the current node, then the left branch, then the right branch.'''

preorder(leaf(X), [X]).
preorder(tree(Root, Left, Right), [Root|T]) :- preorder(Left, T1), preorder(Right, T2), append(T1, T2, T).

test_answer :- preorder(leaf(a), L),
               writeln(L).
#Answer : [a]
test_answer :- preorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
               writeln(T).
#Answer : [a,b,c,d,e]


# 8
'''Write a predicate postorder(+Tree, Traversal) that determines the postorder traversal of a given binary tree.
Each tree/subtree is either a leaf or of the form tree(root, left_subtree, right_subtree).
A postorder traversal records the left branch, then the right branch, then the current node.'''


postorder(leaf(X), [X]).
postorder(tree(Root, Left, Right), L) :- postorder(Left, T1), postorder(Right, T2), append(T1, T2, T), append(T, [Root], L).


test_answer :- postorder(tree(a, leaf(b), leaf(c)), T), writeln(T).
#Answer : [b,c,a]

test_answer :- postorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
               writeln(T).
#Answer : [c,d,b,e,a]


# 9
'''Write a predicate unique(+List, ?Set) that take a list and succeeds with Set being a list of distinct terms in List.
All the elements in the list Set must be unique (no repetition).
The order of elements in Set does not matter.'''

unique([], []).
unique([H|T], L) :- member(H, T), unique(T, L).
unique([H|T], [H|L1]) :- \+ member(H, T), unique(T, L1).


test_answer :-
    unique([1,2,1,4,3,3], Set),
    sort(Set,Sorted),
    writeln(Sorted).
#Answer : [1,2,3,4]

test_answer :-
    unique([], Set),
    sort(Set,Sorted),
    writeln(Sorted).
#Answer : []

test_answer :-
    unique([1,3,5,7,9,0,2,4,6,8],Set),
    sort(Set,Sorted),
    writeln(Sorted).
#Answer : [0,1,2,3,4,5,6,7,8,9]

test_answer :-
    unique([8],[8]),
    writeln('OK').
#Answer : OK

test_answer :-
    unique([8,8],[8]),
    writeln('OK').
#Answer : OK

test_answer :-
    unique([8,8,8],[8]),
    writeln('OK').
#Answer : OK


# 10
'''Define a predicate fib(+N, Numbers) that produces the first N Fibonacci numbers. We will never ask for less than two numbers.'''


fib_number(1, 0).
fib_number(2, 1).
fib_number(N, S) :- N1 is N - 1, N2 is N - 2, fib_number(N1, S1), fib_number(N2, S2), S is S1 + S2.
fib(2, [0, 1]).
fib(N, L) :- fib_number(N, S), NewN is N - 1, fib(NewN, L1), append(L1, [S], L).


test_answer :- fib(2, [0, 1]),
               writeln('OK').
#Answer : OK

test_answer :- fib(6, X),
               writeln(X).
#Answer : [0,1,1,2,3,5]

test_answer :- fib(10, X),
               writeln(X).
#Answer : [0,1,1,2,3,5,8,13,21,34]


# 11
'''Write a predicate rle(+LongForm, ShortForm) that creates the run-length encoding of the LongForm list.'''


rle([], []).
rle([H|T], [(H, C1)|L]) :- member(H, T), rle(T, [(H, C)|L]), C1 is C + 1.
rle([H|T], [(H, 1)|L]) :- rle(T, L).


test_answer :- rle([a, a, b, c, c, c], X),
               writeln(X).
#Answer : [ (a,2), (b,1), (c,3)]

test_answer :- rle([], []), writeln('OK').
#Answer : OK


# 12
'''Write a predicate cartesian_product(?A, ?B, ?AcrossB) that forms the cartesian product of two lists.
The cartesian product is all possible pairings of elements from the two lists.
'''


cartesian_product(A, [], []).
cartesian_product([], B, []).
cartesian_product([A|T1], [B|T2], L) :- cartesian_product([A], T2, L1), cartesian_product(T1, [B|T2], L2), append([(A, B)|L1], L2, L).

test_answer: - cartesian_product([a, b], [1, 2], X),
writeln(X).
#Answer : [(a, 1), (a, 2), (b, 1), (b, 2)]

test_answer: - cartesian_product([a, b], X,
                                 [(a, 1), (a, 2), (b, 1), (b, 2)]),
writeln(X).
#Answer : [1, 2]

test_answer: - cartesian_product([a, b, c], [1, 2, 3], X),
writeln(X).
#Answer : [(a, 1), (a, 2), (a, 3), (b, 1), (b, 2), (b, 3), (c, 1), (c, 2), (c, 3)]
