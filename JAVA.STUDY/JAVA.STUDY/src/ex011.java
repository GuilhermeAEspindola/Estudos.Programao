public class ex011{
    public static void main(String[] args) {
        int diadasemana = (int) (Math.random() * 7) + 1;

        switch(diadasemana){
            case 1:
            System.out.println("Domingo");
            break;
            case 2:
            System.out.println("Segunda");
            break;
            case 3:
            System.out.println("Terça");
            break;
            case 4:
            System.out.println("Quarta");
            break;
            case 5:
            System.out.println("Quinta");
            break;
            case 6:
            System.out.println("Sexta");
            break;
            case 7:
            System.out.println("Sábado");
            break;
            default:
            System.out.println("Valor Inválido");
        }
    }
}
