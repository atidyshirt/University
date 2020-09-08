#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char* description;
    float duration; // hours
    int priority;
} Task;

Task* newTask(char* description, float duration, int priority);
void freeTask(Task* task);

int main(void) 
{
    Task* task = newTask("Studying for ENCE260", 2.5f, 1);
    printf("Task \'%s\' (priority %d) takes %.1f hours.\n", task->description, task->priority, task->duration);
    freeTask(task);
}


Task* newTask(char* description, float duration, int priority)
{
    Task* tmp = NULL;
    tmp = malloc(sizeof(Task));
    if (tmp != NULL) {
        int descsize = strlen(description);
        tmp->description = malloc(descsize + 1); // need true size not one short for terminator
        if (tmp->description == NULL) {
            free(tmp);
            tmp = NULL;
        } else {
            strncpy(tmp->description, description, descsize + 1);
            tmp->duration = duration;
            tmp->priority = priority;
        }
    }
    return tmp;
}


void freeTask(Task* task)
{
    free(task->description);
    free(task);
}
