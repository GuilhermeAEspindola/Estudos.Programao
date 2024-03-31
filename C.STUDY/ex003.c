#include<stdio.h>
float fdistancia(float kmi, float kmf){
	float d = kmf - kmi; 
	return(d);
}
float fconsumo(float d, float qtl){
	float c = d / qtl; 
	return(c); 
}
float fgasto(float p, float qtl){
	float vr = p * qtl; 
	return(vr);
}
main(){
    float kmi,kmf,qtlitros, precolitro,vdistancia; 
	// ler dados 
	printf("Km inicial: ");
	scanf("%f",&kmi);   
	printf("Km final: ");
	scanf("%f",&kmf);   
	printf("Qtde de Litros: ");
	scanf("%f",&qtlitros);   
	printf("Pre�o do Litro: ");
	scanf("%f",&precolitro);
	vdistancia = fdistancia(kmi,kmf); 
	printf("Distancia percorrida: %f ",vdistancia);
	printf("\nConsumo (Km/l): %f ",fconsumo(vdistancia,qtlitros));
	printf("\nValor Gasto (R$):  %f ",fgasto(precolitro,qtlitros));
}
