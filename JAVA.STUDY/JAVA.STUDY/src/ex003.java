import java.util.Scanner;

/**
 * ex003
 */
public class ex003 {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        int num1;
        int num2;
        int subtração;

        System.out.println("Dígite o primeiro Número: ");
        num1 = entrada.nextInt();

        System.out.println("Dígite o segundo Número: ");
        num2 = entrada.nextInt();

        subtração = num1 - num2;

        System.out.println("A Subtração dos Numeros e: " + subtração);


    }
}
