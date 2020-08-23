/* studentlist.c: implements the StudentList type defined in
 * studentlist.h
 *
 * Author: Richard Lobb
 * Date: August 2014, updated July 2019.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "student.h"
#include "studentlist.h"

// Reads a list of students from a given file. Input stops when
// a blank line is read, or an EOF occurs, or an illegal input
// line is encountered.
// Returns a pointer to the first student in the list or NULL if no
// valid student records could be read.
Student* readStudents(FILE *file)
{
    Student* first = NULL;     // Pointer to the first student in the list
    Student* last = NULL;      // Pointer to the last student in the list
    Student* student = readOneStudent(file);
    while (student != NULL) {
        if (first == NULL) {
            first = last = student;   // Empty list case
        } else {
            last->next = student;
            last = student;
        }
        student = readOneStudent(file);
    }
    return first;
}

const Student* findStudent(const Student* studentList, const char* name)
{
    int i = 0;
    while (i <= (500 / 16)) {
        if (strcmp(studentList[i].name, name) == 0) {
            return &studentList[i];
        } i++;
    } 

    return NULL;

}

// printStudents: print all students in a list of students, passed
// by reference
void printStudents(const Student* student)
{
    while (student != NULL) {
        printOneStudent(*student);
        student = student->next;
    }
}


