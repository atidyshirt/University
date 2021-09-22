/* Base case */
mirror(leaf(X), leaf(Y)) :- X = Y.

/* Recursive step */
mirror(tree(X2, Y2), tree(X3, Y3)) :-
  /* mirror outers */
  mirror(X2, Y3),
  /* mirror inners */
  mirror(X3, Y2).
