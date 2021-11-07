from csp import CSP

csp_instance = CSP(
   var_domains = {
        "a": {1, 2},
        "b": {1, 2},
        "c": {3,4},
        "d": {1, 2, 3, 4},
        },
   constraints = {
      lambda a, b: a >= b,
      lambda a, b: b >= a,
      lambda a, b, c: c > a + b,
      lambda d: d <= d,
   }
)
