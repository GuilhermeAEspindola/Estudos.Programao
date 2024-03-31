#include<stdio.h>

float fvolume(float a, float l, float p){
   float vvolume = a * l * p; 
   return (vvolume); 
}
float converte(float cm){
	float m = cm / 100; 
	return (m); 
}
main(){
   float altura, largura, profundidade;
   float volume; 
   printf("---- Calculo do Volume da Caixa ----");
   printf("\nEntre com Altura: ");
   scanf("%f",&altura);
   printf("\nEntre com Largura: ");
   scanf("%f",&largura);
   printf("\nEntre com Profundidade: ");
   scanf("%f",&profundidade);
   volume = fvolume(altura,largura,profundidade);
   printf("\nVolume = %f ",converte(volume));   
}