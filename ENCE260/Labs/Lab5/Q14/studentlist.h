/* studentlist.h
 * Defines input and output operations on a linked list of students.
 *
 * Author: Richard Lobb
 * Date: August 2014, July 2019
 */
#ifndef STUDENT_LIST_H

#define STUDENT_LIST_H
#include <stdio.h>
#include "student.h"

/* Read a list of students from the given file and link them into a
 * list in order of appearance in the file.
 * Return a pointer to the first student.
 */
Student* readStudents(FILE* file);

// printStudents: print all students in a linked list of students, given a pointer
// to the first student in the list.
void printStudents(const Student* student);

// initilizing the findStudent function
const Student* findStudent(const Student* studentList, const char* name);

#endif /* end ifndef STUDENT_LIST_H */
