#include<stdio.h>

int ftotalMinutos(int horas, int minutos){
   int vtotalMinutos = (horas*60) + minutos;	
   return (vtotalMinutos); 
}

main(){
   int horas, minutos,total; 
   printf("---- Calculo dos Minutos ----");
   printf("\nEntre com horas: ");
   scanf("%d",&horas);
   printf("\nEntre com minutos: ");
   scanf("%d",&minutos);
   total = ftotalMinutos(horas,minutos);
   printf("\nTotal em Minutos = %d ",total);   
}