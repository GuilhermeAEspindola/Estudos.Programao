import java.util.Scanner;
public class ex002 {

    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        int num1;
        int num2;
        int soma;

        System.out.println("Digíte o Primeiro Número: ");
        num1 = entrada.nextInt();
        
        System.out.println("Dígite o segundo Número: ");
        num2 = entrada.nextInt();

        soma = num1 + num2;

       System.out.println("A soma dos Números é; " + soma);

    }
}
