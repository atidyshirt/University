from csp import CSP

csp_instance = CSP(
    var_domains={
        'w': {'as', 'far', 'if', 'know', 'why'},
        'x': {1, 2},
        'y': {-1, 0},
        'z': {1, 4}
    },

   constraints={
      lambda w, x, y: len(w) == x - y,
      lambda z: z % 3 == 1,
   }
)

assert type(csp_instance) is CSP
print(sorted(csp_instance.var_domains.keys()))
print(len(csp_instance.constraints))
