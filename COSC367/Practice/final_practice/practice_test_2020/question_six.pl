# write a predicate to test if a binary tree is inorder or not

append([], L, L).
append([H|L1], L2, [H|L3]) :- append(L1, L2, L3).

# we halt when we reach a leaf node and traversal_HEAD is value of leaf
inorder(leaf(X), [X|[]]) :- !.
inorder(tree(Root, Left, Right), Traversal) :-
  inorder(Left, LeftTraversal),
  append(LeftTraversal, [Root], LeftRootTraversal),
  inorder(Right, RightTraversal),
  append(LeftRootTraversal, RightTraversal, Traversal).

# write a predicate to find out if the tree is preorder or not, using append predicate

preorder(leaf(X), [X|[]]) :- !.
preorder(tree(Root, Left, Right), Traversal) :-
  preorder(Left, LeftTraversal),
  append(LeftTraversal, [Root], LeftRootTraversal),
  preorder(Right, RightTraversal),
  append(LeftRootTraversal, RightTraversal, Traversal).

test_answer :- inorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
               writeln(T).
