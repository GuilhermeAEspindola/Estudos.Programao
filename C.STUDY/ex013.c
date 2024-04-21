#include<stdio.h>
#include<locale.h>

int main()
{
  char turno;
  int horas;
  float valorHora;
  float salario;

  printf("Dígite o turno de trabalho(N para noturno e D para diurno); ");
  scanf("%c",&turno);

  printf("Dígite a quantidade de Horas Trabalhadas: ");
  scanf("%d",&horas);

  if (turno == "N")
  {
    valorHora = 45.0;
  }
  else{
    valorHora = 37.5;
  }
  salario = horas * valorHora;

printf("O valor do Salário é de: R$ %.2f Reais", salario);   
  
    return 0;
}
