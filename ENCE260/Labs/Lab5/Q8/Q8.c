#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_LINE_LENGTH 80      // The longest line this program will accept
#define MAX_NUM_STUDENTS 500    // The maximum number of students this program can handle
#define MAX_NAME_SIZE 50        // The maximum allowable name length

typedef struct student_s Student;

struct student_s {
    char name[MAX_NAME_SIZE];
    int age;
    Student* next;              // Pointer to next student in a list
};

Student studentPool[MAX_NUM_STUDENTS];  // The student pool
int firstFree = 0;

Student* newStudent(const char* name, int age)
{
    Student* student = NULL;
    if (firstFree < MAX_NUM_STUDENTS) {
        student = &studentPool[firstFree];
        firstFree += 1;
        strncpy(student->name, name, MAX_NAME_SIZE);
        student->name[MAX_NAME_SIZE - 1] = '\0';  // Make sure it's terminated
        student->age = age;
        student->next = NULL;
    }
    return student;
}

Student* readOneStudent(FILE* file)
{
    char buffer[MAX_LINE_LENGTH] = {0};  // Buffer into which we read a line from stdin
    Student* student = NULL;       // Pointer to a student record from the pool

    char* inputLine = fgets(buffer, MAX_LINE_LENGTH, file);
    if (inputLine != NULL) {        // Proceed only if we read something
        char* commaPos = strchr(buffer, ',');
        if (commaPos != NULL) {
            int age = atoi(commaPos + 1);
            *commaPos = '\0';  // null-terminate the name
            student = newStudent(buffer, age);
        }
    }
    return student;
}

Student* readStudents(FILE *file)
{
    Student* first = NULL;     // Pointer to the first student in the list
    Student* last = (Student*)malloc(sizeof(struct Student*));      // Pointer to the last student in the list
    Student* student = readOneStudent(file);
    while (student != NULL) {
        if (first == NULL) {
            first = last = student;   // Empty list case
        } else {
            last->next = first;
            last = student;
        }
        student = readOneStudent(file);
    }
    return first;
}

void printOneStudent(Student student)
{
    printf("%s (%d)\n", student.name, student.age);
}

void printStudents(const Student* student)
{
    while (student != NULL) {
        printOneStudent(*student);
        student = student->next;
    }
}


int main(void)
{
    FILE* inputFile = stdin;
    if (inputFile == NULL) {
        fprintf(stderr, "File not found\n");
    } else {
        Student* studentList = readStudents(inputFile);
        printStudents(studentList);
    }
}
