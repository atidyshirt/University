inorder(Root, [], []).

inorder(tree(Root, [], Right), Traversal) :-
    append(Root, [], Traversal),
    inorder(Right, RightTraversal),
    append(RightTraversal, [], Traversal).

inorder(tree(Root, Left, Right), Traversal) :-
    inorder(Left, LeftTraversal),
    append(LeftTraversal, [], Traversal).

test_answer :- inorder(tree(1, leaf(2), leaf(3)), T), writeln(T).

