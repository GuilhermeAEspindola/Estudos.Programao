
#include<stdio.h>

void fparcela(float vrcompra,float qtparcela){
   float vparcela;	 
   if (qtparcela>0)
      vparcela = (vrcompra * 1.05) / qtparcela;
   else
      vparcela = vrcompra; 	   
   printf("Valor da Parcela = %f ",vparcela); 
}

main(){
   float vrcompra, qtparcela;
   printf("---- Calculo da Parcela ----");
   printf("\nEntre com Valor da Compra: ");
   scanf("%f",&vrcompra);
   printf("\nEntre com Qtde de Parcelas: ");
   scanf("%f",&qtparcela);
   fparcela(vrcompra,qtparcela);   
}
