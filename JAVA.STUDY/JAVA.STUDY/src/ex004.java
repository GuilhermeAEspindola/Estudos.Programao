import java.util.Scanner;

public class ex004 {
    public static void main(String[] args) {
       Scanner entrada = new Scanner(System.in);

       int num1;
       int num2;
       int Multiplicação;

       System.out.println("Dígite um Número: ");
       num1 = entrada.nextInt();

       System.out.println("Dígite um Número: ");
       num2 = entrada.nextInt();

       Multiplicação = num1 * num2;
       System.out.println("A Multiplicação dos Números é: " + Multiplicação);   
    }
}
