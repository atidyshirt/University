\newpage

## Problem One - Conversion to standard form

### Question One

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad -9x_1 + 9x_2 + 9x_3 - 4x_4 - 4x_5 + 4x_6 \\
 \text{s.t} & \quad \quad -8x_1 + 6x_2 + 8x_3 - 9x_4 - 2x_5 + 4x_6 \geq -1 \\
 & \quad \quad -x_1 + 3x_2 + 6x_4 + 3x_6 \leq -7 \\
 & \quad \quad 8x_1 + 7x_2 - 9x_3 - 5x_4 - 3x_5 - 8x_6 \leq -6 \\
 & \quad \quad 3x_1 + 3x_2 + 2x_3 - 8x_4 + 7x_5 + 6x_6 = -1 \\
 & \quad \quad x_1 \geq 0, x_2 \geq 0, x_4 \geq 0, x_6 \geq 0
\end{aligned}
$$

First we need to remove negative constants from the right hand side of each equation
the constraints:

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad -9x_1 + 9x_2 + 9x_3 - 4x_4 - 4x_5 + 4x_6 \\
 \text{s.t} & \quad \quad 8x_1 - 6x_2 - 8x_3 + 9x_4 + 2x_5 - 4x_6 \leq 1 \\
 & \quad \quad x_1 - 3x_2 - 6x_4 - 3x_6 \geq 7 \\
 & \quad \quad -8x_1 - 7x_2 + 9x_3 + 5x_4 + 3x_5 + 8x_6 \geq 6 \\
 & \quad \quad -3x_1 - 3x_2 - 2x_3 + 8x_4 - 7x_5 - 6x_6 = 1 \\
 & \quad \quad x_1 \geq 0, x_2 \geq 0, x_4 \geq 0, x_6 \geq 0
\end{aligned}
$$

The next step to translating this equation to standard form is to remove the
inequalities. In this linear program, there are three inequalities, so we need to
create three slack variables $s_1, s_2, s+3$, we need to include these in the
objective function and use them to equalise constraints.

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad -9x_1 + 9x_2 + 9x_3 - 4x_4 - 4x_5 + 4x_6 + s_1 - s_2 - s_3 \\
 \text{s.t} & \quad \quad 8x_1 - 6x_2 - 8x_3 + 9x_4 + 2x_5 - 4x_6 + s_1 = 1 \\
 & \quad \quad x_1 - 3x_2 - 6x_4 - 3x_6 - s_2 = 7 \\
 & \quad \quad -8x_1 - 7x_2 + 9x_3 + 5x_4 + 3x_5 + 8x_6 -s_3 = 6 \\
 & \quad \quad -3x_1 - 3x_2 - 2x_3 + 8x_4 - 7x_5 - 6x_6 = 1 \\
 & \quad \quad x_1 \geq 0, x_2 \geq 0, x_4 \geq 0, x_6 \geq 0, s_1 \geq 0, s_2 \geq 0, s_3 \geq 0
\end{aligned}
$$

The last step to put this into standard form, is to remove negative variables from the linear program,
by assigning two non-negative values to any unconstrained values, we can grantee that the resulting variables
will be non-negative. The result of this process is as follows:

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad -9x_1 + 9x_2 + 9(x_3' - x_3'') - 4x_4 - 4(x_5' - x_5'') + 4x_6 + s_1 - s_2 - s_3 \\
 \text{s.t} & \quad \quad 8x_1 - 6x_2 - 8(x_3' - x_3'') + 9x_4 + 2(x_5', x_5'') - 4x_6 + s_1 = 1 \\
 & \quad \quad x_1 - 3x_2 - 6x_4 - 3x_6 - s_2 = 7 \\
 & \quad \quad -8x_1 - 7x_2 + 9(x_3' - x_3'') + 5x_4 + 3(x_5' - x_5'') + 8x_6 -s_3 = 6 \\
 & \quad \quad -3x_1 - 3x_2 - 2(x_3' - x_3'') + 8x_4 - 7(x_5' - x_5'') - 6x_6 = 1 \\
 & \quad \quad x_1 \geq 0, x_2 \geq 0, x_4 \geq 0, x_6 \geq 0, s_1 \geq 0, s_2 \geq 0, s_3 \geq 0, x_3' \geq 0, x_3'' \geq 0, x_5' \geq 0, x_5'' \geq 0
\end{aligned}
$$

The linear program above is now in standard form.

\newpage

### Question Two

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad 5x_1 - 8x_2 - 5x_3 + 9x_4 - x_5 + 6x_6 \\
 \text{s.t} & \quad \quad -2x_1 - 4x_2 + 3x_3 - 4x_4 - x_5 \geq 2 \\
 & \quad \quad -8x_1 - 10x_2 + x_3 + 3x_4 - 2x_5 + 9x_6 \leq 9 \\
 & \quad \quad 3x_1 + 4x_2 - 3x_3 + 4x_4 - 3x_5 \leq -5 \\
 & \quad \quad -7x_2 + 2x_3 + 8x_4 - x_5 + 8x_6 \leq 4 \\
 & \quad \quad x_1 \geq 0, x_3 \geq 0, x_5 \geq 0, x_6 \geq 0
\end{aligned}
$$

First we need to remove negative constants from the right hand side of each equation
the constraints:

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad 5x_1 - 8x_2 - 5x_3 + 9x_4 - x_5 + 6x_6 \\
 \text{s.t} & \quad \quad -2x_1 - 4x_2 + 3x_3 - 4x_4 - x_5 \geq 2 \\
 & \quad \quad -8x_1 - 10x_2 + x_3 + 3x_4 - 2x_5 + 9x_6 \leq 9 \\
 & \quad \quad -3x_1 - 4x_2 + 3x_3 - 4x_4 + 3x_5 \geq 5 \\
 & \quad \quad -7x_2 + 2x_3 + 8x_4 - x_5 + 8x_6 \leq 4 \\
 & \quad \quad x_1 \geq 0, x_3 \geq 0, x_5 \geq 0, x_6 \geq 0
\end{aligned}
$$

The next step to translating this equation to standard form is to remove the
inequalities. In this linear program, there are four inequalities, so we need to
create three slack variables $s_1, s_2, s_3, s_4$, we need to include these in the
objective function and use them to equalise constraints.

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad 5x_1 - 8x_2 - 5x_3 + 9x_4 - x_5 + 6x_6 - s_1 + s_2 - s_3 + s_4 \\
 \text{s.t} & \quad \quad -2x_1 - 4x_2 + 3x_3 - 4x_4 - x_5 - s_1 = 2 \\
 & \quad \quad -8x_1 - 10x_2 + x_3 + 3x_4 - 2x_5 + 9x_6 + s_2 = 9 \\
 & \quad \quad -3x_1 - 4x_2 + 3x_3 - 4x_4 + 3x_5 - s_3 = 5 \\
 & \quad \quad -7x_2 + 2x_3 + 8x_4 - x_5 + 8x_6 + s_4 = 4 \\
 & \quad \quad x_1 \geq 0, x_3 \geq 0, x_5 \geq 0, x_6 \geq 0, s_1 \geq 0, s_2 \geq 0, s_3 \geq 0, s_4 \geq 0
\end{aligned}
$$

The last step to put this into standard form, is to remove negative variables from the linear program,
by assigning two non-negative values to any unconstrained values, we can grantee that the resulting variables
will be non-negative. The result of this process is as follows:

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad 5x_1 - 8(x_2' - x_2'') - 5x_3 + 9(x_4' = x_4'') - x_5 + 6x_6 - s_1 + s_2 - s_3 + s_4 \\
 \text{s.t} & \quad \quad -2x_1 - 4(x_2' - x_2'') + 3x_3 - 4(x_4' = x_4'') - x_5 - s_1 = 2 \\
 & \quad \quad -8x_1 - 10(x_2' - x_2'') + x_3 + 3(x_4' = x_4'') - 2x_5 + 9x_6 + s_2 = 9 \\
 & \quad \quad -3x_1 - 4(x_2' - x_2'') + 3x_3 - 4(x_4' = x_4'') + 3x_5 - s_3 = 5 \\
 & \quad \quad -7(x_2' - x_2'') + 2x_3 + 8(x_4' = x_4'') - x_5 + 8x_6 + s_4 = 4 \\
 & \quad \quad x_1 \geq 0, x_3 \geq 0, x_5 \geq 0, x_6 \geq 0, s_1 \geq 0, s_2 \geq 0, s_3 \geq 0, s_4 \geq 0, x_2' \geq 0, x_2'' \geq 0, x_4' \geq 0, x_4'' \geq 0
\end{aligned}
$$

The linear program above is now in standard form.

\newpage

### Question Three

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad -2x_1 - 10x_2 + 8x_3 + 2x_4 - 3x_5 + 2x_6 \\
 \text{s.t} & \quad \quad -10x_1 + 6x_2 -6x_3 - 7x_4 - 4x_5 - 7x_6 \geq 3 \\
 & \quad \quad -6x_1 - 4x_2 + 5x_3 - 2x_4 - x_5 - 2x_6 = 2 \\
 & \quad \quad -7x_1 + x_2 - 9x_4 - 6x_5 - 8x_6 = 3 \\
 & \quad \quad 9x_1 + 3x_2 -x_3 - 6x_4 + x_5 \geq -2 \\
 & \quad \quad x_1 \geq 0, x_2 \geq 0, x_5 \geq 0, x_6 \geq 0
\end{aligned}
$$

First we need to remove negative constants from the right hand side of each equation
the constraints:

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad -2x_1 - 10x_2 + 8x_3 + 2x_4 - 3x_5 + 2x_6 \\
 \text{s.t} & \quad \quad -10x_1 + 6x_2 -6x_3 - 7x_4 - 4x_5 - 7x_6 \geq 3 \\
 & \quad \quad -6x_1 - 4x_2 + 5x_3 - 2x_4 -x_5 - 2x_6 = 2 \\
 & \quad \quad -7x_1 + x_2 - 9x_4 - 6x_5 - 8x_6 = 3 \\
 & \quad \quad -9x_1 - 3x_2 +x_3 + 6x_4 -x_5 \leq 2 \\
 & \quad \quad x_1 \geq 0, x_2 \geq 0, x_5 \geq 0, x_6 \geq 0
\end{aligned}
$$

The next step to translating this equation to standard form is to remove the
inequalities within our main constraints (excluding non-negative).
In this linear program, there are four inequalities, so we need to
create three slack variables $s_1, s_2$, we need to include these in the
objective function and use them to equalise constraints.

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad -2x_1 - 10x_2 + 8x_3 + 2x_4 - 3x_5 + 2x_6 - s_1 + s_2 \\
 \text{s.t} & \quad \quad -10x_1 + 6x_2 -6x_3 - 7x_4 - 4x_5 - 7x_6 - s_1 = 3 \\
 & \quad \quad -6x_1 - 4x_2 + 5x_3 - 2x_4 -x_5 - 2x_6 = 2 \\
 & \quad \quad -7x_1 + x_2 - 9x_4 - 6x_5 - 8x_6 = 3 \\
 & \quad \quad -9x_1 - 3x_2 +x_3 + 6x_4 -x_5 + s_2 = 2 \\
 & \quad \quad x_1 \geq 0, x_2 \geq 0, x_5 \geq 0, x_6 \geq 0, s_1 \geq 0, s_2 \geq 0
\end{aligned}
$$

The last step to put this into standard form, is to remove negative variables from the linear program,
by assigning two non-negative values to any unconstrained values, we can grantee that the resulting variables
will be non-negative. The result of this process is as follows:

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad -2x_1 - 10x_2 + 8(x_3' - x_3'') + 2(x_4' - x_4'') - 3x_5 + 2x_6 - s_1 + s_2 \\
 \text{s.t} & \quad \quad -10x_1 + 6x_2 -6(x_3' - x_3'') - 7(x_4' - x_4'') - 4x_5 - 7x_6 - s_1 = 3 \\
 & \quad \quad -6x_1 - 4x_2 + 5(x_3' - x_3'') - 2(x_4' - x_4'') -x_5 - 2x_6 = 2 \\
 & \quad \quad -7x_1 + x_2 - 9(x_4' - x_4'') - 6x_5 - 8x_6 = 3 \\
 & \quad \quad -9x_1 - 3x_2 + x_3' - x_3'' + 6(x_4' - x_4'') -x_5 + s_2 = 2 \\
 & \quad \quad x_1 \geq 0, x_2 \geq 0, x_5 \geq 0, x_6 \geq 0, s_1 \geq 0, s_2 \geq 0, x_3' \geq 0, x_3'' \geq 0, x_4' \geq 0, x_4'' \geq 0
\end{aligned}
$$

The linear program above is now in standard form.

\newpage

### Question Four

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad -4x_1 - 3x_2 - 2x_3 - 3x_4 + 9x_5 - 5x_6 \\
 \text{s.t} & \quad \quad -10x_1 - 3x_2 - 4x_3 - 5x_4 - 8x_6 \geq -7 \\
 & \quad \quad 1x_1 + 3x_2 + 4x_3 - 8x_4 + 3x_5 = 2 \\
 & \quad \quad -6x_1 - 10x_2 +x_3 - 3x_5 + 8x_6 \geq -4 \\
 & \quad \quad x_1 \geq 0, x_4 \geq 0, x_5 \geq 0, x_6 \geq 0
\end{aligned}
$$

First we need to remove negative constants from the right hand side of each equation
the constraints:

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad -4x_1 - 3x_2 - 2x_3 - 3x_4 + 9x_5 - 5x_6 \\
 \text{s.t} & \quad \quad 10x_1 + 3x_2 + 4x_3 + 5x_4 + 8x_6 \leq 7 \\
 & \quad \quad 1x_1 + 3x_2 + 4x_3 - 8x_4 + 3x_5 = 2 \\
 & \quad \quad 6x_1 + 10x_2 - x_3 + 3x_4 - 8x_6 \leq 4 \\
 & \quad \quad x_1 \geq 0, x_4 \geq 0, x_5 \geq 0, x_6 \geq 0
\end{aligned}
$$

The next step to translating this equation to standard form is to remove the
inequalities. In this linear program, there are two inequalities, so we need to
create three slack variables $s_1, s_2$, we need to include these in the
objective function and use them to equalise constraints.

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad -4x_1 - 3x_2 - 2x_3 - 3x_4 + 9x_5 - 5x_6 - s_1 + s_2 \\
 \text{s.t} & \quad \quad 10x_1 + 3x_2 + 4x_3 + 5x_4 + 8x_6 - s_1 = 7 \\
 & \quad \quad 1x_1 + 3x_2 + 4x_3 - 8x_4 + 3x_5 = 2 \\
 & \quad \quad 6x_1 + 10x_2 - x_3 + 3x_4 - 8x_6 + s_2 = 4 \\
 & \quad \quad x_1 \geq 0, x_4 \geq 0, x_5 \geq 0, x_6 \geq 0, s_1 \geq 0, s_2 \geq 0
\end{aligned}
$$

The last step to put this into standard form, is to remove negative variables from the linear program,
by assigning two non-negative values to any unconstrained values, we can grantee that the resulting variables
will be non-negative. The result of this process is as follows:

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad -4x_1 - 3(x_2' - x_2'') - 2(x_3' - x_3'') - 3x_4 + 9x_5 - 5x_6 - s_1 + s_2 \\
 \text{s.t} & \quad \quad 10x_1 + 3(x_2' - x_2'') + 4(x_3' - x_3'') + 5x_4 + 8x_6 - s_1 = 7 \\
 & \quad \quad 1x_1 + 3(x_2' - x_2'') + 4(x_3' - x_3'') - 8x_4 + 3x_5 = 2 \\
 & \quad \quad 6x_1 + 10(x_2' - x_2'') - (x_3' - x_3'') + 3x_4 - 8x_6 + s_2 = 4 \\
 & \quad \quad x_1 \geq 0, x_4 \geq 0, x_5 \geq 0, x_6 \geq 0, s_1 \geq 0, s_2 \geq 0, x_2' \geq 0, x_2'' \geq 0, x_3' \geq 0, x_3'' \geq 0
\end{aligned}
$$

The linear program above is now in standard form.

\newpage

## Problem Two - Simplex Algorithm

### Question One 

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad 14x_1 + 8x_2 + 10x_3 + 14x_4 \\
 \text{s.t} & \quad \quad 11x_1 + 7x_2 + 6x_3 + 10x_4 = 7 \\
 & \quad \quad 14x_1 + 2x_2 + 5x_3 + 6x_4 = 6 \\
 & \quad \quad 10x_1 + 5x_2 + 12x_3 + 6x_4 = 7
\end{aligned}
$$

We need to form an auxiliary problem in order to find a basic feasible solution to the problem above
This is formed below.

**Auxiliary function**

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad s_1 + s_2 + s_3 \\
 \text{s.t} & \quad \quad 11x_1 + 7x_2 + 6x_3 + 10x_4 + s_1 = 7 \\
 & \quad \quad 14x_1 + 2x_2 + 5x_3 + 6x_4 +s_2 = 6 \\
 & \quad \quad 10x_1 + 5x_2 + 12x_3 + 6x_4 +s_3 = 7 \\
 & \quad \quad x_1 \geq 0, x_2 \geq 0, x_3 \geq 0, x_4 \geq 0, s_1 \geq 0, s_2 \geq 0, s_3 \geq 0
\end{aligned}
$$

**Initialise tableau for auxiliary problem**

$$
\begin{array}{ccccccc|c}
  x_1 & x_2 & x_3 & x_4 & s_1 & s_2 & s_3 & b \\
  11 & 7 & 6 & 10 & 1 & 0 & 0 & 7 \\
  14 & 2 & 5 & 6 & 0 & 1 & 0 & 6 \\
  10 & 5 & 12 & 6 & 0 & 0 & 1 & 7 \\
  0 & 0 & 0 & 0 & 1 & 1 & 1 & 0 \\
\end{array}
$$

We plug in $x_i = 0$ for all $1 \leq i \leq m$ which gives us the obvious solution, that a feasible solution to
the auxiliary linear programing problem is when $b_i = x_i$, this gives us our initial feasible solution where
the following conditions are met:

$$x_1 = 0, x_2 = 0, x_3 = 0, x_4 = 0, s_1 = 7, s_2 = 6, s_3 = 7$$

Now we can start the simplex method to minimise the auxiliary problem. *As the tableu above contains
$z = 0$ in the bottom left corner, we know that the original Linear programming problem
has a basic feasible solution.*

**Simplex method on Auxiliary Problem**

First we need to clean out the initial tableau, this will result in $s_1 = s_2 = s_3 = 0$ in last row of the tableau,
we can achieve this by preforming arithmetic on the rows of the tableau.

$$
\begin{aligned}
R_4 - R_1 \rightarrow R_4 \\
R_4 - R_2 \rightarrow R_4 \\
R_4 - R_3 \rightarrow R_4 \\
\end{aligned}
$$

The resulting tableau of the above operations is as follows:

$$
\begin{array}{ccccccc|c}
  x_1 & x_2 & x_3 & x_4 & s_1 & s_2 & s_3 & b \\
  11 & 7 & 6 & 10 & 1 & 0 & 0 & 7 \\
  14 & 2 & 5 & 6 & 0 & 1 & 0 & 6 \\
  10 & 5 & 12 & 6 & 0 & 0 & 1 & 7 \\
  -35 & -14 & -23 & -22 & 0 & 0 & 0 & -20 \\
\end{array}
$$

We can find our pivot point by finding the largest negative and then checking the
ratio $\frac{b_i}{y_i}$ for each value $i$ within the column *q*, the element in *q*
with the lowest ratio will become the new pivot point for the proceeding operations:

**Applying the pivot**

Calculating the rows operations

$$
\begin{aligned}
\frac{1}{14}R_2 \rightarrow R_2 \\
R_1 - 11R_2 \rightarrow R_1 \\
R_3 - 10R_2 \rightarrow R_3 \\
R_1 + 35R_2 \rightarrow R_4 \\
\end{aligned}
$$

After these calculations, the new tableau is as follows:

$$
\begin{array}{ccccccc|c}
  x_1 & x_2 & x_3 & x_4 & s_1 & s_2 & s_3 & b \\
  0 & \frac{38}{7} & \frac{29}{14} & \frac{37}{7} & 1 & - \frac{11}{14} & 0 & \frac{16}{7} \\[1.5ex]
  1 & \frac{1}{7} & \frac{5}{14} & \frac{3}{7} & 0 & \frac{1}{14} & 0 & \frac{3}{7} \\[1.5ex]
  0 & \frac{25}{7} & \frac{59}{7} & \frac{12}{5} & 0 & - \frac{5}{7} & 1 & \frac{19}{7} \\[1.5ex]
  0 & -9 & - \frac{21}{2} & -7 & 0 & \frac{5}{2} & 0 & -5 \\[1.5ex]
\end{array}
$$

Because we still have negative cost values, we must repeat the pivot process, this time as the most negative value
is $-\frac{21}{2}$, we calculate the ratios and find that the lowest is $\frac{19}{59}$.

**We then calculate the next pivot**

Calculating row operations:

$$
\begin{aligned}
\frac{R_3}{\frac{59}{7}} \rightarrow R_3 \\
R_1 - \frac{29}{14}R_3 \rightarrow R_1 \\
R_2 - \frac{5}{14}R_3 \rightarrow R_2 \\
R_4 + \frac{21}{2}R_3 \rightarrow R_4 \\
\end{aligned}
$$

After these calculations, the new tableau is as follows:

$$
\begin{array}{ccccccc|c}
  x_1 & x_2 & x_3 & x_4 & s_1 & s_2 & s_3 & b \\[2ex]
  0 & \frac{537}{118} & 0 & \frac{287}{59} & 1 & - \frac{36}{59} & - \frac{29}{118} & \frac{191}{118} \\[2ex]
  1 & - \frac{1}{118} & 0 & \frac{21}{59} & 0 & \frac{6}{59} & - \frac{5}{118} & \frac{37}{118} \\[2ex]
  0 & \frac{25}{59} & 1 & \frac{12}{59} & 0 & - \frac{5}{59} & \frac{7}{59} & \frac{19}{59} \\[2ex]
  0 & - \frac{537}{118} & 0 & - \frac{287}{59} & 0 & \frac{95}{59} & \frac{147}{188} & - \frac{191}{118} \\[2ex]
\end{array}
$$

Because we still have negative cost values, we must repeat the pivot process, this time as the most negative value
is $-\frac{287}{59}$, we calculate the ratios and find that the lowest is $\frac{191}{574}$.

**We then calculate the next pivot**

Calculating row operations:

$$
\begin{aligned}
\frac{R_1}{\frac{287}{59}} \rightarrow R_1 \\
R_2 - \frac{21}{59}R_1 \rightarrow R_2 \\
R_3 - \frac{12}{59}R_1 \rightarrow R_3 \\
R_4 + \frac{287}{59}R_1 \rightarrow R_4 \\
\end{aligned}
$$

After these calculations, the final tableau is as follows:

$$
\begin{array}{ccccccc|c}
  x_1 & x_2 & x_3 & x_4 & s_1 & s_2 & s_3 & b \\[2ex]
  0 & \frac{537}{574} & 0 & 1 & \frac{59}{287} & - \frac{36}{287} & - \frac{29}{574} & \frac{191}{574} \\[2ex]
  1 & - \frac{14}{41} & 0 & 0 & - \frac{3}{41} & \frac{6}{41} & - \frac{1}{41} & \frac{8}{41} \\[2ex]
  0 & \frac{67}{287} & 1 & 0 & - \frac{12}{287} & - \frac{17}{287} & \frac{37}{287} & \frac{73}{287} \\[2ex]
  0 & 0 & 0 & 0 & 1 & 1 & 1 & 0
\end{array}
$$

Now as we have a basic feasible solution where: must remove the auxiliary variables $s_1$, $s_2$ and $s_3$ from the basis and have a basic feasible solution where:

$$ x_1 = \frac{8}{41}, x_2 = 0, x_3 = \frac{73}{287}, x_4 = \frac{191}{574}$$

We can use this as a starting initial solution for our original problem. For this we set up the new tableau:

$$
\begin{array}{cccc|c}
  x_1 & x_2 & x_3 & x_4 & b \\[2ex]
  0 & \frac{537}{574} & 0 & 1 & \frac{191}{574} \\[2ex]
  1 & - \frac{14}{41} & 0 & 0 & \frac{8}{41} \\[2ex]
  0 & \frac{67}{287} & 1 & 0 & \frac{73}{287} \\[2ex]
  14 & 8 & 10 & 14 & 0
\end{array}
$$

Once we have cleared the tableau and applied one more pivot, the resulting tableau is as follows:

$$
\begin{array}{cccc|c}
  x_1 & x_2 & x_3 & x_4 & b \\[2ex]
  0 & 1 & 0 & 0 & \frac{574}{537} \\[2ex]
  1 & 0 & 0 & 0 & \frac{8}{41} \\[2ex]
  0 & 0 & 1 & 0 & \frac{73}{287} \\[2ex]
  0 & 0 & 0 & 0 & -\frac{1276}{719} \\[2ex]
\end{array}
$$

As this has strictly non-negative relative costs anymore, we have found the optimal solution where:

$$ x_1 = \frac{170}{537}, x_2 = \frac{191}{537}, x_3 = \frac{92}{537}, x_4 = 0 $$

### Question Two

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad 0x_1 + 12x_2 + 10x_3 + 6x_4 \\
 \text{s.t} & \quad \quad 9x_1 + 14x_2 + 1x_3 + 11x_4 = 14 \\
 & \quad \quad 9x_1 + 0x_2 + 3x_3 + 6x_4 = 10 \\
 & \quad \quad 8x_1 + 5x_2 + 9x_3 + 8x_4 = 12
\end{aligned}
$$

We need to form an auxiliary problem in order to find a basic feasible solution to the problem above
This is formed below.

**Auxiliary function**

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad s_1 + s_2 + s_3 \\
 \text{s.t} & \quad \quad 9x_1 + 14x_2 + 1x_3 + 11x_4 + s_1 = 14 \\
 & \quad \quad 9x_1 + 0x_2 + 3x_3 + 6x_4 + s_2 = 10 \\
 & \quad \quad 8x_1 + 5x_2 + 9x_3 + 8x_4 +s_3 = 12 \\
 & \quad \quad x_1 \geq 0, x_2 \geq 0, x_3 \geq 0, x_4 \geq 0, s_1 \geq 0, s_2 \geq 0, s_3 \geq 0
\end{aligned}
$$

**Initialise tableau for auxiliary problem**

$$
\begin{array}{ccccccc|c}
  x_1 & x_2 & x_3 & x_4 & s_1 & s_2 & s_3 & b \\
  9 & 14 & 1 & 11 & 1 & 0 & 0 & 14 \\
  9 & 0 & 3 & 6 & 0 & 1 & 0 & 10 \\
  8 & 6 & 9 & 8 & 0 & 0 & 1 & 12 \\
  0 & 0 & 0 & 0 & 1 & 1 & 1 & 0 \\
\end{array}
$$

We plug in $x_i = 0$ for all $1 \leq i \leq m$ which gives us the obvious solution, that a feasible solution to
the auxiliary linear programing problem is when $b_i = x_i$, this gives us our initial feasible solution where
the following conditions are met:

$$x_1 = 0, x_2 = 0, x_3 = 0, x_4 = 0, s_1 = 7, s_2 = 6, s_3 = 7$$

This gives us the initial tableau:

$$
\begin{array}{ccccccc|c}
  x_1 & x_2 & x_3 & x_4 & s_1 & s_2 & s_3 & b \\
  9 & 14 & 1 & 11 & 1 & 0 & 0 & 14 \\
  9 & 0 & 3 & 6 & 0 & 1 & 0 & 10 \\
  8 & 6 & 9 & 8 & 0 & 0 & 1 & 12 \\
  0 & 0 & 0 & 0 & 1 & 1 & 1 & 0 \\
\end{array}
$$

**Simplex method on Auxiliary Problem**

First we need to clean out the initial tableau, this will result in $s_1 = s_2 = s_3 = 0$ in last row of the tableau,
we can achieve this by preforming arithmetic on the rows of the tableau.

$$
\begin{aligned}
R_4 - R_1 \rightarrow R_4 \\
R_4 - R_2 \rightarrow R_4 \\
R_4 - R_3 \rightarrow R_4 \\
\end{aligned}
$$

The resulting tableau of the above operations is as follows:

$$
\begin{array}{ccccccc|c}
  x_1 & x_2 & x_3 & x_4 & s_1 & s_2 & s_3 & b \\
  9 & 14 & 1 & 11 & 1 & 0 & 0 & 14 \\
  9 & 0 & 3 & 6 & 0 & 1 & 0 & 10 \\
  8 & 6 & 9 & 8 & 0 & 0 & 1 & 12 \\
  -26 & -20 & -13 & -25 & 1 & 1 & 1 & -36 \\
\end{array}
$$

We can find our pivot point by finding the largest negative and then checking the
ratio $\frac{b_i}{y_i}$ for each value $i$ within the column *q*, the element in *q*
with the lowest ratio will become the new pivot point for the proceeding operations:

**Applying the pivot**

Calculating the rows operations

$$
\begin{aligned}
\frac{1}{9}R_2 \rightarrow R_2 \\
R_1 - 9R_2 \rightarrow R_1 \\
R_3 - 8R_2 \rightarrow R_3 \\
R_4 + 26R_2 \rightarrow R_4 \\
\end{aligned}
$$

After these calculations, the new tableau is as follows:

$$
\begin{array}{ccccccc|c}
  x_1 & x_2 & x_3 & x_4 & s_1 & s_2 & s_3 & b \\[2ex]
  0 & 14 & -2 & 5 & 1 & -1 & 0 & 4 \\[2ex]
  1 & 0 & \frac{1}{3} & \frac{2}{3} & 0 & \frac{1}{9} & 0 & \frac{10}{9} \\[2ex]
  0 & 6 & \frac{19}{3} & \frac{8}{3} & 0 & - \frac{8}{9} & 1 & \frac{28}{9} \\[2ex]
  0 & -20 & - \frac{13}{3} & - \frac{23}{3} & 1 & \frac{35}{9} & 1 & - \frac{88}{63} \\[2ex]
\end{array}
$$

Because we still have negative relative cost values, we must repeat the pivot process, this time as the most negative value
is $-20$, we calculate the ratios and find that the lowest is $\frac{2}{7}$.

**We then calculate the next pivot**

Calculating row operations:

$$
\begin{aligned}
\frac{1}{14}R_1 \rightarrow R_2 \\
R_3 - 6R_1 \rightarrow R_3 \\
R_4 +20R_2 \rightarrow R_4 \\
\end{aligned}
$$

The resulting tableau of the above operations is as follows:

$$
\begin{array}{ccccccc|c}
  x_1 & x_2 & x_3 & x_4 & s_1 & s_2 & s_3 & b \\[2ex]
  0 & 1 & - \frac{1}{7} & \frac{5}{14} & \frac{1}{14} & - \frac{1}{14} & 0 & \frac{2}{7} \\[2ex]
  1 & 0 & \frac{1}{3} & \frac{2}{3} & 0 & \frac{1}{9} & 0 & \frac{10}{9} \\[2ex]
  0 & 0 & \frac{151}{21} & \frac{11}{21} & - \frac{3}{7} & - \frac{29}{63} & 1 & \frac{88}{63} \\[2ex]
  0 & 0 & - \frac{151}{21} & - \frac{11}{21} & \frac{17}{7} & \frac{155}{63} & 1 & - \frac{88}{63} \\[2ex]
\end{array}
$$

Because we still have negative relative cost values, we must repeat the pivot process, this time as the most negative value
is $-\frac{151}{21}$, we calculate the ratios and find that the lowest is $\frac{88}{453}$.

**We then calculate the next pivot**

Calculating row operations:

$$
\begin{aligned}
\frac{R_3}{\frac{151}{21}} \rightarrow R_3 \\
R_1 + \frac{1}{7}R_3 \rightarrow R_1 \\
R_2 - \frac{1}{3}R_3 \rightarrow R_2 \\
R_4 + \frac{151}{21}R_3 \rightarrow R_4 \\
\end{aligned}
$$

The final tableau is calculated from the above operations, and is as follows:

$$
\begin{array}{ccccccc|c}
  x_1 & x_2 & x_3 & x_4 & s_1 & s_2 & s_3 & b \\[2ex]
  0 & 1 & 0 & \frac{111}{302} & \frac{19}{302} & - \frac{73}{906} & \frac{3}{151} & \frac{142}{453} \\[2ex]
  1 & 0 & 0 & \frac{97}{151} & \frac{3}{161} & \frac{20}{151} & - \frac{7}{151} & \frac{158}{151} \\[2ex]
  0 & 0 & 1 & \frac{11}{151} & - \frac{9}{151} & - \frac{29}{453} & \frac{21}{151} & \frac{88}{63} \\[2ex]
  0 & 0 & 0 & 0 & 1 & 1 & 1 & 0 \\[2ex]
\end{array}
$$

Now as we have a basic feasible solution where: must remove the auxiliary variables $s_1$, $s_2$ and $s_3$ from the basis and have a basic feasible solution where:

$$ x_1 = \frac{158}{151}, x_2 = \frac{142}{453}, x_3 = \frac{88}{453}, x_4 = 0$$

We can use this as a starting initial solution for our original problem. For this we set up the new tableau:

$$
\begin{array}{cccc|c}
  x_1 & x_2 & x_3 & x_4 & b \\[2ex]
  0 & 1 & 0 & \frac{111}{302} & \frac{142}{453} \\[2ex]
  1 & 0 & 0 & \frac{97}{151} & \frac{158}{151} \\[2ex]
  0 & 0 & 1 & \frac{11}{151}  & \frac{88}{63} \\[2ex]
  0 & 12 & 10 & 6 & 0 \\[2ex]
\end{array}
$$

We then clean out the tableau by applying row operations as seen previously:

$$
\begin{aligned}
R_4 - 12R_1 \rightarrow R_4 \\
R_4 - 10R_2 \rightarrow R_4 \\
\end{aligned}
$$

The final resulting tableau is as follows:

$$
\begin{array}{cccc|c}
  x_1 & x_2 & x_3 & x_4 & b \\[2ex]
  0 & 1 & 0 & \frac{111}{302} & \frac{142}{453} \\[2ex]
  1 & 0 & 0 & \frac{97}{151} & \frac{158}{151} \\[2ex]
  0 & 0 & 1 & \frac{11}{151}  & \frac{88}{63} \\[2ex]
  0 & 0 & 0 & \frac{130}{151} & - \frac{2584}{453} \\[2ex]
\end{array}
$$

We now can use this resulting table to find the minimal solutions to the linear program.

$$ x_1 = \frac{142}{453}, x_2 = \frac{158}{151}, x_3 = \frac{88}{453}, x_4 = 0 $$

### Question Three

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad 3x_1 + 0x_2 + 0x_3 + 3x_4 \\
 \text{s.t} & \quad \quad 14x_1 + 10x_2 + 0x_3 + 2x_4 = 7 \\
 & \quad \quad 0x_1 + 0x_2 + 2x_3 + 14x_4 = 2 \\
 & \quad \quad 11x_1 + 3x_2 + 13x_3 + 13x_4 =10 
\end{aligned}
$$

We need to form an auxiliary problem in order to find a basic feasible solution to the problem above
This is formed below.

**Auxiliary function**

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad s_1 + s_2 + s_3 \\
 \text{s.t} & \quad \quad 14x_1 + 10x_2 + 0x_3 + 2x_4 s_1 = 7 \\
 & \quad \quad 0x_1 + 0x_2 + 2x_3 + 14x_4 + s_2 = 2 \\
 & \quad \quad 11x_1 + 3x_2 + 13x_3 + 13x_4 + s_3 = 10 \\
 & \quad \quad x_1 \geq 0, x_2 \geq 0, x_3 \geq 0, x_4 \geq 0, s_1 \geq 0, s_2 \geq 0, s_3 \geq 0
\end{aligned}
$$

**Initialise tableau for auxiliary problem**

We plug in $x_i = 0$ for all $1 \leq i \leq m$ which gives us the obvious solution, that a feasible solution to
the auxiliary linear programing problem is when $b_i = x_i$, this gives us our initial feasible solution where
the following conditions are met:

$$x_1 = 0, x_2 = 0, x_3 = 0, x_4 = 0, s_1 = 7, s_2 = 6, s_3 = 7$$

$$
\begin{array}{ccccccc|c}
  x_1 & x_2 & x_3 & x_4 & s_1 & s_2 & s_3 & b \\
  14 & 10 & 0 & 2 & 1 & 0 & 0 & 7 \\
  0 & 0 & 2 & 14 & 0 & 1 & 0 & 2 \\
  11 & 3 & 13 & 13 & 0 & 0 & 1 & 10 \\
  0 & 0 & 0 & 0 & 1 & 1 & 1 & 0 \\
\end{array}
$$

**Simplex method on Auxiliary Problem**

First we need to clean out the initial tableau, this will result in $s_1 = s_2 = s_3 = 0$ in last row of the tableau,
we can achieve this by preforming arithmetic on the rows of the tableau.

$$
\begin{aligned}
R_4 - R_1 \rightarrow R_4 \\
R_4 - R_2 \rightarrow R_4 \\
R_4 - R_3 \rightarrow R_4 \\
\end{aligned}
$$

The resulting tableau of the above operations is as follows:

$$
\begin{array}{ccccccc|c}
  x_1 & x_2 & x_3 & x_4 & s_1 & s_2 & s_3 & b \\[2ex]
  14 & 10 & 0 & 2 & 1 & 0 & 0 & 7 \\[2ex]
  0 & 0 & 2 & 14 & 0 & 1 & 0 & 2 \\[2ex]
  11 & 3 & 13 & 13 & 0 & 0 & 1 & 10 \\[2ex]
  -25 & -13 & -15 & -29 & 0 & 0 & 0 & -19 \\[2ex]
\end{array}
$$

We can find our pivot point by finding the largest negative and then checking the
ratio $\frac{b_i}{y_i}$ for each value $i$ within the column *q*, the element in *q*
with the lowest ratio will become the new pivot point for the proceeding operations:

In this case we consider $x_4$ due to $R_4$ containing the largest negative relative
cost value, we then calculate the ratios, and take the smallest one of $\frac{1}{7}$.

**Applying the pivot**

Calculating the rows operations

$$
\begin{aligned}
\frac{1}{14}R_2 \rightarrow R_2 \\
R_1 - 2R_2 \rightarrow R_1 \\
R_3 - 13R_2 \rightarrow R_3 \\
R_4 + 29R_2 \rightarrow R_4 \\
\end{aligned}
$$

After these calculations, the new tableau is as follows:

$$
\begin{array}{ccccccc|c}
  x_1 & x_2 & x_3 & x_4 & s_1 & s_2 & s_3 & b \\[2ex]
  14 & 10 & - \frac{2}{7} & 0 & 1 & - \frac{1}{7} & 0 & \frac{47}{7} \\[2ex]
  0 & 0 & \frac{1}{7} & 1 & 0 & \frac{1}{14} & 0 & \frac{1}{7} \\[2ex]
  11 & 3 & \frac{78}{7} & 0 & 0 & - \frac{13}{14} & 1 & \frac{57}{7} \\[2ex]
  -25 & -13 & - \frac{76}{7} & 0 & 0 & \frac{29}{14} & 0 & - \frac{104}{7} \\[2ex]
\end{array}
$$

Because we still have negative relative cost values, we must repeat the pivot process, this time as the most negative value
is $-25$, we calculate the ratios and find that the lowest is $\frac{47}{98}$.

**We then calculate the next pivot**

Calculating row operations:

$$
\begin{aligned}
\frac{1}{14}R_1 \rightarrow R_1 \\
R_3 - 11R_1 \rightarrow R_3 \\
R_4 + 25R_1 \rightarrow R_4 \\
\end{aligned}
$$

The resulting tableau of the above operations is as follows:

$$
\begin{array}{ccccccc|c}
  x_1 & x_2 & x_3 & x_4 & s_1 & s_2 & s_3 & b \\[2ex]
  1 & \frac{5}{7} & - \frac{1}{49} & 0 & \frac{1}{14} & - \frac{1}{98} & 0 & \frac{47}{98} \\[2ex]
  0 & 0 & \frac{1}{7} & 1 & 0 & \frac{1}{14} & 0 & \frac{1}{7} \\[2ex]
  0 & - \frac{34}{7} & \frac{557}{49} & 0 & - \frac{11}{14} & - \frac{40}{49} & 1 & \frac{281}{98} \\[2ex]
  0 & \frac{34}{7} & - \frac{49}{557} & 0 & \frac{25}{14} & \frac{89}{49} & 0 & - \frac{281}{98} \\[2ex]
\end{array}
$$

Because we still have negative relative cost values, we must repeat the pivot process, this time as the most negative value
is $-\frac{557}{49}$, we calculate the ratios and find that the lowest non-negative ratio is $\frac{28}{111}$.

**We then calculate the next pivot**

Calculating row operations:

$$
\begin{aligned}
\frac{49}{557}R_3 \rightarrow R_3 \\
R_1 + \frac{1}{49}R_3 \rightarrow R_1 \\
R_2 - \frac{1}{7}R_3 \rightarrow R_2 \\
R_4 + \frac{557}{49}R_3 \rightarrow R_4 \\
\end{aligned}
$$

The resulting tableau of the above operations is as follows:

$$
\begin{array}{ccccccc|c}
  x_1 & x_2 & x_3 & x_4 & s_1 & s_2 & s_3 & b \\[2ex]
  1 & \frac{393}{557} & 0 & 0 & \frac{39}{557} & - \frac{10}{857} & \frac{1}{557} & \frac{270}{557} \\[2ex]
  0 & \frac{34}{557} & 0 & 1 & \frac{7}{709} & \frac{62}{759} & - \frac{7}{557} & \frac{36}{337} \\[2ex]
  0 & - \frac{238}{557} & 1 & 0 & - \frac{62}{897} & - \frac{40}{557} & \frac{49}{557} & \frac{28}{111} \\[2ex]
  0 & 0 & 0 & 0 & 1 & 1 & 1 & 0 \\[2ex]
\end{array}
$$

Now that we have a Basic feasible solution to the auxiliary problem, we can use this as a starting 
initial solution for our original problem. For this we set up the new tableau:

$$
\begin{array}{cccc|c}
  x_1 & x_2 & x_3 & x_4 & b \\[2ex]
  1 & \frac{393}{557} & 0 & 0 & \frac{270}{557} \\[2ex]
  0 & \frac{34}{557} & 0 & 1 & \frac{36}{337} \\[2ex]
  0 & - \frac{238}{557} & 1 & 0 & \frac{28}{111} \\[2ex]
  3 & 0 & 0 & 3 & 0 \\[2ex]
\end{array}
$$

We then clean out the tableau by applying row operations as seen previously:

$$
\begin{aligned}
R_4 - 3R_1 \rightarrow R_4 \\
R_4 - 3R_2 \rightarrow R_4 \\
\end{aligned}
$$

The resulting tableau is as follows:

$$
\begin{array}{cccc|c}
  x_1 & x_2 & x_3 & x_4 & b \\[2ex]
  1 & \frac{393}{557} & 0 & 0 & \frac{270}{557} \\[2ex]
  0 & \frac{34}{557} & 0 & 1 & \frac{36}{337} \\[2ex]
  0 & - \frac{238}{557} & 1 & 0 & \frac{28}{111} \\[2ex]
  0 & - \frac{1281}{557} & 0 & 0 & - \frac{1276}{719} \\[2ex]
\end{array}
$$

Notice that there are still some negative relative costs within the tableau, this means that
we are not done. We must make another pivot to remove negative relative costs.

We apply the appropriate row operations:

$$ R_1 - \frac{557}{393}R_1 \rightarrow R_1 $$
$$ R_2 - \frac{34}{557}R_1 \rightarrow R_2 $$
$$ R_3 + \frac{238}{557}R_1 \rightarrow R_3 $$
$$ R_4 + \frac{1281}{557}R_1 \rightarrow R_4 $$

The final resulting table is as follows:

$$
\begin{array}{cccc|c}
  x_1 & x_2 & x_3 & x_4 & b \\[2ex]
  \frac{557}{393} & 1 & 0 & 0 & \frac{90}{131} \\[2ex]
  - \frac{34}{393} & 0 & 0 & 1 & \frac{17}{262} \\[2ex]
  \frac{238}{393} & 0 & 1 & 0 & \frac{143}{262} \\[2ex]
  \frac{427}{131} & 0 & 0 & 0 & - \frac{51}{262} \\[2ex]
\end{array}
$$

We now can use this resulting table to find the minimal solutions to the linear program.

$$ x_1 = 0, x_2 = \frac{90}{131}, x_3 = \frac{143}{262}, x_4 = \frac{17}{262} $$

### Question Four

$$
\begin{aligned}
\end{aligned}
$$

First we need to remove negative constants from the right hand side of each equation
the constraints:

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad 12x_1 + 4x_2 + 1x_3 + 1x_4 \\
 \text{s.t} & \quad \quad 11x_1 + 12x_2 + 7x_3 + 9x_4 = 12 \\
 & \quad \quad 5x_1 + 5x_2 + 10x_3 + 11x_4 = 14 \\
 & \quad \quad 2x_1 + 12x_2 + 13x_3 + 6x_4 = 9
\end{aligned}
$$

We need to form an auxiliary problem in order to find a basic feasible solution to the problem above
This is formed below.

**Auxiliary function**

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad s_1 + s_2 + s_3 \\
 \text{s.t} & \quad \quad 11x_1 + 12x_2 + 7x_3 + 9x_4 + s_1 = 12 \\
 & \quad \quad 5x_1 + 5x_2 + 10x_3 + 11x_4 + s_2 = 14 \\
 & \quad \quad 2x_1 + 12x_2 + 13x_3 + 6x_4 + s_3 = 9 \\
 & \quad \quad x_1 \geq 0, x_2 \geq 0, x_3 \geq 0, x_4 \geq 0, s_1 \geq 0, s_2 \geq 0, s_3 \geq 0
\end{aligned}
$$

We plug in $x_i = 0$ for all $1 \leq i \leq m$ which gives us an obvious solution, that a feasible solution to
the auxiliary linear programing problem is when $b_i = x_i$.

$$
\begin{array}{ccccccc|c}
  x_1 & x_2 & x_3 & x_4 & s_1 & s_2 & s_3 & b \\
  11 & 12 & 7 & 9 & 1 & 0 & 0 & 12 \\
  5 & 5 & 10 & 11 & 0 & 1 & 0 & 14 \\
  2 & 12 & 13 & 6 & 0 & 0 & 1 & 9 \\
  0 & 0 & 0 & 0 & 1 & 1 & 1 & 0 \\
\end{array}
$$

**Simplex method on Auxiliary Problem**

First we need to clean out the initial tableau, this will result in $s_1 = s_2 = s_3 = 0$ in last row of the tableau,
we can achieve this by preforming arithmetic on the rows of the tableau.

$$
\begin{aligned}
R_4 - R_1 \rightarrow R_4 \\
R_4 - R_2 \rightarrow R_4 \\
R_4 - R_3 \rightarrow R_4 \\
\end{aligned}
$$

Giving us our initial tableau to start the simplex algorithm

$$
\begin{array}{ccccccc|c}
  x_1 & x_2 & x_3 & x_4 & s_1 & s_2 & s_3 & b \\
  11 & 12 & 7 & 9 & 1 & 0 & 0 & 12 \\
  5 & 5 & 10 & 11 & 0 & 1 & 0 & 14 \\
  2 & 12 & 13 & 6 & 0 & 0 & 1 & 9 \\
  -23 & -29 & -30 & -26 & 0 & 0 & 0 & -35 \\
\end{array}
$$

We can find our pivot point by finding the largest negative and then checking the
ratio $\frac{b_i}{y_i}$ for each value $i$ within the column *q*, the element in *q*
with the lowest ratio will become the new pivot point for the proceeding operations:

In this case we consider $x_3$ due to $R_4$ containing the largest negative relative
cost value, we then calculate the ratios, of each and every $x_3$ and take the smallest
ratio of $\frac{9}{13}$, therefore $R_{3,3}$ becomes our new pivot point.

**Applying the pivot**

Calculating row operations:

$$
\begin{aligned}
\frac{1}{13}R_3 \rightarrow R_3 \\
R_1 - 7R_3 \rightarrow R_1 \\
R_2 - 10R_3 \rightarrow R_2 \\
R_4 + 30R_3 \rightarrow R_4 \\
\end{aligned}
$$

The resulting tableau of the above operations is as follows:

$$
\begin{array}{ccccccc|c}
  x_1 & x_2 & x_3 & x_4 & s_1 & s_2 & s_3 & b \\
  \frac{129}{13} & \frac{72}{13} & 0 & \frac{68}{13} & 1 & 0 & - \frac{7}{13} & \frac{93}{13} \\[2ex]
  \frac{45}{13} & - \frac{49}{13} & 0 & \frac{83}{13} & 0 & 1 & - \frac{10}{13} & \frac{92}{13} \\[2ex]
  \frac{2}{13} & \frac{12}{13} & 1 & \frac{6}{13} & 0 & 0 & \frac{1}{13} & \frac{9}{13} \\[2ex]
  - \frac{174}{13} & - \frac{17}{13} & 0 & - \frac{158}{13} & 0 & 0 & - \frac{43}{13} & - \frac{185}{13} \\[2ex]
\end{array}
$$

As we still have negative relative cost values, we must continue the process and apply another
pivot, we do this the same way as before, by choosing the most negative relative cost value,
and finding the smallest ratio of $\frac{b_i}{y_i}$.

**Applying the next pivot**

Calculating row operations:

$$
\begin{aligned}
\frac{13}{45}R_2 \rightarrow R_2 \\
R_1 - \frac{129}{13}R_2 \rightarrow R_1 \\
R_3 - \frac{2}{13}R_2 \rightarrow R_3 \\
R_4 + \frac{174}{13}R_2 \rightarrow R_4 \\
\end{aligned}
$$

The resulting tableau of the above operations is as follows:

$$
\begin{array}{ccccccc|c}
  x_1 & x_2 & x_3 & x_4 & s_1 & s_2 & s_3 & b \\
  0 & \frac{53}{3} & 0 & - \frac{188}{13} & 1 & - \frac{43}{15} & \frac{5}{3} & - \frac{197}{15} \\[2ex]
  1 & - \frac{11}{9} & 0 & \frac{83}{13} & 0 & \frac{13}{45} & - \frac{2}{9} & \frac{92}{13} \\[2ex]
  0 & \frac{12}{13} & 1 & \frac{6}{13} & 0 & 0 & \frac{1}{13} & \frac{9}{13} \\[2ex]
  0 & - \frac{53}{3} & 0 & \frac{188}{15} & 1 & \frac{73}{15} & \frac{1}{3} & \frac{197}{15} \\[2ex]
\end{array}
$$

Because we still have a negative cost value of $- \frac{53}{3}$, we must make another
pivot on the lowest ratio element of $\frac{b_i}{y_i}$. In this case with a ratio of
$\frac{197}{265}$.

**Applying the next pivot**

Calculating row operations:

$$
\begin{aligned}
\frac{3}{53}R_1 \rightarrow R_1 \\
R_2 + \frac{11}{9}R_1 \rightarrow R_2 \\
R_3 - \frac{12}{13}R_1 \rightarrow R_3 \\
R_4 + \frac{53}{3}R_1 \rightarrow R_4 \\
\end{aligned}
$$

The final resulting tableau of the above operations is as follows:

$$
\begin{array}{ccccccc|c}
  x_1 & x_2 & x_3 & x_4 & s_1 & s_2 & s_3 & b \\
  0 & 1 & 0 & - \frac{188}{265} & \frac{3}{53} & - \frac{43}{265} & \frac{5}{53} & - \frac{197}{265} \\[2ex]
  1 & 0 & 0 & \frac{259}{265} & \frac{11}{159} & \frac{24}{265} & - \frac{17}{159} & \frac{301}{265} \\[2ex]
  0 & 0 & 1 & \frac{211}{189} & - \frac{36}{689} & \frac{34}{227} & - \frac{7}{689} & \frac{1322}{959} \\[2ex]
  0 & 0 & 0 & 0 & 1 & 1 & 1 & 0 \\[2ex]
\end{array}
$$

Now that we have a Basic feasible solution to the auxiliary problem, we can use this as a starting 
initial solution for our original problem. For this we set up the new tableau:

**Solving the original posed problem**

We setup our initial tableau for the original problem

$$
\begin{array}{cccc|c}
  x_1 & x_2 & x_3 & x_4 & b \\
  0 & 1 & 0 & - \frac{188}{265} &  - \frac{197}{265} \\[2ex]
  1 & 0 & 0 & \frac{259}{265} & \frac{301}{265} \\[2ex]
  0 & 0 & 1 & \frac{211}{189} & \frac{1322}{959} \\[2ex]
  12 & 4 & 1 & 1 & 0 \\[2ex]
\end{array}
$$

We must clean out the tableau by doing the following row operations:

$$
\begin{aligned}
R_4 - 4R_1 \rightarrow R_4 \\
R_4 - 12R_2 \rightarrow R_4 \\
R_4 - 1R_3 \rightarrow R_4 \\
\end{aligned}
$$

This gives us the following tableau:

$$
\begin{array}{cccc|c}
  x_1 & x_2 & x_3 & x_4 & b \\
  0 & 1 & 0 & - \frac{188}{265} &  - \frac{197}{265} \\[2ex]
  1 & 0 & 0 & \frac{259}{265} & \frac{301}{265} \\[2ex]
  0 & 0 & 1 & \frac{211}{189} & \frac{1322}{959} \\[2ex]
  0 & 0 & 0 & \frac{2585}{287} & \frac{5825}{484} \\[2ex]
\end{array}
$$

As we still have a negative relative cost value, we must make another pivot
on $x_{4,1}$. After the appropriate row operations are done, the resulting
tableau is as follows:

$$
\begin{array}{cccc|c}
  x_1 & x_2 & x_3 & x_4 & b \\
  \frac{188}{259} & 1 & 0 & 0 & \frac{3}{37} \\[2ex]
  \frac{305}{259} & 0 & 0 & 1 & \frac{43}{37} \\[2ex]
  -\frac{827}{724} & 0 & 1 & 0 & \frac{3}{37} \\[2ex]
  \frac{2949}{320} & 0 & 0 & 0 & - \frac{58}{37} \\[2ex]
\end{array}
$$

As we have no negative relative cost values, this is our final tableau.

We now can use this resulting table to find the minimal solutions to the linear program.

$$ x_1 = 0, x_2 = \frac{3}{37}, x_3 = \frac{3}{37}, x_4 = - \frac{58}{37} $$
