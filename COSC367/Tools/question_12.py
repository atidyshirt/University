def num_crossovers(parent_expression1, parent_expression2):
  count1 = _num_crossover_helper(parent_expression1)
  count2 = _num_crossover_helper(parent_expression2)
  return count1 * count2

def _num_crossover_helper(ls):
  if type(ls) is list:
    return sum(_num_crossover_helper(child) for child in ls)
  else:
    return 1


expression1 = ['+', 12, 'x']
expression2 = ['-', 3, 6]
print(num_crossovers(expression1, expression2))