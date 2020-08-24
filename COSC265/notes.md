<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [COSC265 Notes - Database Management](#cosc265-notes---database-management)
    - [General Info About Course](#general-info-about-course)
      - [Gradings](#gradings)
      - [Resources](#resources)
    - [Introduction to Databases](#introduction-to-databases)
      - [Data Management](#data-management)
        - [Example Database](#example-database)
        - [DBMS Functionality](#dbms-functionality)
        - [Schema's and Instances](#schemas-and-instances)
        - [Database Features](#database-features)
        - [Data Models](#data-models)
      - [Classification of DBMS's](#classification-of-dbmss)
      - [Don't Bother using DBMS for these Scenario's](#dont-bother-using-dbms-for-these-scenarios)
    - [Database Design](#database-design)
      - [Data Modeling](#data-modeling)
        - [Phases of Database Design](#phases-of-database-design)
      - [Types of attributes](#types-of-attributes)
        - [The `NULL` Value](#the-null-value)
      - [Introduction to Relationships](#introduction-to-relationships)
        - [Dependent's](#dependents)
      - [Relationship Diagrams](#relationship-diagrams)
        - [Syntax of Diagrams](#syntax-of-diagrams)
        - [Shit I need to know](#shit-i-need-to-know)
        - [ER to Relational Mapping Algorithm](#er-to-relational-mapping-algorithm)
    - [Relational Algebra](#relational-algebra)
      - [The Pie Operand](#the-pie-operand)
    - [The Omega Operand](#the-omega-operand)
      - [Cartesian Product](#cartesian-product)
      - [Complete set of relational algebra operations](#complete-set-of-relational-algebra-operations)
    - [SQL](#sql)
      - [Logical Design](#logical-design)
      - [Division](#division)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

<center>

# COSC265 Notes - Database Management

</center>

### General Info About Course

#### Gradings
- Assessment part 1 8% (8/8/2020, 5PM)
- Assessment part 2 16% (21/8/2020, 5PM)
- Quizzes 6% (multiple quizzes)
- Lab Test 20% (1st October, 7PM)
- Final Exam 50% (To be announced)

#### Resources
- [Lecture Notes](https://learn.canterbury.ac.nz/course/view.php?id=8959&section=1)
- [Labs and Tutorials](https://learn.canterbury.ac.nz/course/view.php?id=8959&section=2)
- [Homework Material](https://learn.canterbury.ac.nz/course/view.php?id=8959&section=4)
- [Previous Exams](https://learn.canterbury.ac.nz/course/view.php?id=8959&section=2)

### Introduction to Databases 

#### Data Management
- Entity
    - Is something that we have to collect data about
- Attribute
    - Is something we assign to a value, ie if we have an entity called person, 
      the person will have a name attribute
- Data
    - Must be well organized
    - we need to have a system in order to access it efficiently
- Record

**Why We Use Databases**

We use databases to store our information rather then files, this is because
working with files becomes a problem for a number of reasons, these include
having information located in different files and locations. This is a problem
for querying information and manipulating data.

**Database Management System (DBMS)**

Is a system to manage and create databases, the most common one is Oracle. This is also
responsible for managing traffic and making sure that multiple people on the same system
cannot make conflicting changes to the database.

**Database Software**

This is inclusive of applications used to manipulate the database as well as the DBMS.
A DBMS is a general software, it is possible to have many databases on each DBMS. In
the labs we will use the Oracle database.

##### Example Database
Entities
- Course
- section
- grade_report
- prerequisite

**Here is an example of an Entity**

| course_name               | course_number | credit | department |
| -----------               | ------------- | ------ | ---------- |
| Intro to computer science | CS1310        | 4      | CS         |
| Data Structures           | CS1120        | 3      | CS         |
| Discrete Mathematics      | MA2220        | 5      | MATH       |

##### DBMS Functionality

- Define database:
- Construct or load databases
- Manipulate database
    - querying
    - generating reports
    - insertions
    - deletions
    - modification to content
- Concurrent processing
- Protection or security

##### Schema's and Instances

| Terminology            | Description                                                          |
| ---                    | ---                                                                  |
| Database Schema        | The description of a database (database's purpose)                   |
| Schema Diagram         | A diagram display of some aspects of database schema                 |
| Database instance      | The actual data stored in a database *at one point in time*          |
| Database state         | Refers to content of database at a time (extension, occurrence)      |
| Data model             | A set of concepts used to describe the structure of a database       |
| Initial database state | Refers to the database when it is loaded                             |
| Valid state            | A state that satisfies the structure and constraints of the database |

An important distinction to make between database states and database schema is that **the
database schema changes very infrequently** and the **database state changes every time
the database is updated**.

**Internal Schema**

At this level, we are dealing with the files directly, this is about how things are stored
and how to achieve results, this is not for the user to interact with. This has lots of
detail about the database structure and storage. This is independent from the conceptual
view.

**Conceptual Schema**

This is where we can interact with the relationships between entities and make queries and
changes to the database. This has a bit of detail about storage but not that much. This is
independent from the internal level.

**External level**

This is where the end users only get what they desire from the database, the queries are
made for them in an automatic fashion. We can give different descriptions of the data for
different users (multiple viewing methods of data).

##### Database Features
- Data catalog (dictionary)
- Data abstraction
- Data integrity
- Data independence
    - Logical data independence
    - physical data independence
- Multiple views of data
- Sharing of data
- Controlled data redundancy (repeated stuff)
- Query languages
- Interfaces
- Backup and recovery
- Utilities

**People invlolved with Databases**
- Actors on the scene
    - Database administrators
    - Database designers
    - End-users
        - Casual users
        - Naive/Parametric users *("canned transactions")*
        - sophisticated users
        - standalone users
- Working behind the scene
    - DBMS designers and implementers
    - Tool developers
    - Operators and maintenance

##### Data Models
**Categories of Data Models**
- Conceptual
    - High level, semantic
    - Provide concepts that are close to the way many users percieve data
- Physical
    - Low level, internal
    - Provide concepts that are describe details of how data is stored
- Implementation
    - Provide concepts that fall between users views and computer storage details

#### Classification of DBMS's
- Based on data model used
    - Relational, Netowrk, Hierarchical
    - Emerging: Object-orientated Models

#### Don't Bother using DBMS for these Scenario's 
- small data set
- strict time requirements
- access by a single user
- not expecting data to change

### Database Design

This section is estimated to take around four lectures to complete

#### Data Modeling

##### Phases of Database Design
- Requirements collection and analysis
- Conceptual design
- Logical design
- Physical design

**Structural Component of ER**
- `Entities` are specific objects or things in the mini-world that are represented in the database
- `Attributes` are properties used to describe an entity
    - Name
    - SSN
    - Address
        - Number
        - Street
        - suburb
    - Gender
    - etc. 

Note that `Attributes` can have multiple sub-attributes bellow it. If this is the case it is said to be the value is *multi-valued*

- A specific entity will have a value for each of its attributes

Example of an entity with a few attributes
| Name         | SSN        | Address             | Gender | BirthDate   |
| ---          | ---        | ---                 | ---    | ---         |
| 'John Smith' | '12232333' | '731 Houston Drive' | 'Male' | '09-JAN-85' |

#### Types of attributes
**Simple (atomic) or Composite**
- *Gender* is a simple attribute
- *Name* (FirstName, MiddleName, LastName)
    - Composition may form a hierarchy where some components are themselves composite
**Single/Multi-valued**
- *previousDegrees* of a STUDENT
    - Denoted as `{PreviousDegrees}`

**Composite Multi-valued attribute**
- Denoted by: `{Degrees (University, Year, Degree, Field)}`
- In charts: *Double oval denotes multivalued attribute*

**Key Attributes**
- A key attribute may be composite
    - Denoted as `{CourseCode(CourseNo, UnitNo, AddressNo)}`
- A key cannot be multivalued
- It has to be a unique identifier
- A key attribute in a model will be underlined
- Strong entity types must contain at least one key attribute

##### The `NULL` Value
Has three possible interpretations
- Not known
- Not applicable
- Missing

#### Introduction to Relationships

Relationships are denoted using diamonds in the diagrams

**Relationship types**
- Is the schema description of a relationship
- Identifies the relationship name and the participating entity types
- Also identifies certain relationship constraints
- More than one relationship type can exist with the same entity types
- Relationship types can also have attributes associated with them
- Recursive Relationship Types
    - Both participants have the same entity type in different roles
    - (slides 2-26)

**Relationship Set**
- The current set of relationship instances represented in the database
- The current state of a relationship type

##### Dependent's

**Dependents**
- Denoted with double box
- connects to Depends relationship
- This is considered a *Weak Identity Type*

**Cardinality Ratio**

The types of relationships, and how they connect.

- One to one `(1:1)`
- One to many `(1:N)`
- Many to many `(N:N)`

**Participation Constraint**
- Total (existential)
- Partial

Minimum cardinality
    (also called existence dependency constraint)

**Structural Constraints**

If we want to put a minimum amount of people and maximum on a relationships cardinality ratio, we use the syntax `(min, max)` in the diagram.

**Lattice**

This is a type of structure where entity types end up at a single node, if this is to occur, it must all stem from the same parent class. If 
this is the case, it is possible to take on roles of multiple subclasses at the same level.

#### Relationship Diagrams

Assessment info on Learn, they have given us ER-Tutor to draw diagrams, they have given us model answers (also available on Learn).

##### Syntax of Diagrams

| Notation                 | Definition                                                  |
| --------                 | ----------                                                  |
| Underline                | Key attribute                                               |
| Square box               | Entity                                                      |
| Oval                     | Attributes                                                  |
| Double square            | Weak Entity Type                                            |
| Double Oval              | Multi-valued attribute                                      |
| ) on line                | Represents specialization as a subclass of the parent class |
| circle                   | represents multiple subclasses below parent                 |
| Double lines (Relations) | represents that there need to be plow both ways             |

##### Shit I need to know

An attribute can be associated with the relationship diamond when it shows an association
between two particular entities.

A week entity type can only have **One Partial Key**, in some cases it can be a composite
attribute if a set of attributes is required for unique identification

The values of completeness constraint are **Total / Partial**.

An entity type has a multivalued attribute, then there are some entities of this type
that have more than one value for that attribute.

A week entity type participates in the identifying relationship type **always totally**.

##### ER to Relational Mapping Algorithm

This is the algorithm to turn an ER model into a relational model

**NOTE:** *Steps for what to do are found in Lecture: July 31st, and corresponding slide-set*

A table is defined as a set of tuples, this means that we can not contain duplicate
entries.

### Relational Algebra

#### The Pie Operand

This is the Reject operation.

$\pi (A, C)$ if the tuple does not contain a key, it is possible to have < `N` entries
as there is a possibility that there are duplicate entries in the table (SET OF TUPLES).

If A or C is a key, the tuples cannot be the same because they have a unique identifier.

### The Omega Operand


$\sigma$ is used to define a select method. therefore if given the following:

Table: 

| A (key) | B   | C   |
| ---     | --- | --- |
| 1       | 1   | 2   |
| 2       | 2   | 1   |
| 3       | 3   | 2   |
| 4       | 1   | 2   |
| 5       | 2   | 1   |
| 6       | 3   | 3   | 

Here are some expressions/questions.


Q1: 

$\pi _(A, C) (R)$

This expression will give the following output table:

| A   | C   |
| --- | --- |
| 1   | 2   |
| 2   | 1   |
| 3   | 2   |
| 4   | 2   |
| 5   | 1   |
| 6   | 3   |

The table gives a result set that is of length `N` becuase A is a primary key.


$\pi _(B, C) (R)$

| B   | C   |
| --- | --- |
| 1   | 2   |
| 2   | 1   |
| 3   | 2   |
| 3   | 3   |

The reason that this result set `S < N` is because that if we look at the input table `Table`
we can see that there have been some results appearing multiple times, such as ($B _1, C _1$)

Q3:

$\sigma _(B > 1) (R)$

| $\underline{A}$ | B   | C   |
| ---             | --- | --- |
| 2               | 2   | 1   |
| 3               | 3   | 2   |
| 5               | 2   | 1   |
| 6               | 3   | 3   |

We can use a series of relational Algebra in order to imply a table as these things are
interchangable.

**Union compatible relations**
- same degree
- each pair of corresponding attreubutes have the same domain

- Union: $S \cup R$
- Intersection: $S \cap R$
- Set difference (minus) $S - R$

Properties of Union Intersect and Difference

- Both Union and intersect are Communatative
    - $R\cup S=S \cup R \quad AND \quad R \cap S = S \cap R$

#### Cartesian Product

- set operation
- does not require union compatible relations
- $S \times X$
- Binary operation
- Communatative

Example:

Table R:

| $\underline{A}$ | B   | C   |
| ---             | --- | --- |
| 1               | 1   | 2   |
| 2               | 2   | 1   |
| 3               | 3   | 2   |
| 4               | 1   | 2   |
| 5               | 2   | 1   |
| 6               | 3   | 3   |

Table S:

| $\underline{D}$ | E   | A    |
| ---             | --- | ---  |
| 1               | a   | 1    |
| 2               | b   | 2    |
| 3               | e   | 4    |
| 4               | a   | l    |
| 5               | c   | null |
| 6               | d   | 4    |
| 7               | f   | 2    |

Question: Find the cartesian Product

$S \times R$

| A   | B   | C   | D   | E   | A   |
| --- | --- | --- | --- | --- | --- |
| 1   | 1   | 2   | 1   | a   | 1   |
| 1   | 1   | 2   | 2   | 6   | 2   |
|     |     |     |     |     |     |
| 1   | 1   | 2   | 7   | f   | 2   |
| 2   | 2   | 1   | 1   | a   | 1   |
| 2   | 2   | 1   | 2   | 6   | 2   |
|     |     |     |     |     |     |
| 2   | 2   | 1   | 7   | f   | 2   |
|     |     |     |     |     |     |
| 6   | 3   | 3   | 7   | f   | 2   |

**Joins**

- Binary relational operation
- $R \bowtie_{<join condition>} S$
- join condition: $R.A = S.B$
- Example 8:
    - *Join the MOVIE and DVD tables*

The resulting table will have the same number of tuples as the DVD table, as a MOVIE
can have many DVD's. This is more efficent than Cartesian in this case as it does not
create every possible combination of MOVIE and DVD.

If we specify the condition in which it is joining, this is the variable we are joining
onto *This tends to be when the foreign key and primary key from different tables tend
to have the same name*

Aquajoin will not remove the double up of the keys, normal outer join will remove this
double contents.

#### Complete set of relational algebra operations
 
The set is as follows, this should allow us to derive any operation on a database from
these five different operations: 

`SET =`$\{\sigma, \pi, \cup, -, \times\}$

### SQL

- Terminology: tables, columns and rows
- Important distinction: between `SQL` and the formal relational model, `SQL` will allow
a table to contain multiple duplicate tuples.
- Hence an `SQL` relastion table is a *multi-set* of tuples; it is **Not** a set
of tuples.
- `SQL` relations can be constrained to be sets by specifying `PRIMARY KEY` or `UNIQUE`
attributes, or by using the `DISTINCT` option in a query.

#### Logical Design

*This is the process of going from a relational model to an DBMS specific outline
for this section we will be using Oracle*

**Oracle Syntax**

For the value of a primary key we cannot use the `NUMBER` as it is a reserved
word in Oracle, we must instead use `DNUMBER` for our unique identifiers

Comments: HTML/C Style /\* ... \*/ Multi-line comment or -- for single line.

```sql
-- single line comment

/* 
    Multi-line
    comment
*/
```

Example of setting values with constraints

```sql
-- This is an example of a statement in SQL --
BORN integer
    constraint dir_born check
        (BORN between 1880 and 1990);
```

We can also specify key, ability to hold nulls, other constraints and conditions.

Here is a full `SQL` example of a table:

```sql
/* This table is a table of movies, with the following attributes:
MNUMBER >> Unique Identifier
TITLE >> String length 50 chars (not null)
TYPE >> String length 15 not null
AANOM >> integer
AAWON >> integer
YEAR >> integer
CRITICS >> string length 2
DIRECTOR >> integer that references a primary key from another table (DIRECTOR table)
    Note: This foreign key MUST be the same type as the primary key
*/
CREATE TABLE MOVIE(
    MNUMBER Unique number not null PRIMARY KEY, 
    TITLE, varchar(50) not null,
    TYPE varchar(15) not null,
    AANOM integer,
    AAWON integer,
    YEAR integer,
    CRITICS varchar(2),
    DIRECTOR integer references DIRECTOR
);
```

#### Division

We can divide a table by another table. This means to remove the values from table B
in table A. This can be denoted using $A \div B$

Given two relations `R(X)` and `S(Z)`:

$R \div S = T(Y)$, this results in the corresponding association $Y = X - Z$, for
a tuple `t` to appear in `T`, the values in `t`   must appear in `R` in combination
with every *tuple* in `S`.


