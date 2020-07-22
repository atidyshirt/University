<center>

# ENCE260 Notes - Computer Systems

</center>

> [TOC]

### General Info About Course

The goal of this course is to introduce and get familiar with linux and to teach you how to program in C. In this course the notes will be split into 3 major chunks throughout the year.

1. C Programming
2. Computer Architecture
3. Embedded System's

Textbook: None

Recommended text to read (C programming)

#### Grading

- 10% C Programming Assignment
  - (this is a three part super quiz)
- 10% Embedded Systems Assignment (Term 4)
  - Date: Monday 12th October
- 10% Weekly Quiz's
  - Dates: Each one will be on quiz server
  - There will be around 13 of these (0.8% each)
- 20% Test
  - Date: Monday 7th September 7pm
- 50% Final Exam (does not include C programming)

#### Resources

- K. N. King, C programming: a modern approach (2nd Edition) (Recommended not required)
- [Lecture notes, Recordings and slides](https://learn.canterbury.ac.nz/course/view.php?id=9078&section=1)
- [C Style Guide](https://learn.canterbury.ac.nz/mod/resource/view.php?id=1346587)
- [C Refrence](https://en.cppreference.com/w/c)

### Introduction and C Basics

#### Memory Organisation

- C programs should be structured as follows:
  - Program code (text)
  - Global and static data (data)
  - Uninitilized global data (bss)
  - Dynamic memory (heap)
  - scratch pad memory (stack)

#### Basic Hello World!

```c
// This line is including the header which contains a vast amount of C
#include <stdio.h>
// sepcifies the return type, main body function, and takes in void perameters
int main(void) {
  // Despite printing a string, this function will return 0, if return != 0 --> error
  printf("Hello World\n");
  return 0;
}
```

#### Declaring Variables

```c
#include <stdio.h>

# define A_CONSTANT 30 //this is how to define constants

int main(void) {
//Declorations are as follows
  int number1; // int means dedicate 4 bits to a number
  int number2;
  int total;

//Manipulation of variables
  number1 = 10;
  number2 = 20;
  total = number1 + number2;
  printf("The sum of %d and %d is %d\n", number1, number2, total);
  return 0
}
```

#### Using Macro's

The `#define` tag is used to assign macro's in C, this will be completed in-line with other
arithmetic. This is used to re-assign stock symbols and will execute the arithmetic where it
is placed in the file.

```c
// These are known as Macro's
#define SECOND_NUMBER 20
#define FIRST_NUMBER 20 this is still legal 2020
```

This line is defining second number as 20, this means that every time we call the parameter
second number it means 20, As we can see by the FIRST_NUMBER definition, this is not the
same as assigning an integer within the body of the function, this is defining a term as a
replacement for the symbol.

##### Macro's for arithmetic

As previously noted, we can re-define symbols using Macro's. This means that arithmetic works
in the same way as you would expect, so if we define a calculation as the macro, every time we
use it it will be evaluated in line with the expression. Here is an example.

```C
#define TEST 4 + 2

int main(void) {
  int val = TEST * TEST;
  printf("%i\n" val);
}
```

> This will use in-line math to result in the following output: 14

#### C Error Messages

The C error messaging system is considerably more cryptic than that seen in the Python
interpreter. It is harder to follow, and the key point to take away is that **Not all
error messages will point to exactly where the error is unlike python sometimes you
will have to find the error yourself**.

#### The Celsius function

```C
#include <stdio.h>
#include <stdlib.h>

#define FREEZING_PT 32.0
#define SCALE_FACTOR (5.0 / 9.0)

int main(void) {
  float fahrenheit = 0.0;
  float celsius = 0.0;
  printf("Enter Fahrenheit temperature: ");
  scanf("%f", &fahrenheit);
  celsius = (fahrenheit - FREEZING_PT) * SCALE_FACTOR;
  printf("Celsius equivilent: %.1f\n", celsius);
  return EXIT_SUCCESS;
}
```

### How Memory Works

Memory at the lower levels is just a series of bits. C treats memory the same way as it has
no object store or _heap_. Each piece of memory used is allocated a byte sized number to
tell us where it is stored, this is known as an _address_, (if we have a 4GB machine, then
there is 4 Billion bytes to store this information).

#### a = b

Because of the above, the assignment operator _a = b_, is actually saying, go to memory location
_b_ and copy all the bytes of _b_ to memory location _a_. This is raw byte copying, this is
different to python in the fact that python stores the name in a dictionary as an object.

#### Basic Data Types

- Integers
  - unsigned
  - signed
  - long
  - short
  - int
- Floating Point Integers
  - float
  - double
- Characters
  - char
  - always 8-bit ASCII encoding (1-byte)
- Complex Floating Point
  - not covered in ENCE260
- Boolean
  - \_Bool (or just _bool_ if #include <stdbool.h>)

```C
int a = 0;
short int b = 1;
signed long long int x = 256;
short c = 20; // Don't have to expand
long d = 50;
```

The different variables tell it how much memory to allocate to each variable, for instance
**char** allocates 1-byte, **short** allocates 2-bytes, **int** allocates 4-bytes and **long
long int** allocates 8-bytes.

### Computer Architecture

#### Digital Logic

Analog Information

- defined by quantity

Digital Information

- true/false
- yes/no
- pairs well with logic values
- switches on/off

Logical variable, represents true or false, and is denoted by `varName = true`

**Logical functions**

- the limited set of values that logical variables can take (0, 1, true or false)
- makes it feasible to write out every possible combination

**Fundamental Functions**

`NOT`

- $f(a = a')$

`AND`

- $f(a,b) = a * b$

`OR`

#### Boolean Algebra

- closure
  - for $a,b \in B$ then $a*b \in B$
- Identity $a*i = a$ therefore
  - $a*1 = a$
  - $a + 0 = a$
- Associative $a * (b*c) = (a*b)*c$
- Communatative $a*b = b*a$

#### Expressions

**General Operators**

These are mostly like python except:

- No exponential operator
- `/` operator behaves like Python's `//` (integer devision by default)
- Logical operators are different
    - `and = &&`
        - single `&` acts as bitwise
    - `or = ||`
        - single `|` acts as bitwise
    - `not = !`
    - `++, --` are used as increment operators
        - pre-increment `++j`
        - post-increment `j--`
    - Assignment operator `=` is used anywhere in expressions
        * e.g. $foobar = (foo = 2) + (bar = 10)$
        * only use in simple assignment statements

**If Statements**
* Syntax in BNF notation
    - `::=` means *is defined as*
    - `|` denotes *or*
    - Tokens in double quotes are *terminals*
    - Other tokens are expanded by their own syntax definitions
* Note the parentheses around the condition expression

**To use Boolean Values**

To use boolean values, we must include *stdbool.h* into the program, this will give us a 
boolean value to use, the following will be the code to use boolean values.

```c
#include <stdbool.h>

int main(void)
{
    bool bigger = 6 > 5;
}
```

**The Switch Statement**

The switch statement uses a series of cases, and acts similar to that of the switch statement
found in `Java`.

```c
// Example of switch statement
switch ( expression ) {
    case constant-expression1 :
        // statement if case complies
        break;
    case constant-expression2 :
        // statement if case complies
        break;
    default :
        // the final case that is carried out if all above cases do not comply
}
```

