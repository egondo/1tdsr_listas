#include<stdio.h>
//exemplo de passagem de parametros por referencia
int dobro(int* x) {
    *x = 2 * (*x);
    return *x;
}

int main() {
    //int r = dobro(8);
    //printf("%d\n", r);
    int var = 10;
    int r = dobro(&var);
    printf("%d %d", r, var);
}