from csp import *
import copy, itertools

def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    to_do = {(x, c) for c in csp.constraints for x in scope(c)} # COMPLETE
    while to_do:
        x, c = to_do.pop()
        ys = scope(c) - {x}
        new_domain = set()
        for xval in csp.var_domains[x]: # COMPLETE
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c):
                    new_domain.add(xval) # COMPLETE
                    break
        if csp.var_domains[x] != new_domain:
            for cprime in set(csp.constraints) - {c}:
                if x in scope(cprime):
                    for z in scope(cprime): # COMPLETE
                        if x != z: # COMPLETE
                            to_do.add((z, cprime))
            csp.var_domains[x] = new_domain     #COMPLETE
    return csp

csp_instance = CSP(
   var_domains = {
        "a": {2,3,4},
        "b": {1,2},
        "c": {2,3,4},
        "d": {1,2,3,4},
    },

   constraints = {
      lambda b, c: b < c,
      lambda a, b, c: b * c == a,
   }
)

csp_instance_og = CSP(
   var_domains = {
        "a": {1, 2,3,4},
        "b": {1,2,3,4},
        "c": {1,2,3,4},
        "d": {1,2,3,4},
    },

   constraints = {
      lambda b, c: b < c,
      lambda a, b, c: b * c == a,
   }
)
print(arc_consistent(csp_instance_og))

