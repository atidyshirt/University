# IDK WHAT THE FUCK IS GOING ON HERE BUT IT DOESNT WORK

# write a predicate that takes in a list and determines that the elements in the
# list are installed

installed([]) :- !.
installed([H|T]) :-
    package(H),
    installed(T).

# write a predicate requires(Software, Dependencies) that takes in a list of
# software and determines that the dependencies are required

requires(Software, Dependencies) :-
    requires(Software, [], Dependencies).

# write a predicate that checks if software can be installed if it requires
# dependencies

can_be_installed(Software) :-
    requires(Software, Dependencies),
    installed(Dependencies).

requires(prolog, [cmake, yaml, ncurses]).

installed([cmake, java]).
installed([yaml, json]).
installed([vim, emacs]).
installed([ncurses]).

test_answer :-
    can_be_installed(prolog),
    writeln("OK").

test_answer :-
    \+ can_be_installed(prolog),
    writeln("Wrong!").
