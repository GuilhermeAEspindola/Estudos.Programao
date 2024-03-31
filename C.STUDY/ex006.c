#include<stdio.h>
#include<stdlib.h>
#include<math.h> 

int main()
{
     float a, b, c, delta, x1, x2;

     printf("Dígite o valor de a: ");
     scanf("%f",&a);

     printf("Dígite o valor de b: ");
     scanf("%f",&b);

     printf("Dígite o valor de c: ");
     scanf("%f",&c);
    
    delta = ((b*b)- 4 * a * c);
    x1 = (- b + (sqrt(delta))) / (2 * a);
    x1 = (- b - (sqrt(delta))) / (2 * a);
       
    printf("O valor de delta é: %.2f \n",delta);
    printf("O valor de X1 é: %.2f \n",x1);
    printf("O valor de X2 é: %.2f \n",x2);

}
