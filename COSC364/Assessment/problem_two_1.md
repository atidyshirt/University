## Problem Two - Simplex Algorithm

#### 1. Solve the following Linear Programming instance

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad 14_{x1} + 8_{x2} + 10_{x3} + 14_{x4} \\
 \text{s.t} & \quad \quad 11_{x1} + 7_{x2} + 6_{x3} + 10_{x4} = 7 \\
 & \quad \quad 14_{x1} + 2_{x2} + 5_{x3} + 6_{x4} = 6 \\
 & \quad \quad 10_{x1} + 5_{x2} + 12_{x3} + 6_{x4} = 7
\end{aligned}
$$

We need to form an auxiliary problem in order to find a basic feasible solution to the problem above
This is formed below.

**Auxiliary function**

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad s_1 + s_2 + s_3 \\
 \text{s.t} & \quad \quad 11_{x1} + 7_{x2} + 6_{x3} + 10_{x4} + s_1 = 7 \\
 & \quad \quad 14_{x1} + 2_{x2} + 5_{x3} + 6_{x4} +s_2 = 6 \\
 & \quad \quad 10_{x1} + 5_{x2} + 12_{x3} + 6_{x4} +s_3 = 7 \\
 & \quad \quad x_1 \geq 0, x_2 \geq 0, x_3 \geq 0, x_4 \geq 0, s_1 \geq 0, s_2 \geq 0, s_3 \geq 0
\end{aligned}
$$

**Initialise tableau for auxiliary problem**

$$
\begin{array}{ccccccc|c}
  a_1 & a_2 & a_3 & a_4 & a_5 & a_6 & a_7 & b \\
  11 & 7 & 6 & 10 & 1 & 0 & 0 & 7 \\
  14 & 2 & 5 & 6 & 0 & 1 & 0 & 6 \\
  10 & 5 & 12 & 6 & 0 & 0 & 1 & 7 \\
  0 & 0 & 0 & 0 & 1 & 1 & 1 & 0 \\
\end{array}
$$

We plug in $x_i = 0$ for all $1 \leq i \leq m$ which gives us the obvious solution, that a feasible solution to
the auxiliary linear programing problem is when $y_i = b_i$, this gives us our initial feasible solution where
the following conditions are met:

$$x_1 = 0, x_2 = 0, x_3 = 0, x_4 = 0, s_1 = 7, s_2 = 6, s_3 = 7$$

Now we can start the simplex method to minimise the auxiliary problem. *As the tableu above contains
$z = 0$ in the bottom left corner, we know that the original Linear programming problem
has a basic feasible solution.*

**Simplex method on Auxiliary Problem**

First we need to clean out the initial tableau, this will result in $a_5 = a_6 = a_7 = 0$ in last row of the tableau,
we can achieve this by preforming arithmetic on the rows of the tableau.

$$ 
\begin{aligned}
R_4 \rightarrow R_4 - R_1 = & \ [-11, -7, -6, -10, 0, 1, 1] \\
R_4 \rightarrow R_4 - R_2 = & \ [-25, -9, -11, -16, 0, 0, 1] \\
R_4 \rightarrow R_4 - R_3 = & \ [-11, -7, -6, -10, 0, 1, 1] \\
\end{aligned}
$$

The resulting tableau of the above operations is as follows:

$$
\begin{array}{ccccccc|c}
  a_1 & a_2 & a_3 & a_4 & a_5 & a_6 & a_7 & b \\
  11 & 7 & 6 & 10 & 1 & 0 & 0 & 7 \\
  14 & 2 & 5 & 6 & 0 & 1 & 0 & 6 \\
  10 & 5 & 12 & 6 & 0 & 0 & 1 & 7 \\
  -35 & -14 & -23 & -22 & -22 & 0 & 0 & -20 \\
\end{array}
$$

We continue the simplex method by finding the most negative value within the
relative cost coefficients, if their are no non-negative solutions, we have
reached the optimal solution. As we can see there are many negative cost co-efficents,
we pick the most negative one and let that be some variable $q$.

Consider the elements in this column and find the lowest quotient for $\frac{y_i}{b_i}$, the element that has the
lowest ratio is the element in which we will apply the pivot.

Candidates: $a_{1,1} = \frac{11}{7}, a_{1,2} = \frac{14}{6}, a_{1,3} = \frac{10}{7}$, as $\frac{10}{7} \leq \frac{11}{7} \leq \frac{16}{6}$, then the element $a_{1,3}$
is the pivot point for this iteration.

**Applying the pivot**



