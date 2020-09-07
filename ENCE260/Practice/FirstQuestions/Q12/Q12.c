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
    Task* task = NULL; 
    size_t allo = strlen(description) + 1;
    task = malloc(sizeof(Task));
    if (task != NULL) {
        task->description = malloc(allo);
        if (description != NULL) {
            strncpy(task->description, description, allo);
            task->duration = duration;
            task->priority = priority;
        } else {
            free(task);
            task = NULL;
        }
    }
    return task;
}

void freeTask(Task* task)
{
    // Freeing the allocated memory to description
    free(task->description);
    // Freeing the actual Task instance
    free(task);
}
