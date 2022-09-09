public class ex009 {
    public static void main(String[] args) {
        int idade =(int) (Math.random() * 96 )+ 1;

        System.out.println("idade" + idade);

        if(idade >= 18) {
            System.out.println("Pode Entrar Sozinho!");
        }else if (idade < 18 && idade >= 13) {
                System.out.println("Pode Entrar Acompanhado!");
        }else {
                System.out.println("Não Pode Entrar!");
            }
        
        }

}