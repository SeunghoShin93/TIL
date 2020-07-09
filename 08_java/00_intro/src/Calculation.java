class Calc2 {
	int add(int a, int b) {
		return a + b ;
	}
}

public class Calculation {
	static void disp() {
		int c ;
		Calc2 calc = new Calc2();
		c = calc.add(8, 9);
		System.out.println("8 + 9 = " + c);
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		disp();
	}

}
