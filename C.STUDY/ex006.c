#include<stdio.h>
#include<stdlib.h>
#include<math.h> 
float delta (float a,float b,float c){
   float delta1 = (b*b) - 4 * a * c;
   return(delta1);
      
}
float x(float a, float b){
   float x1 =(- b + (sqrt(x1))) / (2 * a);
    return(x1);
}
float x1(float b, float a){
    float x2 = (- b - (sqrt(x2))) / (2 * a);
    return(x2);
}
int main()
{
     float a, b, c;

     printf("Dígite o valor de a: ");
     scanf("%f",&a);

     printf("Dígite o valor de b: ");
     scanf("%f",&b);

     printf("Dígite o valor de c: ");
     scanf("%f",&c);
    
    ///delta = ((b*b)- 4 * a * c);
    ///x1 = (- b + (sqrt(delta))) / (2 * a);
    ///x1 = (- b - (sqrt(delta))) / (2 * a);
       
    printf("O valor de delta é: %.2f \n",delta(a,b,c));
    printf("O valor de X1 é: %.2f \n",x(b,a));
    printf("O valor de X2 é: %.2f \n",x1(b,a));

}
