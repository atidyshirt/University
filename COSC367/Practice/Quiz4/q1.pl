likes(Y, Z).
edible(Y).
hungry(Y).
eats(Y,Z):-likes(Y,Z),edible(Z),hungry(Y).

