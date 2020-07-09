class Math {
	int add(int a, int b) {
		return a+b;
	}
}


public class Calc {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Math math = new Math() ;
		System.out.println("3 + 9 = " + math.add(3, 9));
	}

}
