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
- 10% Weekly Quiz's
  - There will be around 13 of these (1% each)
- 20% Test (Friday 13 September, 6pm)
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

#### Using #define
```c
// These are known as Macro's
#define SECOND_NUMBER 20
#define FIRST_NUMBER 20 this is still legal 2020
```

This line is defining second number as 20, this means that every time we call the perameter
second number it means 20, As we can see by the FIRST_NUMBER definition, this is not the
same as assigning an integer within the body of the function, this is defining a term as a 
replacement for the symbol.
