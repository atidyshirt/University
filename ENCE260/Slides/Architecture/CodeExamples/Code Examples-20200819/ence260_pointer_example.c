/* ENCE260 Pointer Example
 *   A small example of using pointers in C
 *   Allan McInnes / 2018-06-21
 *
 * Build with: gcc -o pointer_example ence260_pointer_example.c
 */
 #include <stdio.h>

 void change_the_value_at_an_address(int* address) {
    *address = 128;
 }

 int main (int argc, char* argv[]) {
 	int varA = 42;
 	int varB[2] = {64, 256};
 	int* var_address;

    printf("Starting with these variables:\n");
    printf("int varA = 42;\n");
    printf("int varB[2] = {64, 256};\n");
    printf("int* var_address;\n");

    // Getting an address
    var_address = &varA; 
    printf("\n--> var_address = &varA;\n");
    printf("The address of varA is 0x%X\n", &varA);
    printf("The value of var_address is also 0x%X\n", var_address);    
    printf("The value of varA is %d\n", varA);
    printf("The value of *var_address is also %d\n", *var_address);

    // Dereferencing
    *var_address = *var_address + 1; 
    printf("\n--> *var_address = *var_address + 1;\n");    
    printf("The value of varA is now %d\n", varA); 
    printf("The value of var_address is still 0x%X\n", var_address);   

    // Reassigning a pointer
    var_address = &varB[0]; 
    printf("\n--> var_address = &varB[0];\n");    
    printf("The value of varB[0] is %d\n", varB[0]); 
    printf("The address of varB[0] is 0x%X\n", &varB[0]);    
    printf("The value of var_address is now 0x%X\n", var_address);  

    // Passing a pointer as an argument
    change_the_value_at_an_address(var_address);
    printf("\n--> change_the_value_at_an_address(var_address);\n");    
    printf("The value of varB[0] is now %d\n", varB[0]); 
    printf("The value of var_address is still 0x%X\n", var_address);   

    // Modifying a pointer (pointer arithmetic)
    var_address = var_address + 1;
    printf("\n--> var_address = var_address + 1;\n");   
    printf("The value of var_address is now 0x%X\n", var_address);  
    printf("The address of varB[1] is also 0x%X\n", &varB[1]);    
    printf("The value of *var_address is %d\n", *var_address);        
    printf("The value of varB[1] is also %d\n", varB[1]); 
    
    return 0;   
 }