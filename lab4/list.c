#include <stdlib.h>
#include <stdio.h>
struct list
{
    struct list * nastepny;
    int var;
    

};

int main(){
    struct list element;
    printf("%s",element.nastepny);
    return 0;
}