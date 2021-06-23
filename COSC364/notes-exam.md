# Exam Revision Notes

This is exam revision notes to be condensed to a cheat sheet for the exam.;

## Networks

The nodes in the network correspond to routers, and the edges of the
network correspond to transmission links. Links will be notated with an
integer that is representing some unit of capacity *Mb/s, Gb/s, Tb/s*. This
defines the total amount of traffic that can be put on a link.

### Minimum Cost Routing Formulation

In a minimum cost example, we also have a **cost**, these costs can be associated
with an individual link or an entire path within the demand volume, for simplicity
we will apply a cost to the entire path for this example.

A cost is notated with the following notation $\phi_{path}$.

We want to find values for our decision variables $x_{12}, x_{132}$ which
**minimise** the total cost for serving the demand volume. We can now express
the minimum-cost linear program for the single-commodity problem:

$$
\begin{aligned}
 \text{min}_{[x]} & \qquad \phi_{12} x_{12} + \phi_{132} x_{132} \\
 \text{s.t} & \qquad x_{12} + x_{132} = h \\
 & \quad \quad x_{12}, x_{132} \geq 0 \\
 & \quad \quad x_{12} \leq c_{12} \\
 & \quad \quad x_{132} \leq c_{132} \\
\end{aligned}
$$

The above formulation is an example of an *optimization problem*, in which
we aim to minimise the value of the objective function for all feasible solutions.

### Load Balancing Formulation

We now establish another function by exchanging the objective function. We again
consider the network from Figure 1, but our new aim is to balance the load properly.
The goal is to make sure that path/link utilization is the same on both available paths.
Or at least as close as possible.

Path utilization can be expressed in the following fashion:

$$ \frac{x_{12}}{c_{12}}, \frac{x_{132}}{c_{132}} $$

$$
\begin{aligned}
 \text{minimise}_{[x]} & \qquad max(\frac{x_{12}}{c_{12}}, \frac{x_{132}}{c_{132}}) \\
 \text{s.t} & \qquad x_{12} + x_{132} = h \\
 & \quad \quad x_{12}, x_{132} \geq 0 \\
 & \quad \quad x_{12} \leq c_{12} \\
 & \quad \quad x_{132} \leq c_{132} \\
\end{aligned}
$$

The reason this problem formulation makes sense is because by minimising the highest
value of $x \in X$, the optimal solution will have the least distance between the possible
paths $x_{ij}$.

### Averaging Delay Formulation

If we want to minimize the average delay, then we need some idea how we can calculate the
average delay on a path. For starters, each link along a path incurs its own delay and
the delay of a path is the sum of the delays across all links within this path.

There are several factors that cause delay on a link, including the propagation delay, bitrate
of the link, router processing times, and the delay introduced by queueing packets in the router
output buffers for the link in question. Here we are only concerned with queueing delay.

The delay on a link can be expressed in the following fashion:

$$ d_{12} = \frac{x_{12}}{c_{12} - x_{12}} $$

The problem formulation is then as follows:

$$
\begin{aligned}
 \text{minimise}_{[x]} & \qquad max(\frac{x_{12}}{c_{12}}, \frac{x_{132}}{c_{132}}) \\
 \text{s.t} & \qquad x_{12} + x_{132} = h \\
 & \quad \quad x_{12}, x_{132} \geq 0 \\
 & \quad \quad x_{12} \leq c_{12} \\
 & \quad \quad x_{132} \leq c_{132} \\
\end{aligned}
$$

### Capacity Design Problems


