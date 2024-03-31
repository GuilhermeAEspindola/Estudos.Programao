# include<stdio.h>
float converteDolar(float conversao){
float converteDolar1 = conversao / 5.02;
   return(converteDolar1);///
}
int main()
{
    float a,b;
    printf("Dígite o valor em reais: ");
    scanf("%f",&a);
    b = converteDolar(a);
    printf("O valor convertido de Real para Dólar é: $ %.2f\n ",b);

    return 0;
}