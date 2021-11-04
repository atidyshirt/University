inorder(tree(a, tree(b, tree(c, nil, nil), nil), tree(d, nil, nil))).

test_answer :- inorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
               writeln(T).

