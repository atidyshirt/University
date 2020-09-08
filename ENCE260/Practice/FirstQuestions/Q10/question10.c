#include <stdio.h>

typedef struct Pizza_s Pizza;

struct Pizza_s {
    char* type;
    int energy;
    double price;
};

int main(void)
{
    Pizza pizza = {"Hawaiian", 929, 1.0};
    printf("A slice of %s pizza costs $%.2f and contains %d kJ of energy.\n", pizza.type, pizza.price, pizza.energy);
}
