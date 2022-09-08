import java.util.Scanner;

//ex 005 multiplicação
public class ex005 {
    public static void main(String[]args){
        Scanner entrada = new Scanner(System.in);
        int num1;
        int num2;
        int divisão;
        System.out.println("Dígite um Numero: ");
        num1 = entrada.nextInt();
        System.out.println("Dígite  outro Numero: ");
        num2 = entrada.nextInt();
        divisão = num1 ** num2;
        System.out.println("A Soma dos Números é:" + divisão);
    }
}
