#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>
#include <math.h>

// Common declarations
#define MAX_TEXTFILE_SIZE       4096
#define MAX_FILENAME_LENGTH       80
#define MAX_NUMBER_AGENTS         15
#define MAX_AGENTNAME_LENGTH      45
#define MAX_LINE_LENGTH           96

typedef struct {
    char name[MAX_AGENTNAME_LENGTH];
    size_t key;
} Agent;

typedef struct {
    size_t size;
    size_t next;
    Agent  pool[MAX_NUMBER_AGENTS];
} AgentPool;

size_t readText(FILE* file, char text[], size_t maxTextSize);
size_t readCipherBook(FILE* file, char text[], size_t maxTextSize);
size_t readMessage(FILE* file, char text[], size_t maxTextSize);

void initAgentPool(AgentPool* agentPool);
Agent* newAgent(AgentPool* agentPool);
void deleteAgent(Agent* agent, AgentPool* agentPool);
Agent* readAgent(FILE* file, AgentPool* agentPool);
Agent* findAgent(char name[], AgentPool* agentPool);
void readAgentName(char agentName[], size_t maxAgentNameLength);

Agent* newAgent(AgentPool* agentPool)
{
    if (agentPool->next != agentPool->size) {
        Agent* someone = agentPool->pool + agentPool->next;
        agentPool->next+=1;
        return someone;
    }
    return NULL;
}

int main(void)
{
    char filename[80] = "";
    char agentname[MAX_AGENTNAME_LENGTH] = "";
    FILE* file = NULL;
    AgentPool agentPool;
    Agent* agent;

    scanf("%80s", filename);
    initAgentPool(&agentPool);
    file = fopen(filename, "r");
    if (file == NULL) {
        printf("File not found... program will fail with segmentation fault\n");
    }
    while (!feof(file)) {
        agent = readAgent(file, &agentPool);
    }
    fclose(file);

    getchar();

    readAgentName(agentname, MAX_AGENTNAME_LENGTH);
    agent = findAgent(agentname, &agentPool);
    if (agent != NULL) {
        printf("Found Agent %s with key %zu\n", agent->name, agent->key);
    } else {
        printf("No Agent found by the name %s\n", agentname);
    }
    return 0;
}

Agent* findAgent(char name[], AgentPool* agentPool)
{
    while (agentPool->next != agentPool->size) {
        Agent* someone = agentPool->pool + agentPool->next;
        printf("%s %zu\n", someone->name, someone->key);
        if (strcmp(someone->name, name)) {
            return someone;
        }
        agentPool->next+=1;
    }
    return NULL;

}

// A function to initialise an AgentPool structure
void initAgentPool(AgentPool* agentPool)
{
    agentPool->size = MAX_NUMBER_AGENTS;
    agentPool->next = 0;
}

// A function to read a file with agent data in it, adding the agent to a agentlist and returning a reference to the agent
Agent* readAgent(FILE* file, AgentPool* agentPool)
{
    char line[MAX_LINE_LENGTH];
    int successAgentName = 0;
    int successAgentKey = 0;
    Agent* agent = newAgent(agentPool);

    if (fgets(line, MAX_LINE_LENGTH, file) && agent) {
        size_t i;
        for (i = 0; i < strlen(line) && line[i] != ',' && i < MAX_AGENTNAME_LENGTH-1; i++) {
            agent->name[i] = line[i];
        }
        agent->name[i] = '\0';
        while (i < strlen(line) && line[i] != ',') {
            i++;
        }
        if (line[i] == ',' && strlen(agent->name) > 0) {
            i++;
            successAgentName = 1;
            successAgentKey = sscanf(line+i, "%zu", &agent->key) == 1;
        }
    }
    if (agent && !(successAgentName && successAgentKey)) {
        deleteAgent(agent, agentPool);
        agent = NULL;
    }
    return agent;
}

// A function to delete an agent from an AgentPool
void deleteAgent(Agent* agent, AgentPool* agentPool)
{
    int i;
    int move = 0;
    for (i = 0; i < agentPool->next-1; i++) {
        if (move || &agentPool->pool[i] == agent) {
            move = 1;
            agentPool->pool[i] = agentPool->pool[i+1];
        }
    }

    agentPool->next--;
}

void readAgentName(char agentName[], size_t maxAgentNameLength)
{
    char c;
    size_t i;

    c = getchar();
    for (i = 0; i < maxAgentNameLength-1 && c != '\n'; i++) {
        agentName[i] = c;
        c = getchar();
    }
    agentName[i] = '\0';
}
