#include<stdio.h>

float arrecadacao(float a){
    float valorTotaltelheiro = a * 1.05;
    return(valorTotaltelheiro); 
}
float arrecadacao2(float a){
    float valorTotalquadrados = a * 0.51;
    return(valorTotalquadrados);
}
float valorTotal(float a ,float b){
    float valortotal1 = a + b;
    return(valortotal1);
}
float comissao(float a, float b){
    float comissao1 = ((a * 1.05 + b * 0.51) / 10);
    return(comissao1);
}
int main()
{
    float telheiro, quadrado;
    printf("Dígite a quantidade que foi vendido de pregos telheiros: ");
    scanf("%f", &telheiro);
    printf("Dígite a quantidade que foi vendido de pregos quadrados: ");
    scanf("%f",&quadrado);
    printf("O valor total de pregos telheiros que foram vendidos é de: R$ %2.f Reais.\n",arrecadacao(telheiro));
    printf("O valor total de pregos quadrados que foram vendidos é de: R$ %2.f Reais.\n",arrecadacao2(quadrado));
    printf("A quantidade total de pregos que foram vendidos foram de: %2.f Unidades.\n",valorTotal(telheiro,quadrado));
    printf("Ira receber de comissão total de pregos vendidos valor de: R$ %2.f Reais.\n",comissao(telheiro,quadrado));
    return 0;

}
