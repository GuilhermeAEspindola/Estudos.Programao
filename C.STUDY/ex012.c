#include<stdio.h>
int main()
{
    int a;
    printf("Dígite um numero: ");
    scanf("%d",&a);
    if ( a <= 10 )
    {
        printf("Valor Correto!");
    }
    else {
        
        printf("Valor Incorreto!");
    }
    return 0;
}
