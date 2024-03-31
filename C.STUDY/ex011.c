#include<stdio.h>
float velocidade(float distancia, float tempo){
    float velocidadecorrida = distancia / tempo;
    return(velocidadecorrida); 
}
int main(int argc, char const *argv[])
{
    float distancia, tempo,distancia2, tempo2,distancia3, tempo3;
    printf("digite a distancia percorrida do primeiro objeto: ");
    scanf("%f",&distancia);
    printf("digite o tempo que necessitou para percorrer essa distancia do primeiro objeto: ");
    scanf("%f",&tempo);
    printf("digite a distancia percorrida do segundo objeto: ");
    scanf("%f",&distancia2);
    printf("digite o tempo que necessitou para percorrer essa distancia do segundo objeto: ");
    scanf("%f",&tempo2);
    printf("digite a distancia percorrida do terceiro objeto: ");
    scanf("%f",&distancia3);
    printf("digite o tempo que necessitou para percorrer essa distancia do terceiro objeto: ");
    scanf("%f",&tempo3);
    printf("A velocidade percorrida pelo primeiro Objeto é de: %2.f KM/h velocidade percorrida\n",velocidade(distancia,tempo));
    printf("A velocidade percorrida pelo segundo Objeto é de: %2.f KM/h velocidade percorrida\n",velocidade(distancia2,tempo2));
    printf("A velocidade percorrida pelo terceiro Objeto é de: %2.f KM/h velocidade percorrida\n",velocidade(distancia3,tempo3));
    return 0;
}
