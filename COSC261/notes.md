---
title: "Formal Languages and Compilers"
author: [Jordan Pyott]
date: "2022-01-21"
subject: "COSC261"
lang: "en"
titlepage: true
titlepage-color: "3C9F53"
titlepage-text-color: "FFFFFF"
titlepage-rule-color: "FFFFFF"
titlepage-rule-height: 2
---

\newpage

# Course Information

## Course Staff

- Coordinator/Lecturer
  * Walter Guttmann
    + 033692451
    + walter.guttmann@canterbury.ac.nz

## Assessments and Grading

**Grading policy**

1. You mist achieve an average grade of at least 50% over all assessment items
2. You mist achieve an average grade of at least 45% over all invigilated assessments

**Assessment Items**

- Quizzes (15%)
- Assignment Superquiz (10%)
- Lab Test (15%)
- Final Exam (60%)

## Textbooks/Resources

No textbooks are required, but see the following book for additional information:

- [Carol Critchlow and David Eck; Foundationals of Computation; version 2.3.1, 2011](https://math.hws.edu/FoundationsOfComputation)

\newpage

# Lectures

## Lecture One - Introduction

**Topic overview of the course**

- pattern matching
  * Regular expressions describe patterns
  * Search using REGEX is supported in many programs
  * Can all patterns be described by regular expressions? 
  * One to one with state diagrams and automata
- Compilers
  * Progreams can be run by an interpreter or by compiling them first 
  * Interpreting may be slow
  * Compiling to machine code avoids much of the overhead
  * Compiler performs analysis, code generation and optimisation
  * How can these tasks be automated for different programming languages?
- Syntax analysis
  * Analyses code to determine if the syntax is correct for compiling, this is done by using
  context free grammers *there are other methods of doing this however this is the main one we
  will look at in this course*
  * *does the syntax conform to the languages grammar?*
  * Ideally we want to generate the parser for our language, we will look into how to manually like are
  parser and how regular expressions and pattern matching can be used to evaluate this behaviour.
- Code generation
  * There are formalisms that exist to generate code in order to create compilers via code generation.

\newpage

## Lecture Two - Finite Automata and Regular Languages: Symbols, Strings and Languages

**Languages**

- An alphabet $\Sigma$ is non-empty finite set of *symbols*/
- A string over $\Sigma$ is a finite sequence of symbols from $\Sigma$
- The length of $|\sigma|$ of a string $\sigma$ is the number of symbols in $\sigma$
- The empty string $\epsilon$ is the unique set of length 0
- $\Sigma^{*}$ is the set of all strings over $\Sigma$
- A language $L$ over $\Sigma$ is a set of strings $L \subseteq \Sigma^{\*}$

![Example](./Diagrams/languages.png)

- Note that with a finite alphabet we can have an infinite size for $\Sigma^{\*}$
  * This is because we have not specified a size for our length of elements within $\Sigma^{\*}$

> An example of a set that we might use is the unicode set as Sigma.

For example:

- $python \subset UNICODE$
- $english \subset UNICODE$

Because of this relationship, we can use filtering, searching and `REGEX` in order to
manipulate and set rules around this relationship (or syntax in the case of programming
languages by using comparisons and combination of formalisms.

Let $a, b \in \Sigma$ be symbols and let $x, y, z \in \Sigma^{\*}$ be strings.
- Symbols and strings can be concatenated by writing one after the other
- $xy$ is the concatenated version of $x$ and $y$.
  - Note that concatenation is accociative
- $\epsilon$ is an identity for concatenation $\epsilon x = x = x \epsilon$
- $|xy| = |x| + |y|$

**Lifting to a set**

$Let A,B \subseteq \Sigma^{\*}$ be languages:

- concatenate languages $A$ and $B$ by conciliating each string from $A$ with each from $B$
- $AB = \{xy | x \in A, y \in B\}$
- Language concatenation is associative
- $\{\epsilon\}$ is the identity of language concatenation
  * $x^0 = \epsilon$

![Lifting Example](./Diagrams/lifting.png)

**Concatenation can be iterated**

- $a^n$ is the string comprising $n$ copies of the symbol $a \in \Sigma$
- $x^n$ is the string that concatinates $n$ copies of the string $x \in \Sigma^{\*}$
- These operations are defined *inductively*
- The base case is $x^0 = \epsilon$ 
- The *inductive case* is $x^{n+1} = x^n x$

Example: $a^5 = aaaaa$

![Powers of Language](./Diagrams/powers_of_language.png)

> Take aways, the * symbol means that we have zero or more of something, + means that we have
> one or more of something (this is how we use this notation practically in regex expressions

**Key notation and definitions**

- Sets are languages
- variables are strings
- variables with index are symbols

\newpage

## Lecture Three - Finite Automata and Regular Languages: Introduction to Deterministic Finite Automata

A *deterministic finite automaton (DFA)* is a structure $M = (Q, \Sigma, \delta, q_0, F)$ where:

- $Q$ is a non-empty finite set, the *states*,
- $\Sigma$ is a non-empty finite set, the *input alphabet*
- $\delta : Q \times \Sigma \rightarrow Q$ is the *transition funtion*
- $q_0 \in Q$ is the *start state*,
- $F \subseteq Q$ is the set of *accept states* or *final states*.

This can be shown in a *transition diagram* for a visual indication of how this might work:

> see lecture 3, 14:00 minutes for information on how to construct these transition diagrams

### Deterministic Finite Automata Example

Ex 1: The following DFA accepts strings over $\{a,b\}$.

![Sink state diagram](./Diagrams/sink_state.png){width=50%}


Note, we are trying to conatain an automata that is as least complicated as possible (least nodes).
In the above example, we have this concept of a true state and a false state to the specified condition.
We can also note that state $q_1$ is a *sink state* as once we reach $q_1$ it is impossible to leave that
state (*this is because the condition specifies that we need to contain 0 b's*). 

Ex 2: DFA accepting all strings over $\{a,b\}$ with a number of $a$-symbols that is not a multiple of 4.


![Modulo four example](./Diagrams/modulo_four_example.png){width=50%}


\newpage

## Lecture Four - Finite Automata and Regular Languages: Closure of properties of Deterministic Finite Automata

**Exptended transition function**

$$ \hat{\delta} : Q \times \Sigma^{\*} \rightarrow Q$$
$$\hat{\delta}(q, \epsilon) = q$$
$$\hat{\delta}(q, ax) = \hat{\delta}(\delta(q, a), x) \quad where \quad a \in \Sigma, x \in \Sigma^{\*}$$

Now we have seen the basics of DFA's, so how do we get from these basic models to something
that is more complicated? We can use a combination of DFA's in order to define more complicated systems.

**Regular languages are closed under:**

- complement
  * All strings that are not in the set, (generic approach to create such an atomaton)
  * We can get the complement by swapping accepting and non-accepting states
  * If we have a regular language, we know that the complement will always be regular
    + Formal proof provided in `Lecture Four: 27:10`
- intersection *or product automaton*
  * We can combine two automata using an *intersection*, we can use set theory in order
  to satisfy two automata at the same time. We want to check with one automataon to see if
  the string is satisfied
  * $X \cap Y$ is regular if both $X$ and $Y$ are regular
  * Accept states are defined as an acceptance of **both** automata, not just one
  * The product automaton accepting the intersection of the two languages is (*synchronous*):
    * Example found in `Lecture Four: 41:00`
- union
- concatenation
- star

\newpage

## Lecture Five - Finite Automata and Regular Languages: Non-Deterministic Finite Automata

The following automaton accepts strings with a symbol 1 in the third position from the end.
It is not a DFA because there are two 1-transitions in state $q_0$ and no transitions in state 
$q_3$.

- **DFA defined by**: $\delta : Q \times \Sigma \rightarrow Q$
- **NFA defined by**: $\delta : Q \times \Sigma \rightarrow P(Q)$
  * where $P(Q) = \{S | S \subseteq Q\}$, $P(Q)$ is also called the *power set*


![Non-Deterministic Finite Automata](./Diagrams/non-deterministic_finite_automata.png)


Here is an example of the above transition relation:

| $\delta$     | `         0          ` | `          1          ` |
| ------------ | ------------           | ------------            |
| $q_0$        | {$q_0$}                | {$q_0, q_1$}            |
| $q_1$        | {$q_2$}                | {$q_2$}                 |
| $q_2$        | {$q_3$}                | {$q_3$}                 |
| $q_3$        | {$\emptyset$}          | {$\emptyset$}           |


![Possible transition states of this non-deterministic finite automata](./Diagrams/possible_transition_states.png)


