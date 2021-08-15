import re

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    Author: Kourosh Neshatian

    """
    ATOM   = r"[a-z][a-zA-Z\d_]*"
    HEAD   = r"\s*(?P<HEAD>{ATOM})\s*".format(**locals())
    BODY   = r"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*".format(**locals())
    CLAUSE = r"{HEAD}(:-{BODY})?\.".format(**locals())
    KB     = r"^({CLAUSE})*\s*$".format(**locals())

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")

def forward_deduce(knowledge_base):
    derived_true = set()
    knowledge_base = list(clauses(knowledge_base))
    stop_flag = False
    while 1:
        if stop_flag:
            return derived_true
        else:
            stop_flag = True
            for clause in knowledge_base:
                if clause[0] not in derived_true:
                    if clause[1] == []:
                        stop_flag = False
                        derived_true.add(clause[0])
                    else:
                        add = True
                        for body in clause[1]:
                            if body not in derived_true:
                                add = False
                        if add:
                            stop_flag = False
                            derived_true.add(clause[0])

def main():
    kb = """
    a :- b.
    b.
    """
    print(", ".join(sorted(forward_deduce(kb))))
main()
