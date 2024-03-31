#include<stdio.h>

int farea(int la, int lb){
   int varea = (la * lb);	
   return (varea); 
}

main(){
   int ladoa,ladob; 
   printf("---- Calculo da Area ----");
   printf("\nEntre com lado A: ");
   scanf("%d",&ladoa);
   printf("\nEntre com lado B: ");
   scanf("%d",&ladob);
   printf("\nArea = %d ",farea(ladoa,ladob));   
}
