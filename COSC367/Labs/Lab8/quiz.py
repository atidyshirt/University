import itertools
from typing import Dict, List

def joint_prob(network: Dict, assignment: Dict) -> float:
    KEY: int = 0
    INFO: int = 1
    p: float = 1
    for var in network.items():
        parents: List[str] = []
        for parent in var[INFO]['Parents']:
            parents.append(assignment[parent])
        p *= var[INFO]['CPT'][tuple(parents)] if assignment[var[KEY]] else 1 - var[INFO]['CPT'][tuple(parents)]
    return p


def query(network: Dict, query_var: str, evidence: Dict):
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    probability: List[float] = [0, 0]
    assignment: Dict = dict(evidence) # create a partial assignment
    for query_value in {True, False}:
        TF = 1 if query_value else 0
        assignment.update({query_var: query_value})
        for values in itertools.product((True, False), repeat=len(hidden_vars)):
            hidden_assignments = {var:val for var,val in zip(hidden_vars, values)}
            assignment.update(hidden_assignments)
            probability[TF] += joint_prob(network, assignment)
    return [probability[0] / sum(probability), probability[1] / sum(probability)]
