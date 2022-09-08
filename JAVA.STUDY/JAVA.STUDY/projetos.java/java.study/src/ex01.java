public class ex01 {

	public static void main(String[] args) {
		int a = 55;
		int b = 77;
		double c = -45.66d;
		
		//usado para emcontrar o maior valor
		System.out.println(Math.max(a, b));
		//usado para encontrar menor numero
		System.out.println(Max.min(a,b));
		//raiz quadrada
		System.out.println(Math.sqrt(a));
		//absoluto positivo
		System.out.println(Math.abs(c));
		//numero aleatorio
		System.out.println(Math.random());
		
		System.out.println(Math.random() * 10)+1;
		
		int numero = (int)(Math.random() * 10)+1;
		System.out.println(numero);
		
		System.out.println(Math.PI);
		
		short pi = (short) Math.PI;
          
	}

}
