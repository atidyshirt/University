#include <stdio.h>

struct a {int b; } c;
struct a d;
struct a* e;

int main(void)
{
    c.b = 1;
    printf("%d\n", c.b);
    d.b = c.b;
    printf("%d\n", d.b);
    /* c->b = 1; will not work as we are refering to something that is not a pointer */
    /* printf("%d\n", c->b); */
    /* a e; */
    /* print("%d", a e); */
    e->b = 1;
    printf("%d\n", e->b); // Returns nothing, why?
    d.b = e->b;
    printf("%d\n", d.b); // Again same thing, why?
    /* d->b = 1; */
    /* printf("%d\n", d->b); This needs to be refered to as a literal, as it is not declared as a pointer */
    /* struct a f; // legal, however undefined */
    /* print("%d\n", f); // Wont print as it is undefined */
}
